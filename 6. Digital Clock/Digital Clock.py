import tkinter as tk
from time import strftime

# Function to update time
def update_time():
    current_time = strftime('%H:%M:%S %p')  # Format: Hours:Minutes:Seconds AM/PM
    label.config(text=current_time)
    label.after(1000, update_time)  # Call this function again after 1000ms (1 second)

# Create main window
root = tk.Tk()
root.title("Digital Clock")
root.geometry("400x150")
root.resizable(False, False)
root.configure(bg="black")

# Clock label
label = tk.Label(root, font=('calibri', 50, 'bold'),
                 background='black', foreground='cyan')
label.pack(anchor='center', pady=20)

# Start the clock
update_time()

# Run the application
root.mainloop()
