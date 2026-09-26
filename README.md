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
