# Simple Calculator                  # A comment that describes what this program is about

print("Simple Calculator")           # Prints a title for the user

print("Choose an operation:")        # Prints instructions

print("1. Add")                      # Shows option 1: addition
print("2. Subtract")                 # Shows option 2: subtraction
print("3. Multiply")                 # Shows option 3: multiplication
print("4. Divide")                   # Shows option 4: division

choice = input("Enter your choice (1/2/3/4): ")
                                     # Takes the user's choice as a string (text)

num1 = float(input("Enter first number: "))
                                     # Asks the user for the first number and converts it to a float

num2 = float(input("Enter second number: "))
                                     # Asks the user for the second number and converts it to a float


if choice == "1":                    # Checks if the user selected addition
    print("Result:", num1 + num2)    # Adds the two numbers and prints the result

elif choice == "2":                  # Checks if the user selected subtraction
    print("Result:", num1 - num2)    # Subtracts the second number from the first

elif choice == "3":                  # Checks if the user selected multiplication
    print("Result:", num1 * num2)    # Multiplies the two numbers

elif choice == "4":                  # Checks if the user selected division
    if num2 == 0:                    # Checks if the second number is zero
        print("Error: Cannot divide by zero!")
                                     # Prevents division by zero and prints an error message
    else:
        print("Result:", num1 / num2)
                                     # Divides the two numbers and prints the result

else:                                # If the user typed something that isn't 1,2,3,4
    print("Invalid input")           # Prints an error message
