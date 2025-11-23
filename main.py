import tkinter as tk

from ui.file_list_panel import FileListPanel
from ui.repo_panel import RepoPanel


def on_repo_change_callback(path):
    file_list_panel.update_file_list(path)


root = tk.Tk()
root.title("simple git gui")
root.minsize(500, 100)

repo_panel = RepoPanel(root, on_repo_change=on_repo_change_callback)
repo_panel.pack(fill="x", padx=10, pady=10)

file_list_panel = FileListPanel(root)
file_list_panel.pack(fill="both", padx=10, pady=10, expand=True)

root.mainloop()
