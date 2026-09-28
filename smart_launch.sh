#!/bin/bash
# Grab highlighted text
QUERY=$(xclip -o -selection primary 2>/dev/null)

# Launch GUI with the highlighted text
python3 "$HOME/bash-syntax-hinter/hinter_gui.py" "$QUERY"
