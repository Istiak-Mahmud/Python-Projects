import tkinter as tk
from tkinter import messagebox

# Initialize main window
root = tk.Tk()
root.title("Tic Tac Toe")
root.geometry("300x350")
root.resizable(False, False)

# Global variables
current_player = "X"
buttons = [[None for _ in range(3)] for _ in range(3)]

# Label to show turn
turn_label = tk.Label(root, text="Player X's turn", font=('Helvetica', 14))
turn_label.pack(pady=10)

# Function to check for a win or draw
def check_winner():
    # Check rows, columns and diagonals
    for i in range(3):
        if buttons[i][0]['text'] == buttons[i][1]['text'] == buttons[i][2]['text'] != "":
            return buttons[i][0]['text']
        if buttons[0][i]['text'] == buttons[1][i]['text'] == buttons[2][i]['text'] != "":
            return buttons[0][i]['text']
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        return buttons[0][0]['text']
    if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        return buttons[0][2]['text']
    # Check draw
    if all(buttons[i][j]['text'] != "" for i in range(3) for j in range(3)):
        return "Draw"
    return None

# Function to handle button click
def on_click(i, j):
    global current_player
    if buttons[i][j]['text'] == "":
        buttons[i][j]['text'] = current_player
        winner = check_winner()
        if winner:
            if winner == "Draw":
                messagebox.showinfo("Game Over", "It's a draw!")
            else:
                messagebox.showinfo("Game Over", f"Player {winner} wins!")
            reset_board()
        else:
            current_player = "O" if current_player == "X" else "X"
            turn_label.config(text=f"Player {current_player}'s turn")

# Function to reset the game
def reset_board():
    global current_player
    current_player = "X"
    turn_label.config(text="Player X's turn")
    for i in range(3):
        for j in range(3):
            buttons[i][j]['text'] = ""

# Create 3x3 grid of buttons
frame = tk.Frame(root)
frame.pack()
for i in range(3):
    for j in range(3):
        btn = tk.Button(frame, text="", width=5, height=2,
                        font=('Helvetica', 20), command=lambda i=i, j=j: on_click(i, j))
        btn.grid(row=i, column=j, padx=5, pady=5)
        buttons[i][j] = btn

# Restart button
restart_button = tk.Button(root, text="Restart", command=reset_board, font=('Helvetica', 12))
restart_button.pack(pady=10)

# Run the application
root.mainloop()
