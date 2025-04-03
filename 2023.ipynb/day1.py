# import the regular expression module to find numbers in the text
import re

# create a function to obtain the calibration values from the lines of text
def obtain_calibration_value (line): 
    digits = re.findall(r'\d', line)  # finds all digits in the line
    return int(digits[0] + digits[-1]) if digits else 0  # combines first and last digit

# create a function to calculate the sum of calibration values from the input file
def sum_calibration_values (filename):
    try:
        with open(filename, 'r') as file:  # open the input file in read mode
            return sum(obtain_calibration_value(line.strip()) for line in file)  
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")  # Print error if file is missing
        return None

# create the main function to input the file name
def main():
    filename = input("Enter the filename: ").strip()  # asks for filename
    result = sum_calibration_values(filename)  # obtains the sum of calibration values
    if result is not None:
        print(f"Sum of calibration values: {result}")  # prints the result

# run the main function
if __name__ == "__main__":
    main()