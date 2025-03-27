![aws bootstrap](output.png 'Output')  

## How the Calculator App's Code Work:

This Python calculator uses the Tkinter library to create a graphical user interface (GUI). The GUI includes an entry field to show the current expression or result and a grid of buttons for digits, operators, and actions like "Clear" and "=". The layout is managed using frames and pack() with some responsive behavior to keep it tidy.

At the heart of the app is a StringVar() called entry_var, which holds the text inside the entry box. When a number or operator button is clicked, the button_click() function adds the clicked value to the current string in the entry. This allows the user to build up a mathematical expression step by step, like 3+5*2.

When the equals (=) button is clicked, the calculate() function is triggered. It uses Python’s built-in eval() function to compute the result of the expression entered by the user. If the expression is invalid (like typing 5//), it gracefully handles the error and displays “Error” instead of crashing.

The Clear button simply resets the entry field by calling the clear() function, which sets the entry string to an empty value.

Buttons are organized in a list of lists (for rows and columns) and placed inside a Frame to structure them nicely. Each button is given a command using lambda, so it knows what to do when clicked. Finally, the GUI is launched with root.mainloop(), which starts the Tkinter event loop and keeps the app running.