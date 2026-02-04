"""Straker Verify API client wrapper.

This module provides a wrapper around the Straker Verify API.
For demo purposes, it includes a mock implementation that simulates API behavior.
"""

import asyncio
import random
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional
from uuid import uuid4

from .models import (
    FileInfo,
    Language,
    Project,
    ProjectCreate,
    ProjectStats,
    ProjectStatus,
    QualityScore,
    Segment,
    TokenBalance,
)


class StrakerVerifyClient:
    """Client for interacting with Straker Verify API.
    
    This is a mock implementation for demo purposes. In production,
    this would use the actual straker-verify Python SDK.
    """

    def __init__(self, api_key: str, base_url: str = "https://api-verify.straker.ai"):
        """Initialize the Straker Verify client.
        
        Args:
            api_key: Straker Verify API key
            base_url: API base URL
        """
        self.api_key = api_key
        self.base_url = base_url
        self._projects: Dict[str, Project] = {}
        self._token_balance = 10000
        
        # Initialize with some sample data for demo
        self._init_sample_data()

    def _init_sample_data(self) -> None:
        """Initialize sample data for demo purposes."""
        # Create a completed project
        project1 = Project(
            id=str(uuid4()),
            name="Marketing_Campaign_ES",
            description="Marketing campaign translation to Spanish",
            source_language="en",
            target_language="es",
            status=ProjectStatus.COMPLETE,
            quality_score=QualityScore(
                overall=87.5,
                accuracy=92.0,
                fluency=85.0,
                terminology=88.0,
                style=84.0,
            ),
            files=[
                FileInfo(
                    id=str(uuid4()),
                    name="campaign_content.txt",
                    size=2048,
                    mime_type="text/plain",
                    uploaded_at=datetime.now() - timedelta(hours=2),
                )
            ],
            segments=[
                Segment(
                    id=str(uuid4()),
                    source_text="Welcome to our new product launch event.",
                    target_text="Bienvenido a nuestro evento de lanzamiento de producto.",
                    quality_score=QualityScore(
                        overall=95.0,
                        accuracy=98.0,
                        fluency=94.0,
                        terminology=96.0,
                        style=92.0,
                    ),
                ),
                Segment(
                    id=str(uuid4()),
                    source_text="Join us for an exciting showcase of innovation.",
                    target_text="Únase a nosotros para una emocionante exhibición de innovación.",
                    quality_score=QualityScore(
                        overall=88.0,
                        accuracy=90.0,
                        fluency=86.0,
                        terminology=89.0,
                        style=87.0,
                    ),
                ),
                Segment(
                    id=str(uuid4()),
                    source_text="Experience the future of technology today.",
                    target_text="Experimente el futuro de la tecnología hoy.",
                    quality_score=QualityScore(
                        overall=82.0,
                        accuracy=88.0,
                        fluency=78.0,
                        terminology=84.0,
                        style=78.0,
                    ),
                    issues=["Minor fluency issue detected"],
                ),
            ],
            created_at=datetime.now() - timedelta(hours=3),
            updated_at=datetime.now() - timedelta(hours=1),
            completed_at=datetime.now() - timedelta(hours=1),
            human_verified=False,
        )
        self._projects[project1.id] = project1

        # Create a processing project
        project2 = Project(
            id=str(uuid4()),
            name="Product_Docs_FR",
            description="Product documentation translation to French",
            source_language="en",
            target_language="fr",
            status=ProjectStatus.PROCESSING,
            files=[
                FileInfo(
                    id=str(uuid4()),
                    name="user_manual.pdf",
                    size=15360,
                    mime_type="application/pdf",
                    uploaded_at=datetime.now() - timedelta(minutes=5),
                )
            ],
            created_at=datetime.now() - timedelta(minutes=10),
            updated_at=datetime.now() - timedelta(minutes=1),
        )
        self._projects[project2.id] = project2

    async def get_languages(self) -> List[Language]:
        """Get list of supported languages.
        
        Returns:
            List of supported languages
        """
        await asyncio.sleep(0.1)  # Simulate API call
        return [
            Language(id="en", code="en", name="English"),
            Language(id="es", code="es", name="Spanish"),
            Language(id="fr", code="fr", name="French"),
            Language(id="de", code="de", name="German"),
            Language(id="it", code="it", name="Italian"),
            Language(id="pt", code="pt", name="Portuguese"),
            Language(id="ja", code="ja", name="Japanese"),
            Language(id="zh", code="zh", name="Chinese"),
        ]

    async def get_token_balance(self) -> TokenBalance:
        """Get current token balance.
        
        Returns:
            Token balance information
        """
        await asyncio.sleep(0.1)  # Simulate API call
        return TokenBalance(balance=self._token_balance)

    async def create_project(self, project_data: ProjectCreate) -> Project:
        """Create a new project.
        
        Args:
            project_data: Project creation data
            
        Returns:
            Created project
        """
        await asyncio.sleep(0.2)  # Simulate API call
        
        project = Project(
            id=str(uuid4()),
            name=project_data.name,
            description=project_data.description,
            source_language=project_data.source_language,
            target_language=project_data.target_language,
            status=ProjectStatus.PENDING,
            files=[],
            segments=[],
            created_at=datetime.now(),
            updated_at=datetime.now(),
        )
        
        self._projects[project.id] = project
        return project

    async def upload_file(
        self, project_id: str, file_path: Path
    ) -> FileInfo:
        """Upload a file to a project.
        
        Args:
            project_id: Project ID
            file_path: Path to file to upload
            
        Returns:
            File information
            
        Raises:
            ValueError: If project not found or file doesn't exist
        """
        if project_id not in self._projects:
            raise ValueError(f"Project {project_id} not found")
        
        if not file_path.exists():
            raise ValueError(f"File {file_path} not found")
        
        await asyncio.sleep(0.5)  # Simulate upload
        
        file_info = FileInfo(
            id=str(uuid4()),
            name=file_path.name,
            size=file_path.stat().st_size,
            mime_type="text/plain",  # Simplified for demo
            uploaded_at=datetime.now(),
        )
        
        project = self._projects[project_id]
        project.files.append(file_info)
        project.status = ProjectStatus.PROCESSING
        project.updated_at = datetime.now()
        
        # Simulate processing by generating segments
        await self._simulate_processing(project_id)
        
        return file_info

    async def _simulate_processing(self, project_id: str) -> None:
        """Simulate file processing (for demo purposes).
        
        Args:
            project_id: Project ID
        """
        project = self._projects[project_id]
        
        # Generate some sample segments
        sample_texts = [
            ("Hello, world!", "¡Hola, mundo!"),
            ("This is a test.", "Esta es una prueba."),
            ("Welcome to our service.", "Bienvenido a nuestro servicio."),
            ("Thank you for your interest.", "Gracias por su interés."),
        ]
        
        for source, target in sample_texts:
            segment = Segment(
                id=str(uuid4()),
                source_text=source,
                target_text=target,
                quality_score=QualityScore(
                    overall=random.uniform(75, 95),
                    accuracy=random.uniform(80, 98),
                    fluency=random.uniform(75, 95),
                    terminology=random.uniform(80, 95),
                    style=random.uniform(75, 90),
                ),
            )
            project.segments.append(segment)
        
        # Calculate overall quality
        if project.segments:
            avg_quality = sum(s.quality_score.overall for s in project.segments if s.quality_score) / len(project.segments)
            project.quality_score = QualityScore(
                overall=avg_quality,
                accuracy=sum(s.quality_score.accuracy for s in project.segments if s.quality_score and s.quality_score.accuracy) / len(project.segments),
                fluency=sum(s.quality_score.fluency for s in project.segments if s.quality_score and s.quality_score.fluency) / len(project.segments),
                terminology=sum(s.quality_score.terminology for s in project.segments if s.quality_score and s.quality_score.terminology) / len(project.segments),
                style=sum(s.quality_score.style for s in project.segments if s.quality_score and s.quality_score.style) / len(project.segments),
            )
        
        project.status = ProjectStatus.COMPLETE
        project.completed_at = datetime.now()
        project.updated_at = datetime.now()

    async def get_project(self, project_id: str) -> Project:
        """Get project details.
        
        Args:
            project_id: Project ID
            
        Returns:
            Project details
            
        Raises:
            ValueError: If project not found
        """
        await asyncio.sleep(0.1)  # Simulate API call
        
        if project_id not in self._projects:
            raise ValueError(f"Project {project_id} not found")
        
        return self._projects[project_id]

    async def list_projects(self) -> List[Project]:
        """List all projects.
        
        Returns:
            List of projects
        """
        await asyncio.sleep(0.1)  # Simulate API call
        return list(self._projects.values())

    async def get_project_segments(
        self, project_id: str, file_id: Optional[str] = None
    ) -> List[Segment]:
        """Get segments for a project.
        
        Args:
            project_id: Project ID
            file_id: Optional file ID to filter segments
            
        Returns:
            List of segments
            
        Raises:
            ValueError: If project not found
        """
        await asyncio.sleep(0.1)  # Simulate API call
        
        if project_id not in self._projects:
            raise ValueError(f"Project {project_id} not found")
        
        project = self._projects[project_id]
        return project.segments

    async def request_human_verification(self, project_id: str) -> Project:
        """Request human verification for a project.
        
        Args:
            project_id: Project ID
            
        Returns:
            Updated project
            
        Raises:
            ValueError: If project not found
        """
        await asyncio.sleep(0.2)  # Simulate API call
        
        if project_id not in self._projects:
            raise ValueError(f"Project {project_id} not found")
        
        project = self._projects[project_id]
        project.human_verified = True
        project.updated_at = datetime.now()
        
        # Simulate quality improvement after human verification
        if project.quality_score:
            project.quality_score.overall = min(100, project.quality_score.overall + 5)
        
        return project

    async def download_file(self, file_id: str, output_path: Path) -> None:
        """Download a file.
        
        Args:
            file_id: File ID
            output_path: Path to save the file
        """
        await asyncio.sleep(0.3)  # Simulate download
        
        # For demo, just create a simple text file
        output_path.write_text("Sample translated content")

    async def get_stats(self) -> ProjectStats:
        """Get project statistics.
        
        Returns:
            Project statistics
        """
        await asyncio.sleep(0.1)  # Simulate API call
        
        projects = list(self._projects.values())
        completed = [p for p in projects if p.status == ProjectStatus.COMPLETE]
        
        avg_quality = None
        if completed:
            quality_scores = [p.quality_score.overall for p in completed if p.quality_score]
            if quality_scores:
                avg_quality = sum(quality_scores) / len(quality_scores)
        
        return ProjectStats(
            total_projects=len(projects),
            active_projects=len([p for p in projects if p.status == ProjectStatus.PROCESSING]),
            completed_projects=len(completed),
            failed_projects=len([p for p in projects if p.status == ProjectStatus.FAILED]),
            total_files=sum(len(p.files) for p in projects),
            average_quality=avg_quality,
        )