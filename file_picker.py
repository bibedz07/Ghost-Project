#Creating a file picker file that will eventually be used on the main code to attach file when sending email
from tkinter import Tk, filedialog

def browse_file():
    # Hide the main Tkinter window
    root = Tk()
    root.withdraw()

    # Open file picker dialog file types will be customize later
    file_path = filedialog.askopenfilename(
        title="Select a File",
        filetypes=[
            ("All Files", "*.*"),
            ("Text Files", "*.txt"),
            ("Word Docs", "*.docx"),
            ("PDF Files", "*.pdf"),
            ("Excel Sheets", "*.xlsx"),
            ("CSV Files", "*.csv"),
            ("Image Files", "*.jpg"),
            ("PNG Images", "*.png"),
            ("GIF Images", "*.gif"),
            ("Audio Files", "*.mp3"),
            ("Video Files", "*.mp4"),
            ("Zip Archives", "*.zip")        ]
    )

    # Print selected file path in terminal
    if file_path:
        print("Selected File:")
        print(file_path)
        return file_path
    else:
        print("No file selected.")
        return None