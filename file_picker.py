from tkinter import Tk, filedialog

def browse_file():
    # Hide the main Tkinter window
    root = Tk()
    root.withdraw()

    # Open file picker dialog
    file_path = filedialog.askopenfilename(
        title="Select a File",
        filetypes=[
            ("All Files", "*.*"),
            ("Text Files", "*.txt"),
            ("Python Files", "*.py"),
            ("JSON Files", "*.json"),
            ("HTML Files", "*.html")
        ]
    )

    # Print selected file path in terminal
    if file_path:
        print("Selected File:")
        print(file_path)
    else:
        print("No file selected.")

# Run function
if __name__ == "__main__":
    browse_file()