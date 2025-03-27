import tkinter as tk
from tkinter import messagebox
from datetime import datetime, date

# Function to calculate age
def calculate_age():
    try:
        dob = dob_entry.get()
        birth_date = datetime.strptime(dob, "%Y-%m-%d").date()
        today = date.today()

        # Calculate age
        age_years = today.year - birth_date.year
        age_months = today.month - birth_date.month
        age_days = today.day - birth_date.day

        if age_days < 0:
            age_months -= 1
            previous_month = today.month - 1 or 12
            previous_month_year = today.year if today.month != 1 else today.year - 1
            days_in_prev_month = (date(today.year, today.month, 1) - date(previous_month_year, previous_month, 1)).days
            age_days += days_in_prev_month

        if age_months < 0:
            age_years -= 1
            age_months += 12

        result_label.config(text=f"Your Age: {age_years} years, {age_months} months, {age_days} days")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter the date in YYYY-MM-DD format.")

# Create the main window
root = tk.Tk()
root.title("Age Calculator")
root.geometry("350x200")
root.resizable(False, False)

# Title label
title_label = tk.Label(root, text="Age Calculator", font=("Helvetica", 16, "bold"))
title_label.pack(pady=10)

# Input field for date of birth
dob_label = tk.Label(root, text="Enter your Date of Birth (YYYY-MM-DD):", font=("Helvetica", 10))
dob_label.pack()

dob_entry = tk.Entry(root, width=20, font=("Helvetica", 12))
dob_entry.pack(pady=5)

# Calculate button
calculate_button = tk.Button(root, text="Calculate Age", font=("Helvetica", 12), command=calculate_age)
calculate_button.pack(pady=10)

# Result label
result_label = tk.Label(root, text="", font=("Helvetica", 12), fg="blue")
result_label.pack()

# Run the application
root.mainloop()
