"""Utility functions for formatting data for display."""

from datetime import datetime
from typing import Optional

from rich.text import Text


def format_file_size(size_bytes: int) -> str:
    """Format file size in human-readable format.
    
    Args:
        size_bytes: File size in bytes
        
    Returns:
        Formatted file size string
    """
    size = float(size_bytes)
    for unit in ["B", "KB", "MB", "GB"]:
        if size < 1024.0:
            return f"{size:.1f} {unit}"
        size /= 1024.0
    return f"{size:.1f} TB"


def format_percentage(value: float, decimals: int = 1) -> str:
    """Format a percentage value.
    
    Args:
        value: Percentage value (0-100)
        decimals: Number of decimal places
        
    Returns:
        Formatted percentage string
    """
    return f"{value:.{decimals}f}%"


def format_quality_score(score: Optional[float]) -> str:
    """Format a quality score with color coding.
    
    Args:
        score: Quality score (0-100) or None
        
    Returns:
        Formatted quality score string
    """
    if score is None:
        return "N/A"
    return format_percentage(score)


def get_quality_color(score: Optional[float]) -> str:
    """Get color for quality score.
    
    Args:
        score: Quality score (0-100) or None
        
    Returns:
        Color name for Rich styling
    """
    if score is None:
        return "dim"
    if score >= 90:
        return "green"
    elif score >= 80:
        return "yellow"
    elif score >= 70:
        return "orange"
    else:
        return "red"


def format_quality_bar(score: Optional[float], width: int = 10) -> str:
    """Create a text-based progress bar for quality score.
    
    Args:
        score: Quality score (0-100) or None
        width: Width of the bar in characters
        
    Returns:
        Progress bar string
    """
    if score is None:
        return "░" * width
    
    filled = int((score / 100) * width)
    empty = width - filled
    return "█" * filled + "░" * empty


def format_datetime(dt: Optional[datetime], format_str: str = "%Y-%m-%d %H:%M") -> str:
    """Format a datetime object.
    
    Args:
        dt: Datetime object or None
        format_str: Format string
        
    Returns:
        Formatted datetime string
    """
    if dt is None:
        return "N/A"
    return dt.strftime(format_str)


def format_time_ago(dt: datetime) -> str:
    """Format datetime as relative time (e.g., '2 hours ago').
    
    Args:
        dt: Datetime object
        
    Returns:
        Relative time string
    """
    now = datetime.now()
    diff = now - dt
    
    seconds = diff.total_seconds()
    
    if seconds < 60:
        return "just now"
    elif seconds < 3600:
        minutes = int(seconds / 60)
        return f"{minutes} min{'s' if minutes != 1 else ''} ago"
    elif seconds < 86400:
        hours = int(seconds / 3600)
        return f"{hours} hour{'s' if hours != 1 else ''} ago"
    elif seconds < 604800:
        days = int(seconds / 86400)
        return f"{days} day{'s' if days != 1 else ''} ago"
    else:
        weeks = int(seconds / 604800)
        return f"{weeks} week{'s' if weeks != 1 else ''} ago"


def format_language_pair(source: str, target: str) -> str:
    """Format language pair.
    
    Args:
        source: Source language code
        target: Target language code
        
    Returns:
        Formatted language pair string
    """
    return f"{source.upper()} → {target.upper()}"


def truncate_text(text: str, max_length: int = 50, suffix: str = "...") -> str:
    """Truncate text to maximum length.
    
    Args:
        text: Text to truncate
        max_length: Maximum length
        suffix: Suffix to add if truncated
        
    Returns:
        Truncated text
    """
    if len(text) <= max_length:
        return text
    return text[: max_length - len(suffix)] + suffix


def format_status_badge(status: str) -> Text:
    """Format status as a colored badge.
    
    Args:
        status: Status string
        
    Returns:
        Rich Text object with colored status
    """
    status_colors = {
        "pending": "yellow",
        "processing": "blue",
        "complete": "green",
        "failed": "red",
        "cancelled": "dim",
    }
    
    status_lower = status.lower()
    color = status_colors.get(status_lower, "white")
    
    # Add emoji indicators
    status_emoji = {
        "pending": "⏳",
        "processing": "⟳",
        "complete": "✓",
        "failed": "✗",
        "cancelled": "⊘",
    }
    
    emoji = status_emoji.get(status_lower, "•")
    return Text(f"{emoji} {status.title()}", style=color)


def format_number(num: int) -> str:
    """Format number with thousand separators.
    
    Args:
        num: Number to format
        
    Returns:
        Formatted number string
    """
    return f"{num:,}"