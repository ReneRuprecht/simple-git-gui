import tkinter as tk

from ui.repo_panel import RepoPanel


def on_repo_change_callback(path):
    print(f"repo path changed to: {path}")


root = tk.Tk()
root.title("simple git gui")
root.minsize(500, 100)

repo_panel = RepoPanel(root, on_repo_change=on_repo_change_callback)
repo_panel.pack(fill="x", padx=10, pady=10)

root.mainloop()
