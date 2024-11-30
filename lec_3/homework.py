"""
Calculator Program
This program supports basic mathematical operations: addition, subtraction, multiplication, and division.

Homework Solution - Lecture 3
"""
print("Hi, I'm a basic math calculator!")

def addition(arg1, arg2):
    return arg1 + arg2

def subtraction(arg1, arg2):
    return arg1 - arg2

def multiplication(arg1, arg2):
    return arg1 * arg2

def division(arg1, arg2):
    if arg2 == 0:  
        return "Error: Division by zero is not allowed."
    return arg1 / arg2

while True:
    print("\nChoose an operation:")
    print("1: Addition")
    print("2: Subtraction")
    print("3: Multiplication")
    print("4: Division")
    print("5: Exit :)")
    
    try:
        choice = int(input("Enter your choice: ")) 
        
        if choice == 5:
            print("Bye <3")
            break
        
        if choice in [1, 2, 3, 4]:
            num1 = float(input("Input first number: "))
            num2 = float(input("Input second number: "))
            
            if choice == 1:
                print("Result:", addition(num1, num2))
            elif choice == 2:
                print("Result:", subtraction(num1, num2))
            elif choice == 3:
                print("Result:", multiplication(num1, num2))
            elif choice == 4:
                print("Result:", division(num1, num2))
        else:
            print("Invalid choice. Please select a valid option.")
    except ValueError:
        print("Invalid input. Please enter numeric values.")
