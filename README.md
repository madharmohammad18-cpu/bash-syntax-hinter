# Bash Syntax Hinter

A lightweight, non-intrusive command-line utility that provides instant syntax hints and descriptions for Linux commands directly in the terminal, without interrupting your current workflow.

## Features
* **Non-Disruptive Workflow:** Uses the Bash `readline` API (`bind -x`) to intercept input, allowing you to view syntax hints and return exactly to where you left off.
* **Flat-File Database:** Stores commands in a lightweight, easily modifiable pipe-delimited text file (`~/.bash_hints.txt`).
* **Built-in CLI Management:** Includes the `add_hint` command to securely append new syntax rules directly from the terminal.
* **Automated Setup:** Comes with an `install.sh` script for zero-configuration deployment and `.bashrc` integration.

## Installation

Clone the repository and run the installer:

```bash
git clone https://github.com/madharmohammad18-cpu/bash-syntax-hinter.git
cd bash-syntax-hinter
chmod +x install.sh
./install.sh
```
## How to Update
To get the latest features (like fuzzy search), run these commands:

```bash
cd bash-syntax-hinter
git pull
./install.sh
```
## 🖥️ Desktop GUI Manager

Managing your hints is easy with the included Python graphical interface. You can view, add, and delete command hints visually without editing the raw text file.

### Prerequisites (Ubuntu/Debian)
The GUI uses Tkinter, which may not be installed by default on Linux. Install it using:
```bash
sudo apt update
sudo apt install python3-tk
```
### Running the Manager
To launch the desktop window, run the following command from your terminal:
```bash
python3 ~/bash-syntax-hinter/hinter_gui.py
```
# Bash Syntax Hinter

A lightweight, plug-and-play syntax hinter and cheat sheet for Bash commands. It features a fast graphical interface that bridges the gap between your terminal workflow and desktop environment.

## Features
* **Smart Launch Hotkey:** Highlight any command in your terminal, press `Ctrl + Alt + H`, and a GUI will instantly pop up with the correct syntax and description.
* **Automated Setup:** The installer automatically configures dependencies (`xclip`), permissions, and GNOME system-wide hotkeys.
* **Terminal Friendly:** Works alongside strictly terminal-based editors like `nano` without interrupting your workflow.

## Installation
Clone the repository and run the automated installer. The script will handle all configuration automatically.

```bash
git clone [https://github.com/yourusername/bash-syntax-hinter.git](https://github.com/yourusername/bash-syntax-hinter.git)
cd bash-syntax-hinter
./install.sh
```
