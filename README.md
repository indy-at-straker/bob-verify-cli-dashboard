# Straker Verify Dashboard 🚀

An Interactive Translation Quality Dashboard built as a modern Terminal User Interface (TUI) that showcases the Straker Verify API's capabilities for translation quality evaluation, human verification, and project management.

![Python](https://img.shields.io/badge/python-3.9+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-demo-orange.svg)

## ✨ Features

- **📊 Live Dashboard** - Real-time project overview with statistics and status indicators
- **📁 Project Management** - Create, track, and manage translation projects
- **🎯 Quality Metrics** - Visualize translation quality scores with terminal-based charts
- **🔍 Segment Review** - Detailed segment-by-segment translation analysis
- **👤 Human Verification** - Request and track human review workflow
- **⚡ Real-time Updates** - Live progress tracking with smooth animations
- **🎨 Beautiful UI** - Modern, color-coded interface with intuitive navigation

## 🖼️ Screenshots

### Dashboard View
```
┌─────────────────┐┌──────────────────┐┌─────────────────┐┌───────────────────┐
│                 ││                  ││                 ││                   │
│ 2              ││ 1               ││ 87.5%          ││ 2                │
│ Projects       ││ Active  ││ Avg Quality    ││ Files   │
│                 ││                  ││                 ││                   │
└─────────────────┘└──────────────────┘└─────────────────┘└───────────────────┘

┌──────────────────────────────────────────────────────────────────────────┐
│                                                                          │
│ Product_Docs_FR        ⟳ Processing                                     │
│ EN → FR                1 min ago                                         │
│                                                                          │
└──────────────────────────────────────────────────────────────────────────┘
```

## 🚀 Quick Start

### Prerequisites

- Python 3.9 or higher
- pip (Python package manager)
- A Straker Verify API key (optional - works with demo data)

### Super Quick Start (Recommended)

Just run the startup script:

```bash
./run.sh
```

That's it! The script will:
- ✅ Check and activate the virtual environment
- ✅ Install dependencies if needed
- ✅ Create .env file if missing
- ✅ Launch the dashboard

### Manual Installation

If you prefer to set up manually:

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd bob_verify
   ```

2. **Create a virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure your API key** (optional)
   ```bash
   cp .env.example .env
   # Edit .env and add your Straker Verify API key
   ```

5. **Run the dashboard**
   ```bash
   python -m src.main
   ```

## 🎮 Usage

### Keyboard Shortcuts

- `n` - Create new project
- `u` - Upload file
- `p` - View all projects
- `r` - Refresh dashboard
- `s` - Settings
- `q` - Quit application

### Navigation

- Use arrow keys to navigate between elements
- Press `Enter` to select/activate
- Press `Esc` to go back

## 📁 Project Structure

```
bob_verify/
├── src/                     # Application source code
│   ├── main.py              # Entry point
│   ├── app.py               # Main Textual application
│   ├── config.py            # Configuration management
│   ├── api/                 # API client and models
│   ├── screens/             # UI screens
│   ├── widgets/             # Custom widgets
│   └── utils/               # Utility functions
├── docs/                    # Documentation
│   ├── README.md            # Documentation index
│   ├── QUICKSTART.md        # Quick start guide
│   ├── WHAT_YOU_SEE.md      # Visual interface guide
│   ├── NAVIGATION_GUIDE.md  # Navigation instructions
│   ├── PLAN.md              # Technical architecture
│   ├── PROJECT_SUMMARY.md   # Project overview
│   └── REAL_API_INTEGRATION.md  # API integration guide
├── examples/                # Example files
├── tests/                   # Test files
├── run.sh                   # Startup script (just run this!)
├── requirements.txt         # Python dependencies
├── .env.example             # Example environment variables
└── README.md                # This file
```

## 🔧 Configuration

The application is configured via environment variables in the `.env` file:

```bash
# Required: Your Straker Verify API key
STRAKER_VERIFY_API_KEY=your_api_key_here

# Optional: API base URL (default: https://api-verify.straker.ai)
STRAKER_VERIFY_BASE_URL=https://api-verify.straker.ai

# Optional: Default language settings
DEFAULT_SOURCE_LANGUAGE=en
DEFAULT_TARGET_LANGUAGE=es

# Optional: UI preferences
THEME=dark
AUTO_REFRESH_INTERVAL=5
LOG_LEVEL=INFO
```

## 🎯 Demo Mode

This application includes a **mock API client** for demonstration purposes. The mock client:

- Simulates API responses with realistic data
- Includes sample projects with quality scores
- Demonstrates all dashboard features without requiring a real API key

To use demo mode, simply use any placeholder API key in your `.env` file.

## 🛠️ Development

### Running Tests

```bash
pytest tests/
```

### Code Formatting

```bash
black src/
ruff check src/
```

### Type Checking

```bash
mypy src/
```

## 📊 Features in Detail

### Dashboard

The main dashboard provides:
- **Quick Stats**: Total projects, active jobs, average quality, files processed
- **Project Cards**: Visual cards showing project status, language pairs, and quality scores
- **Real-time Updates**: Automatic refresh of project status and metrics

### Quality Metrics

Quality scores are displayed across multiple dimensions:
- **Overall Score**: Aggregate quality rating (0-100%)
- **Accuracy**: Translation accuracy score
- **Fluency**: Language fluency score
- **Terminology**: Terminology consistency score
- **Style**: Style appropriateness score

### Project Workflow

1. **Create Project**: Define source/target languages and workflow
2. **Upload Files**: Add files for translation quality evaluation
3. **Processing**: Automatic AI-powered quality analysis
4. **Review Results**: View detailed quality metrics and segment analysis
5. **Human Verification** (optional): Request human review for low-quality segments
6. **Download**: Get translated files with quality reports

## 🔮 Roadmap

- [ ] File upload interface with drag-and-drop
- [ ] Project creation wizard
- [ ] Detailed segment-level review screen
- [ ] Quality charts and visualizations
- [ ] Human verification workflow
- [ ] Export quality reports (PDF, CSV)
- [ ] Batch processing support
- [ ] Webhook notifications
- [ ] Multi-user support

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Built with [Textual](https://textual.textualize.io/) - Modern TUI framework
- Styled with [Rich](https://rich.readthedocs.io/) - Beautiful terminal formatting
- Powered by [Straker Verify API](https://api-verify.straker.ai/) - Translation quality evaluation

## 📧 Support

For questions or issues:
- Open an issue on GitHub
- Check the [documentation](./PLAN.md)
- Visit [Straker Verify Help](https://help.straker.ai/en/docs/straker-verify)

## 📚 Documentation

Comprehensive documentation is available in the `docs/` directory:

- **[Documentation Index](docs/README.md)** - Start here for all documentation
- **[Quick Start Guide](docs/QUICKSTART.md)** - Get up and running quickly
- **[What You See](docs/WHAT_YOU_SEE.md)** - Visual guide to the interface
- **[Navigation Guide](docs/NAVIGATION_GUIDE.md)** - How to use the dashboard
- **[Technical Plan](docs/PLAN.md)** - Architecture and implementation details
- **[Project Summary](docs/PROJECT_SUMMARY.md)** - High-level overview
- **[Real API Integration](docs/REAL_API_INTEGRATION.md)** - Connect to real Straker Verify API

## 🎓 Learn More

- [Straker Verify API Documentation](https://api-verify.straker.ai/docs)
- [Straker Verify Help Center](https://help.straker.ai/en/docs/straker-verify)
- [Textual Documentation](https://textual.textualize.io/)
- [Rich Documentation](https://rich.readthedocs.io/)

---

**Made with ❤️ for the Straker Verify community**