import tkinter as tk
from GameEngine import *
from tkinter import ttk
from PIL import Image, ImageTk
import ctypes

try:
    ctypes.windll.shcore.SetProcessDpiAwareness(1)  # DPI aware
except:
    pass


## Create main window
root = tk.Tk() # Top level GUI frame
root.title('Risk')
root.geometry('2280x2250')

image = Image.open('database/art/game_board.jpg')
img = ImageTk.PhotoImage(image)
name = input("Name?" )
image_label = tk.Label(root, image=img)
image_label.pack(pady=10, padx=10)
text_label = tk.Label(
    root,
    text=name,
    font=("Arial", 14)  # Font family and size
)
text_label.pack()

command_label = tk.Label(
    root,
    text="Enter a command:",
    font=("Arial", 14)
)
command_label.pack()

command_entry = tk.Entry(
    root,
    font=("Arial", 12)
)
command_entry.pack(pady=5)
root.mainloop()