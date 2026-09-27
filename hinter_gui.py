import tkinter as tk
from tkinter import ttk, messagebox
import os

# Define the absolute path to the database
DB_FILE = os.path.expanduser("~/.bash_hints.txt")

def load_hints():
    """Reads the text file and populates the table."""
    # Clear existing data in the table
    for row in tree.get_children():
        tree.delete(row)
        
    # Create file if it doesn't exist
    if not os.path.exists(DB_FILE):
        open(DB_FILE, 'a').close()
        return

    # Read and insert data
    with open(DB_FILE, "r") as f:
        for line in f:
            if "|" in line:
                cmd, syntax, desc = line.strip().split("|", 2)
                tree.insert("", tk.END, values=(cmd, syntax, desc))

def add_hint():
    """Appends a new hint to the text file and updates the table."""
    cmd = cmd_entry.get().strip()
    syntax = syntax_entry.get().strip()
    desc = desc_entry.get().strip()
    
    if not cmd or not syntax or not desc:
        messagebox.showwarning("Input Error", "All fields are required!")
        return
        
    # Append to file
    with open(DB_FILE, "a") as f:
        f.write(f"{cmd}|{syntax}|{desc}\n")
        
    # Clear input boxes and reload table
    cmd_entry.delete(0, tk.END)
    syntax_entry.delete(0, tk.END)
    desc_entry.delete(0, tk.END)
    load_hints()

def delete_hint():
    """Removes the selected hint from the text file and the table."""
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showwarning("Selection Error", "Please select a hint to delete.")
        return
        
    # Get values of the selected row
    values = tree.item(selected_item[0], "values")
    target_line = f"{values[0]}|{values[1]}|{values[2]}\n"
    
    # Read all lines, filter out the target, and rewrite the file
    with open(DB_FILE, "r") as f:
        lines = f.readlines()
        
    with open(DB_FILE, "w") as f:
        for line in lines:
            if line != target_line:
                f.write(line)
                
    load_hints()

# Set up the main application window
root = tk.Tk()
root.title("Bash Syntax Hinter Manager")
root.geometry("800x500")

# --- UI Layout ---

# Input Frame (Top)
input_frame = tk.Frame(root, pady=10)
input_frame.pack(fill=tk.X, padx=20)

tk.Label(input_frame, text="Command:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
cmd_entry = tk.Entry(input_frame, width=20)
cmd_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(input_frame, text="Syntax:").grid(row=0, column=2, padx=5, pady=5, sticky="e")
syntax_entry = tk.Entry(input_frame, width=35)
syntax_entry.grid(row=0, column=3, padx=5, pady=5)

tk.Label(input_frame, text="Description:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
desc_entry = tk.Entry(input_frame, width=64)
desc_entry.grid(row=1, column=1, columnspan=3, padx=5, pady=5, sticky="w")

# Buttons
btn_frame = tk.Frame(root)
btn_frame.pack(fill=tk.X, padx=20, pady=5)
tk.Button(btn_frame, text="Add Hint", command=add_hint, bg="lightblue").pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame, text="Delete Selected", command=delete_hint, bg="lightcoral").pack(side=tk.RIGHT, padx=5)

# Table Frame (Bottom)
table_frame = tk.Frame(root)
table_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

# Treeview (Table)
columns = ("Command", "Syntax", "Description")
tree = ttk.Treeview(table_frame, columns=columns, show="headings")
tree.heading("Command", text="Command")
tree.heading("Syntax", text="Syntax")
tree.heading("Description", text="Description")

tree.column("Command", width=120)
tree.column("Syntax", width=250)
tree.column("Description", width=380)

# Scrollbar for the table
scrollbar = ttk.Scrollbar(table_frame, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Load data on startup
load_hints()

# Run the application
root.mainloop()
