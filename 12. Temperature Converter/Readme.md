## Output:
![aws bootstrap](test.jpg 'Result')  

## How Code Works:

This Python script defines a temperature converter that allows users to convert values between Celsius, Fahrenheit, and Kelvin. It includes dedicated functions for each possible conversion (e.g., Celsius to Fahrenheit, Fahrenheit to Kelvin, etc.). The main function convert_temperature takes a temperature value along with the source and target units, normalizes the unit names to lowercase, and calls the appropriate conversion function based on the input. If the units are the same, it simply returns the original value. The script also includes an interactive section where the user is prompted to enter a temperature value and choose the units to convert from and to. The result is printed with two decimal places, and error handling is provided for invalid unit combinations.