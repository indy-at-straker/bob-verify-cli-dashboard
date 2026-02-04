# Quick Start Guide 🚀

## Running the Straker Verify Dashboard

Follow these simple steps to run the dashboard in your terminal:

### Step 1: Open Terminal

Open your terminal application and navigate to the project directory:

```bash
cd /Users/indy/Development/straker/bob_verify
```

### Step 2: Activate Virtual Environment

```bash
source venv/bin/activate
```

You should see `(venv)` appear at the beginning of your terminal prompt.

### Step 3: Run the Dashboard

```bash
python -m src.main
```

That's it! The dashboard will launch in your terminal.

## Using the Dashboard

Once the dashboard is running, you'll see:

```
┌─────────────────┐┌──────────────────┐┌─────────────────┐┌───────────────────┐
│ 2              ││ 1               ││ 87.5%          ││ 2                │
│ Projects       ││ Active          ││ Avg Quality    ││ Files            │
└─────────────────┘└──────────────────┘└─────────────────┘└───────────────────┘
```

### Keyboard Shortcuts

- **`n`** - Create new project (coming soon)
- **`u`** - Upload file (coming soon)
- **`p`** - View all projects (coming soon)
- **`r`** - Refresh dashboard
- **`s`** - Settings (coming soon)
- **`q`** - Quit application

### To Exit

Press `q` to quit the application.

## Troubleshooting

### "Command not found: python"

Try using `python3` instead:
```bash
python3 -m src.main
```

### "No module named 'textual'"

Make sure you've activated the virtual environment and installed dependencies:
```bash
source venv/bin/activate
pip install -r requirements.txt
```

### "Configuration Error"

Make sure you have a `.env` file with an API key:
```bash
cp .env.example .env
# The demo API key is already set, so this should work!
```

## One-Line Command

If you want to run everything in one command:

```bash
cd /Users/indy/Development/straker/bob_verify && source venv/bin/activate && python -m src.main
```

## What You'll See

The dashboard displays:
- **Stats Panel** at the top showing project statistics
- **Project Cards** below showing individual projects
- **Status Indicators**: 
  - ⟳ Processing (blue)
  - ✓ Complete (green)
  - ⏳ Pending (yellow)
  - ✗ Failed (red)

## Demo Data

The application includes mock data showing:
- 2 sample projects
- 1 active project ("Product_Docs_FR")
- Quality scores and metrics
- Real-time status updates

Enjoy exploring the Straker Verify Dashboard! 🎉