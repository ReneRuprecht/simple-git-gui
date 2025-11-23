import tkinter as tk
import os
from tkinter import filedialog, messagebox


class RepoPanel(tk.Frame):
    def __init__(self, root, on_repo_change=None):
        super().__init__(root)

        tk.Label(self, text="Repository:").pack(anchor="w")

        row = tk.Frame(self)
        row.pack(fill="x")

        self.entry = tk.Entry(row)
        self.entry.pack(side="left", fill="x", expand=True)

        tk.Button(row, text="Durchsuchen", command=self.choose_repo).pack(
            side="left"
        )

        self.on_repo_change = on_repo_change

    def choose_repo(self):
        path = filedialog.askdirectory(title="Git-Repository auswählen")
        if not path:
            return
        if not os.path.isdir(os.path.join(path, ".git")):
            messagebox.showerror(
                "Fehler", "Dieser Ordner ist kein Git-Repository!"
            )
            return

        self.entry.delete(0, tk.END)
        self.entry.insert(0, path)

        self._trigger_on_repo_change(path)

    def _trigger_on_repo_change(self, path):
        if self.on_repo_change:
            self.on_repo_change(path)
