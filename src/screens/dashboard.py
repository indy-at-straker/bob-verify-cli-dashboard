"""Dashboard screen for Straker Verify application."""

import asyncio
from typing import List, Optional

from textual.app import ComposeResult
from textual.containers import Container, Horizontal, Vertical, VerticalScroll
from textual.screen import Screen
from textual.widgets import Button, Label, Static
from textual.reactive import Reactive

from ..api.client import StrakerVerifyClient
from ..api.models import Project, ProjectStats
from ..config import Settings
from ..utils.formatters import (
    format_number,
    format_percentage,
    format_quality_bar,
    format_status_badge,
    format_time_ago,
)


class StatBox(Static):
    """Widget for displaying a statistic."""

    def __init__(self, label: str, value: str, **kwargs):
        """Initialize stat box.
        
        Args:
            label: Stat label
            value: Stat value
            **kwargs: Additional widget arguments
        """
        super().__init__(**kwargs)
        self.label_text = label
        self.value_text = value

    def compose(self) -> ComposeResult:
        """Compose the stat box.
        
        Yields:
            Stat box widgets
        """
        yield Label(self.value_text, classes="stat-value")
        yield Label(self.label_text, classes="stat-label")


class ProjectCard(Static):
    """Widget for displaying a project card."""

    def __init__(self, project: Project, **kwargs):
        """Initialize project card.
        
        Args:
            project: Project to display
            **kwargs: Additional widget arguments
        """
        super().__init__(**kwargs)
        self.project = project

    def compose(self) -> ComposeResult:
        """Compose the project card.
        
        Yields:
            Project card widgets
        """
        # Project header with name and status
        with Horizontal(classes="project-header"):
            yield Label(self.project.name)
            yield Static(format_status_badge(self.project.status.value))
        
        # Language pair and time
        with Horizontal(classes="project-meta"):
            yield Label(self.project.language_pair)
            yield Label(format_time_ago(self.project.updated_at))
        
        # Quality score if available
        if self.project.quality_score:
            quality_text = f"Quality: {format_quality_bar(self.project.quality_score.overall)} {format_percentage(self.project.quality_score.overall)}"
            yield Label(quality_text)


class DashboardScreen(Screen):
    """Main dashboard screen."""

    CSS = """
    DashboardScreen {
        background: $surface;
    }
    
    .stats-container {
        height: 7;
        margin: 1;
    }
    
    .stat-box {
        width: 1fr;
        height: 100%;
        border: solid $primary;
        padding: 1;
        content-align: center middle;
    }
    
    .projects-scroll {
        height: 1fr;
        margin: 1;
    }
    
    .project-card {
        height: auto;
        border: solid $primary;
        margin-bottom: 1;
        padding: 1;
    }
    
    .loading {
        content-align: center middle;
        height: 100%;
    }
    
    .error {
        background: $error;
        color: $text;
        padding: 1;
        margin: 1;
    }
    """

    stats: Reactive[Optional[ProjectStats]] = Reactive(None)
    projects: Reactive[List[Project]] = Reactive([])
    is_loading: Reactive[bool] = Reactive(True)
    error_message: Reactive[Optional[str]] = Reactive(None)

    def __init__(self, settings: Settings, **kwargs):
        """Initialize dashboard screen.
        
        Args:
            settings: Application settings
            **kwargs: Additional screen arguments
        """
        super().__init__(**kwargs)
        self.settings = settings
        self.client: Optional[StrakerVerifyClient] = None

    def compose(self) -> ComposeResult:
        """Compose the dashboard screen.
        
        Yields:
            Dashboard widgets
        """
        if self.is_loading:
            yield Container(
                Label("Loading dashboard...", classes="loading"),
                classes="loading",
            )
        elif self.error_message:
            yield Container(
                Label(f"Error: {self.error_message}", classes="error"),
                classes="error",
            )
        else:
            # Stats panel
            with Horizontal(classes="stats-container"):
                if self.stats:
                    yield StatBox(
                        "Projects",
                        format_number(self.stats.total_projects),
                        classes="stat-box",
                    )
                    yield StatBox(
                        "Active",
                        format_number(self.stats.active_projects),
                        classes="stat-box",
                    )
                    yield StatBox(
                        "Avg Quality",
                        format_percentage(self.stats.average_quality) if self.stats.average_quality else "N/A",
                        classes="stat-box",
                    )
                    yield StatBox(
                        "Files",
                        format_number(self.stats.total_files),
                        classes="stat-box",
                    )
            
            # Projects list
            with VerticalScroll(classes="projects-scroll"):
                if self.projects:
                    for project in self.projects:
                        yield ProjectCard(project, classes="project-card")
                else:
                    yield Label("No projects yet. Create one to get started!")

    async def on_mount(self) -> None:
        """Handle screen mount event."""
        await self.load_data()

    async def load_data(self) -> None:
        """Load dashboard data from API."""
        try:
            self.is_loading = True
            self.error_message = None
            
            # Initialize client
            self.client = StrakerVerifyClient(
                api_key=self.settings.straker_verify_api_key,
                base_url=self.settings.straker_verify_base_url,
            )
            
            # Show notification about API mode
            if self.client.use_real_api:
                self.app.notify("✓ Connected to Straker Verify API", severity="information", timeout=3)
            else:
                self.app.notify("ℹ Using demo mode with mock data", severity="warning", timeout=3)
            
            # Load stats and projects
            self.stats = await self.client.get_stats()
            self.projects = await self.client.list_projects()
            
            # Sort projects by update time (most recent first)
            self.projects.sort(key=lambda p: p.updated_at, reverse=True)
            
        except Exception as e:
            self.error_message = str(e)
            self.app.notify(f"Error: {str(e)}", severity="error")
        finally:
            self.is_loading = False
            # Refresh the screen to show new data
            await self.recompose()

    async def refresh_data(self) -> None:
        """Refresh dashboard data."""
        await self.load_data()

    def watch_is_loading(self, is_loading: bool) -> None:
        """Watch loading state changes.
        
        Args:
            is_loading: New loading state
        """
        if not is_loading:
            # Trigger recompose when loading completes
            self.call_later(self.recompose)

    def watch_error_message(self, error_message: Optional[str]) -> None:
        """Watch error state changes.
        
        Args:
            error_message: New error message
        """
        if error_message:
            self.call_later(self.recompose)
    
    async def on_unmount(self) -> None:
        """Handle screen unmount event - cleanup resources."""
        if self.client:
            await self.client.close()