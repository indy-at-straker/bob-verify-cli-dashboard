"""Main Textual application for Straker Verify Dashboard."""

from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.containers import Container, Horizontal, Vertical
from textual.widgets import Footer, Header, Static

from .config import Settings
from .screens.dashboard import DashboardScreen


class StrakerVerifyApp(App):
    """Straker Verify Dashboard TUI Application."""

    CSS = """
    Screen {
        background: $surface;
    }
    
    .header-container {
        dock: top;
        height: 3;
        background: $primary;
        color: $text;
    }
    
    .title {
        content-align: center middle;
        text-style: bold;
    }
    
    .balance {
        dock: right;
        width: 20;
        content-align: right middle;
        padding-right: 2;
    }
    
    .main-container {
        height: 100%;
    }
    
    .stats-panel {
        height: 5;
        border: solid $primary;
        margin: 1;
    }
    
    .stat-box {
        width: 1fr;
        height: 100%;
        content-align: center middle;
        border-right: solid $primary;
    }
    
    .stat-box:last-child {
        border-right: none;
    }
    
    .stat-value {
        text-style: bold;
        color: $accent;
    }
    
    .stat-label {
        color: $text-muted;
    }
    
    .projects-container {
        height: 1fr;
        border: solid $primary;
        margin: 1;
        padding: 1;
    }
    
    .project-card {
        height: 6;
        border: solid $primary;
        margin-bottom: 1;
        padding: 1;
    }
    
    .project-header {
        text-style: bold;
    }
    
    .project-meta {
        color: $text-muted;
    }
    
    .action-menu {
        dock: bottom;
        height: 3;
        background: $panel;
        content-align: center middle;
    }
    
    .error-message {
        background: $error;
        color: $text;
        padding: 1;
        margin: 1;
    }
    
    .success-message {
        background: $success;
        color: $text;
        padding: 1;
        margin: 1;
    }
    """

    BINDINGS = [
        Binding("n", "new_project", "New Project", show=True),
        Binding("u", "upload_file", "Upload File", show=True),
        Binding("p", "view_projects", "Projects", show=True),
        Binding("s", "settings", "Settings", show=True),
        Binding("r", "refresh", "Refresh", show=True),
        Binding("q", "quit", "Quit", show=True),
    ]

    def __init__(self, settings: Settings):
        """Initialize the application.
        
        Args:
            settings: Application settings
        """
        super().__init__()
        self.settings = settings
        self.title = "Straker Verify Dashboard"
        self.sub_title = "Translation Quality Management"

    def compose(self) -> ComposeResult:
        """Compose the application layout.
        
        Yields:
            Application widgets
        """
        yield Header()
        yield Footer()

    def on_mount(self) -> None:
        """Handle application mount event."""
        # Push the dashboard screen
        self.push_screen(DashboardScreen(self.settings))

    def action_new_project(self) -> None:
        """Handle new project action."""
        self.notify("New Project - Coming soon!", severity="information")

    def action_upload_file(self) -> None:
        """Handle upload file action."""
        self.notify("Upload File - Coming soon!", severity="information")

    def action_view_projects(self) -> None:
        """Handle view projects action."""
        self.notify("View Projects - Coming soon!", severity="information")

    def action_settings(self) -> None:
        """Handle settings action."""
        self.notify("Settings - Coming soon!", severity="information")

    def action_refresh(self) -> None:
        """Handle refresh action."""
        self.notify("Refreshing...", severity="information")
        # Trigger refresh on current screen
        if hasattr(self.screen, "refresh_data"):
            self.screen.refresh_data()

    def action_quit(self) -> None:
        """Handle quit action."""
        self.exit()