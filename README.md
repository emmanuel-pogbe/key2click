# ⌨️ Key2Click

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Platform: Windows](https://img.shields.io/badge/Platform-Windows-0078d4.svg)](https://www.microsoft.com/windows)

**Assign keyboard shortcuts to screen points for instant clicking**

Key2Click is a lightweight, open-source Windows utility that allows you to create keyboard shortcuts that automatically click on specific screen coordinates. Perfect for automating repetitive clicking tasks, or streamlining your workflow.

## 🎯 Features

- **Point Selection**: Click anywhere on your screen to set a target point for automation
- **Custom Shortcuts**: Assign any keyboard combination to trigger clicks at your saved points (e.g., `Ctrl+F`, `Alt+P`, `Alt+Shift+1`, `Ctrl+Alt+3`)
- **Save & Load**: Export your shortcuts as JSON files to backup or share with others
- **Instant Clicking**: Press your hotkey and watch the cursor automatically click your point
- **Easy Management**: Edit, delete, or update your shortcuts anytime with a simple interface
- **Autosave**: Shortcuts are saved automatically to your AppData folder even when the app is closed

## 📋 Requirements

- **Python 3.8+** (if running from source)
- **Windows 7** or later

## 🚀 Installation

### Option 1: Download Executable (Recommended)

1. Download the latest release from [GitHub Releases](https://github.com/emmanuel-pogbe/key2click/releases)
2. Run `Key2Click_Setup.exe` and follow the prompts

### Option 2: Run from Source

1. **Clone the repository**
   ```bash
   git clone https://github.com/emmanuel-pogbe/key2click.git
   cd key2click
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python main.py
   ```

## 📖 How to Use

### Basic Workflow

1. **Select a Point**
   - Click the "Select point" button
   - Your screen will turn semi-transparent
   - Click at the location where you want shortcuts to trigger clicks
   - The coordinates will be displayed

2. **Create a Shortcut**
   - In the "Enter shortcut" field, type your desired keyboard combination
   - Examples:
     - Single key: `z`, `9`
     - Modifier + key: `ctrl+f`, `alt+p`
     - Multiple modifiers: `ctrl+alt+3`, `shift+alt+d`
   - Click "Add" to save the shortcut

3. **Manage Shortcuts**
   - View all loaded shortcuts in the "Loaded shortcuts" list
   - **Edit Point**: Select a shortcut and click "Edit Point" to change the target coordinates
   - **Delete**: Select shortcuts and click "Delete selected" to remove them
   - **Export**: Click "Export shortcuts" to save your configuration as a JSON file on your computer
   - **Open saved**: Load previously saved shortcuts from a JSON file

4. **Start Automation**
   - Click the "START" button to activate shortcut listening 
   - Press any of your configured shortcuts to trigger automatic clicks
   - Click "STOP" to disable shortcut listening

### Shortcut Format

Shortcuts are case-insensitive and use the following format:

```
<modifier>+<modifier>+<key>
```

**Valid modifiers:**
- `ctrl`
- `alt`
- `shift`

**Valid keys:**
- Single characters: `a`, `z`, `1`, `9`
- Special keys: `space`, `tab`, `enter`, `esc`, `backspace`
- Function keys: `f1`, `f2`, etc.

## 💾 Shortcut Configuration Format

Shortcuts are stored as JSON files. Example:

```json
{
  "ctrl+f": [1920, 1080],
  "alt+p": [512, 256],
  "shift+1": [100, 200],
  "ctrl+alt+3": [1024, 768]
}
```

- **Keys**: Keyboard shortcut (case-insensitive)
- **Values**: Array with `[x, y]` coordinates

### Auto-save Location

Shortcuts are automatically saved to:
```
%APPDATA%\Key2Click\shortcuts.json
```

On Windows, this typically resolves to:
```
C:\Users\<YourUsername>\AppData\Roaming\Key2Click\shortcuts.json
```

## 🛠️ Building from Source

### Prerequisites

- Python 3.8+
- PyInstaller: `pip install pyinstaller`
- (Optional) Inno Setup for creating the installer

## ⚙️ Architecture

### Core Components

- **GUI Framework**: tkinter (built-in with Python)
- **Keyboard Input**: pynput.keyboard (GlobalHotKeys, HotKey parsing)
- **Mouse Control**: PyAutoGUI (Methods for moving cursor and clicking)
- **File Management**: pathlib, json (for shortcut persistence)
- **Instance Management**: File-based lock mechanism to prevent multiple instances

## 🐛 Troubleshooting

### "Key2Click is already open" message

- Check your taskbar for another Key2Click window
- The lock file is stored in: `%TEMP%\Key2Click.lock`, 
- You can find lockfile on windows:
```
C:\Users\<YourUserName>\AppData\Local\Temp\Key2Click.lock
```
- Delete this file manually if needed 

### Shortcuts not triggering

- Ensure the "START" button shows as active (red "STOP" button)
- Check that your shortcut format is valid (use the help dialog for examples)
- Ensure coordinates are within your screen bounds
- Some applications may intercept keyboard shortcuts so clashes might occur

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

You are free to:
- Use this software for personal or commercial purposes
- Modify and distribute it
- Use it in your own projects

The only requirement is attribution.

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/AmazingFeature`)
3. **Commit** your changes (`git commit -m 'Add AmazingFeature'`)
4. **Push** to the branch (`git push origin feature/AmazingFeature`)
5. **Open** a Pull Request

### Areas for Contribution

- Bug fixes and performance improvements
- Additional keyboard modifier support
- Multi-click sequences
- Delay between clicks
- Custom mouse button support (right-click, middle-click)
- Cross-platform support (macOS, Linux)

## 🔗 Links

- **GitHub Repository**: [emmanuel-pogbe/key2click](https://github.com/emmanuel-pogbe/key2click)
- **Releases**: [Download Latest Version](https://github.com/emmanuel-pogbe/key2click/releases)
- **License**: [MIT License](LICENSE)

## 👨‍💻 Author

**Emmanuel Pogbe**

- LinkedIn: [linkedin.com/in/emmanuel-pogbe](https://www.linkedin.com/in/emmanuel-pogbe/)
- GitHub: [@emmanuel-pogbe](https://github.com/emmanuel-pogbe)

## ⚠️ Disclaimer

This software is provided "as-is" without warranty. The developer is not responsible for:

- Any damage or unintended actions caused by automated clicking
- Loss of data or system instability
- Violations of any game's or application's terms of service

## 📞 Support

If you encounter issues or have suggestions:

1. Check the [Troubleshooting](#-troubleshooting) section above
2. Create an issue with:
   - Your Windows version
   - Python version (if running from source)
   - Steps to reproduce the problem
   - Error messages or screenshots

---
