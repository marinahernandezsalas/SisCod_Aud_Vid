import tkinter as tk
from tkinter import filedialog
from SP3 import VideoConverter
import threading
import os

# Suppress Tkinter deprecation warning on macOS
os.environ["TK_SILENCE_DEPRECATION"] = "1"

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4")])
    entry_path.delete(0, tk.END)
    entry_path.insert(0, file_path)

def convert_video():
    input_file = entry_path.get()
    conversion_option = var.get().split()[0]  # Extracting the codec from the option

    if not input_file or not conversion_option:
        status_label.config(text="Please fill in all fields.")
        return

    # Function to be executed in a separate thread
    def conversion_thread():
        input_directory, input_filename = os.path.split(input_file)
        custom_name = "converted_video" 
        output_format = "webm" if option=="libvpx (VP8)" in options else "mp4"  # Adjust the format based on the codec
        VideoConverter.convert_resolution_and_codec(input_file, input_directory, 1280, 720, conversion_option, custom_name, output_format)
        root.after(0, lambda: status_label.config(text="Conversion successful!"))  # Update status_label in the main thread

    # Start the conversion in a separate thread
    threading.Thread(target=conversion_thread).start()

# GUI setup
root = tk.Tk()
root.title("Video Converter")

# Input File
tk.Label(root, text="Input Video File:").pack(pady=5)
entry_path = tk.Entry(root, width=40)
entry_path.pack(pady=5)
tk.Button(root, text="Browse the Input Video File", command=browse_file).pack(pady=5)

# Conversion Options
tk.Label(root, text="Conversion Option:").pack(pady=5)
var = tk.StringVar()
var.set("output_resolution")  # Default option
options = ["libvpx (VP8)", "libvpx-vp9 (VP9)", "libx265 (H.265)"]
for option in options:
    tk.Radiobutton(root, text=option, variable=var, value=option).pack()

# Convert Button
tk.Button(root, text="Convert", command=convert_video).pack(pady=10)

# Status Label
status_label = tk.Label(root, text="", fg="green")
status_label.pack()

root.mainloop()
