"""Main entry point for Straker Verify Dashboard."""

import sys
from pathlib import Path

from .app import StrakerVerifyApp
from .config import init_settings


def main() -> int:
    """Run the Straker Verify Dashboard application.
    
    Returns:
        Exit code (0 for success, non-zero for error)
    """
    try:
        # Initialize settings
        settings = init_settings()
        
        # Create and run the application
        app = StrakerVerifyApp(settings)
        app.run()
        
        return 0
        
    except ValueError as e:
        # Configuration error
        print(f"Configuration Error: {e}", file=sys.stderr)
        print("\nPlease ensure you have:", file=sys.stderr)
        print("1. Copied .env.example to .env", file=sys.stderr)
        print("2. Added your Straker Verify API key to .env", file=sys.stderr)
        return 1
        
    except KeyboardInterrupt:
        # User interrupted
        print("\nInterrupted by user", file=sys.stderr)
        return 130
        
    except Exception as e:
        # Unexpected error
        print(f"Unexpected Error: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())