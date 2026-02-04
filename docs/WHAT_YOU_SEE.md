# What You See When Running the Dashboard 👀

When you run `python -m src.main`, you'll see **ONE screen** - the main dashboard. Here's exactly what appears:

## The Dashboard Screen

```
╔══════════════════════════════════════════════════════════════════════════════╗
║ Straker Verify Dashboard                                                     ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                              ║
║  ┌─────────────────┐┌──────────────────┐┌─────────────────┐┌──────────────┐║
║  │                 ││                  ││                 ││              │║
║  │ 2              ││ 1               ││ 87.5%          ││ 2            │║
║  │ Projects       ││ Active          ││ Avg Quality    ││ Files        │║
║  │                 ││                  ││                 ││              │║
║  └─────────────────┘└──────────────────┘└─────────────────┘└──────────────┘║
║                                                                              ║
║  ┌────────────────────────────────────────────────────────────────────────┐ ║
║  │                                                                        │ ║
║  │ Marketing_Campaign_ES                              ✓ Complete         │ ║
║  │ EN → ES                                            2 hours ago        │ ║
║  │ Quality: ████████░░ 87.5%                                            │ ║
║  │                                                                        │ ║
║  └────────────────────────────────────────────────────────────────────────┘ ║
║                                                                              ║
║  ┌────────────────────────────────────────────────────────────────────────┐ ║
║  │                                                                        │ ║
║  │ Product_Docs_FR                                    ⟳ Processing       │ ║
║  │ EN → FR                                            1 min ago          │ ║
║  │                                                                        │ ║
║  └────────────────────────────────────────────────────────────────────────┘ ║
║                                                                              ║
╠══════════════════════════════════════════════════════════════════════════════╣
║ n New Project | u Upload | p Projects | r Refresh | s Settings | q Quit    ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

## What Each Section Shows

### 1. Header (Top)
- **Title**: "Straker Verify Dashboard"
- **Subtitle**: "Translation Quality Management"

### 2. Stats Panel (4 boxes across the top)
Shows quick statistics:
- **Projects**: Total number of projects (2)
- **Active**: Currently processing projects (1)
- **Avg Quality**: Average quality score across all projects (87.5%)
- **Files**: Total files processed (2)

### 3. Project Cards (Main area)
Each card shows:
- **Project Name**: e.g., "Marketing_Campaign_ES"
- **Status Badge**: 
  - ✓ Complete (green)
  - ⟳ Processing (blue)
  - ⏳ Pending (yellow)
  - ✗ Failed (red)
- **Language Pair**: e.g., "EN → ES"
- **Time**: When last updated (e.g., "2 hours ago")
- **Quality Bar**: Visual progress bar showing quality score (if complete)

### 4. Footer (Bottom)
Shows available keyboard shortcuts:
- `n` - New Project
- `u` - Upload File
- `p` - View Projects
- `r` - Refresh
- `s` - Settings
- `q` - Quit

## What You DON'T See

You do **NOT** see two screens. It's a single, unified dashboard that shows everything at once:
- No separate windows
- No pop-ups
- No multiple terminals
- Just one clean, organized view

## The Demo Data

The dashboard comes pre-loaded with 2 sample projects:

1. **Marketing_Campaign_ES** (Completed)
   - English to Spanish translation
   - Quality score: 87.5%
   - Status: Complete ✓

2. **Product_Docs_FR** (Processing)
   - English to French translation
   - Status: Processing ⟳
   - No quality score yet (still processing)

## Interactive Elements

While viewing the dashboard, you can:
- Press `r` to refresh and see updated data
- Press `q` to exit the application
- Other keys (`n`, `u`, `p`, `s`) show "Coming soon" notifications

## Colors

The dashboard uses colors to make information clear:
- **Green** (✓): Completed successfully
- **Blue** (⟳): Currently processing
- **Yellow** (⏳): Waiting to start
- **Red** (✗): Failed or error
- **Cyan**: Borders and structure
- **White/Gray**: Text and labels

## Summary

**You see ONE screen** - a beautiful, organized dashboard that displays:
- Project statistics at the top
- Individual project cards in the middle
- Keyboard shortcuts at the bottom

Everything updates in real-time, and you can interact with it using keyboard shortcuts!