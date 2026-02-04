#!/bin/bash

# Straker Verify Dashboard Startup Script
# This script activates the virtual environment and runs the dashboard

set -e  # Exit on error

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${BLUE}╔══════════════════════════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║         Straker Verify Dashboard - Starting...              ║${NC}"
echo -e "${BLUE}╚══════════════════════════════════════════════════════════════╝${NC}"
echo ""

# Get the directory where the script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo -e "${RED}Error: Virtual environment not found!${NC}"
    echo "Please run: python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt"
    exit 1
fi

# Check if .env file exists
if [ ! -f ".env" ]; then
    echo -e "${RED}Warning: .env file not found!${NC}"
    echo "Creating .env from .env.example..."
    cp .env.example .env
    echo -e "${GREEN}✓ Created .env file${NC}"
    echo "You can edit .env to add your Straker Verify API key"
    echo ""
fi

# Activate virtual environment
echo -e "${GREEN}✓ Activating virtual environment...${NC}"
source venv/bin/activate

# Check if dependencies are installed
if ! python -c "import textual" 2>/dev/null; then
    echo -e "${RED}Error: Dependencies not installed!${NC}"
    echo "Installing dependencies..."
    pip install -r requirements.txt
fi

echo -e "${GREEN}✓ Dependencies ready${NC}"
echo ""
echo -e "${BLUE}Starting Straker Verify Dashboard...${NC}"
echo -e "${BLUE}Press 'q' to quit${NC}"
echo ""

# Run the application
python -m src.main

# Deactivate virtual environment on exit
deactivate

echo ""
echo -e "${GREEN}Dashboard closed. Goodbye!${NC}"