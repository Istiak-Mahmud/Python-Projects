import tkinter as tk

def button_click(value):
    current = entry_var.get()
    entry_var.set(current + value)

def clear():
    entry_var.set("")

def calculate():
    try:
        result = str(eval(entry_var.get()))
        entry_var.set(result)
    except:
        entry_var.set("Error")

# Main window setup
root = tk.Tk()
root.title("Python Calculator")
root.geometry("350x450")
root.resizable(False, False)

# Entry variable and widget
entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 20), bd=5, relief="ridge", justify="right")
entry.pack(padx=10, pady=10, fill="both", ipadx=8, ipady=10)

# Button frame
btn_frame = tk.Frame(root)
btn_frame.pack()

# Button layout
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+']
]

for row in buttons:
    row_frame = tk.Frame(btn_frame)
    row_frame.pack(expand=True, fill="both")
    for btn_text in row:
        if btn_text == '=':
            btn = tk.Button(row_frame, text=btn_text, font=("Arial", 18), command=calculate)
        else:
            btn = tk.Button(row_frame, text=btn_text, font=("Arial", 18), 
                            command=lambda val=btn_text: button_click(val))
        btn.pack(side="left", expand=True, fill="both", padx=3, pady=3)

# Clear button
clear_btn = tk.Button(root, text="Clear", font=("Arial", 18), bg="tomato", fg="white", command=clear)
clear_btn.pack(fill="both", padx=10, pady=10)

# Run the app
root.mainloop()
