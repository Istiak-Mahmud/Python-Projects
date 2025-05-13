## Output:
![aws bootstrap](test.jpg 'Result')  

## How Code Works:

This Python script defines a function generate_password that creates a random password of a specified length (default is 12) by combining selected character sets—digits, symbols, uppercase, and lowercase letters—based on the user's input. It uses Python's built-in string module to access these character sets and random.choice to randomly select characters from the combined pool. If no character types are selected, it raises an error to ensure a valid password can be generated. The script ends with an example usage in the __main__ block that prints a randomly generated 16-character password.