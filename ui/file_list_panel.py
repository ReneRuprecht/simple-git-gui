import tkinter as tk
import os


class FileListPanel(tk.Frame):
    def __init__(self, root):
        super().__init__(root)

        tk.Label(self, text="Dateien im Ordner:").pack(anchor="w")

        self.listbox = tk.Listbox(self, height=15)
        scrollbar = tk.Scrollbar(
            self, orient="vertical", command=self.listbox.yview
        )
        self.listbox.configure(yscrollcommand=scrollbar.set)

        self.listbox.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    def update_file_list(self, folder_path):
        self.listbox.delete(0, tk.END)

        if not folder_path or not os.path.isdir(folder_path):
            self.listbox.insert(tk.END, "Ungültiger Ordner")
            return

        files = os.listdir(folder_path)

        if not files:
            self.listbox.insert(tk.END, "Der Ordner ist leer")
            return

        for file in sorted(files):
            self.listbox.insert(tk.END, file)
