_show_hint() {
    local cmd=$(echo "$READLINE_LINE" | awk '{print $1}')
    # Using the absolute path so it works in any directory
    local db_file="$HOME/.bash_hints.txt"
    
    echo ""
    
    if [[ ! -f "$db_file" ]]; then
        echo -e "\e[31m[ERROR] Database not found at $db_file\e[0m"
        return
    fi
    
    local matches=$(grep "^${cmd}|" "$db_file")
    
    if [[ -n "$matches" ]]; then
        echo "$matches" | while IFS='|' read -r db_cmd db_syntax db_desc; do
            echo -e "\e[33mSYNTAX:\e[0m $db_syntax"
            echo -e "         $db_desc"
        done
    else
        echo -e "\e[31mNo hint found for '$cmd'\e[0m"
    fi
}

bind -x '"\eh": _show_hint'
# Function to easily add new hints to the database
add_hint() {
    local db_file="$HOME/.bash_hints.txt"
    
    if [[ "$#" -ne 3 ]]; then
        echo -e "\e[31mUsage: add_hint <command> <syntax> <description>\e[0m"
        echo 'Example: add_hint "ls" "ls -la" "List all files with details"'
        return 1
    fi
    
    echo "$1|$2|$3" >> "$db_file"
    echo -e "\e[32mSuccessfully added hint for '$1'\e[0m"
}
