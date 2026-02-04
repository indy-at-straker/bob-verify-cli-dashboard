# Navigation Guide 🧭

## How to Navigate the Straker Verify Dashboard

The dashboard is designed to be simple and intuitive. Here's everything you need to know:

## Current Navigation (v1.0)

### Keyboard Shortcuts

The dashboard uses **keyboard shortcuts** for all navigation. Just press a single key:

| Key | Action | Status |
|-----|--------|--------|
| `r` | **Refresh** - Reload dashboard data | ✅ Working |
| `q` | **Quit** - Exit the application | ✅ Working |
| `n` | New Project | 🚧 Coming Soon |
| `u` | Upload File | 🚧 Coming Soon |
| `p` | View Projects | 🚧 Coming Soon |
| `s` | Settings | 🚧 Coming Soon |

### What Works Right Now

1. **View the Dashboard** 👀
   - The dashboard loads automatically when you start the app
   - Shows all projects, stats, and quality scores
   - Updates in real-time

2. **Refresh Data** 🔄
   - Press `r` to refresh the dashboard
   - Reloads project data from the API
   - Updates all statistics and project cards

3. **Exit Application** 🚪
   - Press `q` to quit
   - Clean exit back to terminal

### What Shows "Coming Soon" Notifications

When you press these keys, you'll see a notification at the top:
- `n` - "New Project - Coming soon!"
- `u` - "Upload File - Coming soon!"
- `p` - "View Projects - Coming soon!"
- `s` - "Settings - Coming soon!"

These are placeholders for future features.

## How to Use It

### Basic Workflow

```
1. Run the app:
   python -m src.main

2. View the dashboard:
   - See project stats at the top
   - Browse project cards below
   - Read status indicators

3. Refresh if needed:
   - Press 'r' to reload data

4. Exit when done:
   - Press 'q' to quit
```

### No Mouse Required

The dashboard is **keyboard-only**:
- ❌ No mouse clicking
- ❌ No scrolling (everything fits on screen)
- ❌ No menus to navigate
- ✅ Just simple keyboard shortcuts

### No Arrow Keys Needed

Unlike some TUI apps, you don't need arrow keys:
- The dashboard shows everything at once
- No need to move between items
- No selection or highlighting
- Just view and use keyboard shortcuts

## What You Can Do

### 1. View Project Information
**Just look at the screen!**
- See all projects at once
- Check status indicators (✓ Complete, ⟳ Processing)
- View quality scores with progress bars
- See language pairs (EN → ES, EN → FR)
- Check timestamps ("2 hours ago", "1 min ago")

### 2. Monitor Statistics
**Top panel shows:**
- Total projects
- Active projects
- Average quality score
- Total files processed

### 3. Refresh Data
**Press `r`**
- Reloads all project data
- Updates statistics
- Refreshes timestamps
- Shows latest status

### 4. Exit Application
**Press `q`**
- Closes the dashboard
- Returns to terminal
- Clean exit

## Tips

### 💡 Best Practices

1. **Let it load** - Wait a moment when starting for data to load
2. **Refresh periodically** - Press `r` to see latest updates
3. **Read the footer** - Shows available keyboard shortcuts
4. **Watch status badges** - Colors indicate project state

### 🎨 Understanding Colors

- **Green (✓)** - Complete, successful
- **Blue (⟳)** - Processing, in progress
- **Yellow (⏳)** - Pending, waiting
- **Red (✗)** - Failed, error
- **Cyan** - Borders and structure
- **White/Gray** - Regular text

### 📊 Reading Quality Bars

Quality scores show as progress bars:
```
████████░░ 87.5%
```
- **Filled blocks (█)** - Achieved quality
- **Empty blocks (░)** - Remaining to 100%
- **Percentage** - Exact score

## Future Navigation Features

In future versions, you'll be able to:
- Click on project cards to view details
- Use arrow keys to navigate between projects
- Press Enter to open project details
- Use Tab to move between sections
- Scroll through long project lists

## Troubleshooting

### "Nothing happens when I press a key"
- Make sure the terminal window is focused
- Try pressing the key again
- Check if you're in the right terminal window

### "I can't see the whole dashboard"
- Make your terminal window larger
- Minimum recommended size: 80 columns × 24 rows
- Try maximizing your terminal window

### "How do I go back?"
- There's no "back" - it's a single screen dashboard
- Press `q` to exit completely

## Summary

**Navigation is simple:**
1. **Look** - View all information on one screen
2. **Press `r`** - Refresh data
3. **Press `q`** - Quit

That's it! No complex navigation needed. The dashboard shows everything at once, making it easy to monitor your translation projects at a glance.