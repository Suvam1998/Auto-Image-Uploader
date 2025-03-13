import tkinter as tk
from tkinter import filedialog, messagebox
import shutil
import os

# Function to detect the Jupyter Notebook's working directory
def detect_jupyter_directory():
    try:
        # Get the current working directory (typically where Jupyter was launched)
        return os.getcwd()
    except Exception as e:
        messagebox.showerror("Error", f"Could not detect the Jupyter Notebook directory: {str(e)}")
        return None

# Function to upload files
def upload_files():
    # Detect the Jupyter Notebook's working directory
    jupyter_directory = detect_jupyter_directory()
    if not jupyter_directory:
        return

    # Confirm the target directory with the user
    confirm = messagebox.askyesno(
        "Confirm Target Directory",
        f"Files will be uploaded to the Jupyter Notebook directory:\n\n{jupyter_directory}\n\nDo you want to proceed?"
    )
    if not confirm:
        return

    # Allow the user to select multiple files
    files = filedialog.askopenfilenames(title="Select Files to Upload")
    if not files:
        messagebox.showinfo("No Files Selected", "No files were selected for upload.")
        return

    try:
        # Copy each selected file to the Jupyter directory
        for file in files:
            shutil.copy(file, jupyter_directory)
        messagebox.showinfo("Upload Successful", f"{len(files)} file(s) uploaded successfully to:\n{jupyter_directory}.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred during upload: {str(e)}")

# Create the GUI
def create_gui():
    root = tk.Tk()
    root.title("Auto File Uploader for Jupyter Notebook")
    root.geometry("400x250")

    # Create a label
    label = tk.Label(root, text="Upload Files to Jupyter Notebook", font=("Arial", 14))
    label.pack(pady=20)

    # Create an upload button
    upload_button = tk.Button(root, text="Select and Upload Files", command=upload_files, font=("Arial", 12))
    upload_button.pack(pady=10)

    # Run the GUI event loop
    root.mainloop()

# Run the application
if __name__ == "__main__":
    create_gui()
