import tkinter as tk
from tkinter import colorchooser

# Initialize main window
root = tk.Tk()
root.title("Paint Application")
root.geometry("800x600")

# Set default brush color and size
brush_color = "black"
brush_size = 5

# Function to draw on the canvas
def paint(event):
    x1, y1 = (event.x - brush_size), (event.y - brush_size)
    x2, y2 = (event.x + brush_size), (event.y + brush_size)
    canvas.create_oval(x1, y1, x2, y2, fill=brush_color, outline=brush_color)

# Function to change brush color
def choose_color():
    global brush_color
    color = colorchooser.askcolor()[1]
    if color:
        brush_color = color

# Function to clear the canvas
def clear_canvas():
    canvas.delete("all")

# Canvas where drawing happens
canvas = tk.Canvas(root, bg="white", width=800, height=500)
canvas.pack()

# Bind mouse drag to paint function
canvas.bind("<B1-Motion>", paint)

# Buttons and tools
frame = tk.Frame(root)
frame.pack(pady=10)

color_btn = tk.Button(frame, text="Choose Color", command=choose_color)
color_btn.grid(row=0, column=0, padx=10)

clear_btn = tk.Button(frame, text="Clear Canvas", command=clear_canvas)
clear_btn.grid(row=0, column=1, padx=10)

# Run the application
root.mainloop()
