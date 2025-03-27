![aws bootstrap](output.png 'Output')  

## How the Calculator Code Works:

The calculator program is a simple command-line tool that allows users to perform basic arithmetic operations such as addition, subtraction, multiplication, and division. The program begins by defining four functions—add(), subtract(), multiply(), and divide()—each responsible for carrying out the respective mathematical operation on two input values.

The main functionality is contained within the calculator() function. When this function runs, it first displays a menu to the user, showing the four available operations with corresponding numbers (1 to 4). The user is then prompted to enter their choice of operation by inputting one of these numbers.

If the user enters a valid option (1, 2, 3, or 4), the program asks for two numerical inputs. These values are read using input() and converted to floating-point numbers using float(). If the conversion fails (i.e., the user enters a non-numeric value), the program catches this with a try-except block and notifies the user of invalid input.

Based on the selected operation, the program then calls the appropriate function with the input numbers as arguments and prints the result. For example, if the user selects option 1, the add() function is called with the two numbers, and the result is displayed.

There’s also a safeguard in the divide() function that checks if the second number is zero, which would result in a division error. If detected, it returns a friendly error message instead of crashing the program.

Finally, if the user enters an invalid choice (anything other than 1–4), the program displays an error message and exits gracefully. This keeps the calculator user-friendly and robust against common input mistakes.
