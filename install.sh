#!/bin/bash

USER_LIB_FILE="$HOME/.bash_hint_lib.sh"
USER_DB_FILE="$HOME/.bash_hints.txt"
BASHRC_FILE="$HOME/.bashrc"

echo -e "\e[34mStarting Bash Syntax Hinter installation...\e[0m"

# Install the logic script
cp bash_hint_lib.sh "$USER_LIB_FILE"
echo "✔️  Library installed."

# Install the starter database if one doesn't exist
if [[ ! -f "$USER_DB_FILE" ]]; then
    cp default_hints.txt "$USER_DB_FILE"
    echo "✔️  Created starter database."
else
    echo "⚠️  Existing database found. Skipping overwrite."
fi

# Inject tool into .bashrc if not already present
if ! grep -q "source $USER_LIB_FILE" "$BASHRC_FILE"; then
    echo -e "\n# Load custom bash syntax hinter" >> "$BASHRC_FILE"
    echo "source $USER_LIB_FILE" >> "$BASHRC_FILE"
    echo "✔️  Added tool to .bashrc."
fi

# Inject Alt+G shortcut if not already present
if ! grep -q "bash-syntax-hinter/smart_launch.sh" "$BASHRC_FILE"; then
    echo "bind -x '\"\\eg\": \"$HOME/bash-syntax-hinter/smart_launch.sh\"'" >> "$BASHRC_FILE"
    echo "✔️  Added Alt+G shortcut to .bashrc."
fi
echo "Installing xclip for smart terminal launching..."
sudo apt-get install -y xclip python3-tk

echo "Configuring smart launcher..."
chmod +x "$HOME/bash-syntax-hinter/smart_launch.sh"

KEY_PATH="org.gnome.settings-daemon.plugins.media-keys.custom-keybinding:/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom0/"
gsettings set org.gnome.settings-daemon.plugins.media-keys custom-keybindings "['$KEY_PATH']"
gsettings set $KEY_PATH name 'Bash Hinter Smart Launch'
gsettings set $KEY_PATH command "$HOME/bash-syntax-hinter/smart_launch.sh"
gsettings set $KEY_PATH binding '<Primary><Alt>h'
echo "Smart launch hotkey (Alt + G) configured!"
echo -e "\e[32mInstallation Complete! Restart terminal to activate.\e[0m"

