import tkinter as tk
from tkinter import ttk, messagebox
import os

DB_FILE = os.path.expanduser("~/.bash_hints.txt")

def load_hints(search_query=""):
    """Reads the text file and populates the table, applying an optional search filter."""
    for row in tree.get_children():
        tree.delete(row)
        
    if not os.path.exists(DB_FILE):
        open(DB_FILE, 'a').close()
        return

    query = search_query.lower()

    with open(DB_FILE, "r") as f:
        for line in f:
            if "|" in line:
                cmd, syntax, desc = line.strip().split("|", 2)
                # If search query is empty OR if it matches any of the fields, insert it
                if not query or query in cmd.lower() or query in syntax.lower() or query in desc.lower():
                    tree.insert("", tk.END, values=(cmd, syntax, desc))

def search_hints(event):
    """Triggers the load_hints function whenever a key is pressed in the search bar."""
    load_hints(search_entry.get())

def add_hint():
    """Appends a new hint to the text file and updates the table."""
    cmd = cmd_entry.get().strip()
    syntax = syntax_entry.get().strip()
    desc = desc_entry.get().strip()
    
    if not cmd or not syntax or not desc:
        messagebox.showwarning("Input Error", "All fields are required!")
        return
        
    with open(DB_FILE, "a") as f:
        f.write(f"{cmd}|{syntax}|{desc}\n")
        
    cmd_entry.delete(0, tk.END)
    syntax_entry.delete(0, tk.END)
    desc_entry.delete(0, tk.END)
    
    # Clear the search bar and reload everything so the new hint is visible
    search_entry.delete(0, tk.END)
    load_hints()

def delete_hint():
    """Removes the selected hint from the text file and the table."""
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showwarning("Selection Error", "Please select a hint to delete.")
        return
        
    values = tree.item(selected_item[0], "values")
    target_line = f"{values[0]}|{values[1]}|{values[2]}\n"
    
    with open(DB_FILE, "r") as f:
        lines = f.readlines()
        
    with open(DB_FILE, "w") as f:
        for line in lines:
            if line != target_line:
                f.write(line)
                
    load_hints(search_entry.get())

# Set up the main application window
root = tk.Tk()
root.title("Bash Syntax Hinter Manager")
root.geometry("800x550")

# --- UI Layout ---

# Search Frame (Top)
search_frame = tk.Frame(root, pady=10)
search_frame.pack(fill=tk.X, padx=20)
tk.Label(search_frame, text="🔍 Search:", font=("Arial", 10, "bold")).pack(side=tk.LEFT)
search_entry = tk.Entry(search_frame)
search_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
# Bind every key release to the search_hints function
search_entry.bind("<KeyRelease>", search_hints)

# Input Frame 
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

columns = ("Command", "Syntax", "Description")
tree = ttk.Treeview(table_frame, columns=columns, show="headings")
tree.heading("Command", text="Command")
tree.heading("Syntax", text="Syntax")
tree.heading("Description", text="Description")

tree.column("Command", width=120)
tree.column("Syntax", width=250)
tree.column("Description", width=380)

scrollbar = ttk.Scrollbar(table_frame, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

load_hints()
root.mainloop()
