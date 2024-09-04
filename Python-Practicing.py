# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Try programiz.pro")
# Global variable
global_var = "I am a global variable"

def basic_function():
    # Local variable
    local_var = "I am a local variable"
    print(local_var)

# Variables and Operators
a = 10
b = 20
sum = a + b
product = a * b

print("Sum:", sum)
print("Product:", product)

# If-Else Condition
if sum > product:
    print("Sum is greater than product")
else:
    print("Product is greater than or equal to sum")

# Array (List in Python)
numbers = [1, 2, 3, 4, 5]

# Loop
for number in numbers:
    print("Number:", number)

# Function call
basic_function()

# Accessing global variable
print(global_var)







# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    return x / y

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:
    # Take input from the user
    choice = input("Enter choice (1/2/3/4): ")

    # Check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
clear

        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")

        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")

        elif choice == '4':
            print(f"{num1} / {num2} = {divide(num1, num2)}")

        # Check if user wants another calculation
        next_calculation = input("Let's do another calculation? (yes/no): ")
        if next_calculation.lower() != 'yes':
            break
    else:
        print("Invalid Input")
