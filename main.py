import os
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

repo_path = None


def choose_repo():
    global repo_path
    path = filedialog.askdirectory(title="Git-Repository auswählen")
    if not path:
        return

    if not os.path.isdir(os.path.join(path, ".git")):
        messagebox.showerror(
            "Fehler", "Dieser Ordner ist kein Git-Repository!"
        )
        return

    repo_path = path
    repo_entry.delete(0, tk.END)
    repo_entry.insert(0, repo_path)


root = tk.Tk()
root.title("simple git gui")
root.minsize(500, 100)

repo_frame = tk.Frame(root)
repo_frame.pack(fill="x", pady=10, padx=10)

tk.Label(repo_frame, text="Repository:").pack(anchor="w")

repo_row = tk.Frame(repo_frame)
repo_row.pack(fill="x")

repo_entry = tk.Entry(repo_row, width=30)
repo_entry.pack(side="left", fill="x", expand=True)

tk.Button(repo_row, text="Durchsuchen", command=choose_repo).pack(side="left")

root.mainloop()
