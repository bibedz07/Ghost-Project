#Creating a file picker file that will eventually be used on the main code to attach file when sending email

import tkinter as tk
from tkinter import filedialog, scrolledtext
from pathlib import Path

class FilePreviewApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cross-Platform File Picker with Preview")
        self.root.geometry("800x600")

        # Top Frame
        top_frame = tk.Frame(root)
        top_frame.pack(fill="x", padx=10, pady=10)

        # Open Button
        open_button = tk.Button(
            top_frame,
            text="Open File",
            command=self.open_file,
            font=("Arial", 12)
        )
        open_button.pack(side="left")

        # File Path Label
        self.path_label = tk.Label(
            top_frame,
            text="No file selected",
            anchor="w"
        )
        self.path_label.pack(side="left", padx=10)

        # Preview Area
        self.preview = scrolledtext.ScrolledText(
            root,
            wrap=tk.WORD,
            font=("Consolas", 11)
        )
        self.preview.pack(fill="both", expand=True, padx=10, pady=10)

    def open_file(self):
        file_path = filedialog.askopenfilename(
            title="Select a File",
            filetypes=[
                ("Text Files", "*.txt"),
                ("Python Files", "*.py"),
                ("JSON Files", "*.json"),
                ("HTML Files", "*.html"),
                ("All Files", "*.*")
            ]
        )

        if file_path:
            self.path_label.config(text=file_path)

            try:
                path = Path(file_path)

                with open(path, "r", encoding="utf-8") as file:
                    content = file.read()

                # Clear previous content
                self.preview.delete("1.0", tk.END)

                # Insert new content
                self.preview.insert(tk.END, content)

            except Exception as e:
                self.preview.delete("1.0", tk.END)
                self.preview.insert(tk.END, f"Error reading file:\n\n{e}")

# Run App
if __name__ == "__main__":
    root = tk.Tk()
    app = FilePreviewApp(root)
    root.mainloop()