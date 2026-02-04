"""Data models for Straker Verify API."""

from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


class ProjectStatus(str, Enum):
    """Project status enumeration."""

    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETE = "complete"
    FAILED = "failed"
    CANCELLED = "cancelled"


class QualityDimension(str, Enum):
    """Quality dimension enumeration."""

    ACCURACY = "accuracy"
    FLUENCY = "fluency"
    TERMINOLOGY = "terminology"
    STYLE = "style"


class Language(BaseModel):
    """Language model."""

    id: str = Field(..., description="Language ID (e.g., 'en', 'es')")
    code: str = Field(..., description="Language code")
    name: str = Field(..., description="Language name")


class QualityScore(BaseModel):
    """Quality score model."""

    overall: float = Field(..., ge=0, le=100, description="Overall quality score")
    accuracy: Optional[float] = Field(None, ge=0, le=100, description="Accuracy score")
    fluency: Optional[float] = Field(None, ge=0, le=100, description="Fluency score")
    terminology: Optional[float] = Field(
        None, ge=0, le=100, description="Terminology score"
    )
    style: Optional[float] = Field(None, ge=0, le=100, description="Style score")

    def get_dimension_score(self, dimension: QualityDimension) -> Optional[float]:
        """Get score for a specific quality dimension.
        
        Args:
            dimension: Quality dimension
            
        Returns:
            Score for the dimension, or None if not available
        """
        return getattr(self, dimension.value, None)


class Segment(BaseModel):
    """Translation segment model."""

    id: str = Field(..., description="Segment ID")
    source_text: str = Field(..., description="Source text")
    target_text: str = Field(..., description="Target text")
    quality_score: Optional[QualityScore] = Field(
        None, description="Quality score for this segment"
    )
    issues: List[str] = Field(default_factory=list, description="List of issues")


class FileInfo(BaseModel):
    """File information model."""

    id: str = Field(..., description="File ID")
    name: str = Field(..., description="File name")
    size: int = Field(..., description="File size in bytes")
    mime_type: Optional[str] = Field(default=None, description="MIME type")
    uploaded_at: Optional[datetime] = Field(default=None, description="Upload timestamp")
    download_url: Optional[str] = Field(default=None, description="Download URL")


class Project(BaseModel):
    """Project model."""

    id: str = Field(..., description="Project ID")
    name: str = Field(..., description="Project name")
    description: Optional[str] = Field(None, description="Project description")
    source_language: str = Field(..., description="Source language code")
    target_language: str = Field(..., description="Target language code")
    status: ProjectStatus = Field(..., description="Project status")
    quality_score: Optional[QualityScore] = Field(
        default=None, description="Overall quality score"
    )
    files: List[FileInfo] = Field(default_factory=list, description="Project files")
    segments: List[Segment] = Field(default_factory=list, description="Translation segments")
    created_at: datetime = Field(..., description="Creation timestamp")
    updated_at: datetime = Field(..., description="Last update timestamp")
    completed_at: Optional[datetime] = Field(default=None, description="Completion timestamp")
    human_verified: bool = Field(default=False, description="Human verification status")
    metadata: Dict[str, Any] = Field(
        default_factory=dict, description="Additional metadata"
    )

    @property
    def progress_percentage(self) -> float:
        """Calculate progress percentage based on status.
        
        Returns:
            Progress percentage (0-100)
        """
        if self.status == ProjectStatus.COMPLETE:
            return 100.0
        elif self.status == ProjectStatus.PROCESSING:
            # If we have segments, calculate based on processed segments
            if self.segments:
                processed = sum(1 for s in self.segments if s.quality_score is not None)
                return (processed / len(self.segments)) * 100
            return 50.0  # Default for processing
        elif self.status == ProjectStatus.PENDING:
            return 0.0
        else:
            return 0.0

    @property
    def language_pair(self) -> str:
        """Get formatted language pair string.
        
        Returns:
            Language pair string (e.g., "EN → ES")
        """
        return f"{self.source_language.upper()} → {self.target_language.upper()}"


class ProjectCreate(BaseModel):
    """Project creation request model."""

    name: str = Field(..., description="Project name")
    description: Optional[str] = Field(None, description="Project description")
    source_language: str = Field(..., description="Source language code")
    target_language: str = Field(..., description="Target language code")
    workflow: Optional[str] = Field(
        None, description="Workflow type (e.g., 'quality-evaluation')"
    )


class TokenBalance(BaseModel):
    """Token balance model."""

    balance: int = Field(..., description="Current token balance")
    currency: str = Field(default="tokens", description="Currency unit")


class APIError(BaseModel):
    """API error model."""

    code: str = Field(..., description="Error code")
    message: str = Field(..., description="Error message")
    details: Optional[Dict[str, Any]] = Field(None, description="Additional error details")


class ProjectStats(BaseModel):
    """Project statistics model."""

    total_projects: int = Field(default=0, description="Total number of projects")
    active_projects: int = Field(default=0, description="Number of active projects")
    completed_projects: int = Field(default=0, description="Number of completed projects")
    failed_projects: int = Field(default=0, description="Number of failed projects")
    total_files: int = Field(default=0, description="Total number of files processed")
    average_quality: Optional[float] = Field(
        None, ge=0, le=100, description="Average quality score"
    )