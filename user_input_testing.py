# Function to add two numbers
def add_nums(num1, num2):
    return num1 + num2

# Function to multiply two numbers
def multiply_nums(num1, num2):
    return num1 * num2

# Function to divide two numbers
def divide_nums(num1, num2):
    if num2 == 0:
        return "Error: Division by zero is not allowed."
    return num1 / num2

# Function to find the average of two numbers
def ave_nums(num1, num2):
    return (num1 + num2) / 2

# Function to get valid numeric input from the user
def get_valid_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

# Function to get valid operation choice
def get_valid_operation():
    while True:
        print("\nSelect operation:")
        print("1. Sum")
        print("2. Multiply")
        print("3. Divide")
        print("4. Average")
        
        operation_selected = input("Enter choice (1/2/3/4): ")
        if operation_selected in {'1', '2', '3', '4'}:
            return operation_selected
        else:
            print("Invalid choice. Please select a valid operation.")

# Main function
if __name__ == "__main__":
    while True:
        # Prompt until we get valid inputs
        num1 = get_valid_input("Enter the first number: ")
        num2 = get_valid_input("Enter the second number: ")

        # Get a valid operation choice
        operation_selected = get_valid_operation()

        # Dictionary to map operations
        operations = {
            '1': add_nums,
            '2': multiply_nums,
            '3': divide_nums,
            '4': ave_nums,
        }

        # Perform the selected operation
        result = operations[operation_selected](num1, num2)
        print(f"\nThe result is: {result}")

        # Ask if the user wants to perform another calculation
        another_calculation = input("\nDo you want to perform another calculation? (yes/no): ").strip().lower()
        if another_calculation != 'yes':
            break
