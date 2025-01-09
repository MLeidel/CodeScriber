import tkinter as tk
from tkinter import colorchooser

def pick_color():
    # Open the color picker dialog and get the selected color
    color_code = colorchooser.askcolor(title="Choose a color")
    print(color_code)

# Create the main window
root = tk.Tk()
root.title("Color Picker Example")

# Add a button to open the color picker
button = tk.Button(root, text="Pick a color", command=pick_color)
button.pack(pady=20)

# Run the application
root.mainloop()
