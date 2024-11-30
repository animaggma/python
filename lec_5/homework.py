"""
1. Create a function called sum_of_elements that takes two arguments: a list of numbers (numbers) and an optional keyword argument exclude_negative (default value is False). This function should calculate the sum of all the elements in the list numbers, excluding negative numbers if exclude_negative is set to True. If exclude_negative is False, the function should include all elements in the sum.
In the main part of the program:

Ask the user to enter a list of numbers separated by spaces (e.g., "1 2 3 -4 5 -6").
Use string splitting to parse the input and create a list of numbers.
Ask the user if they want to exclude negative numbers (yes or no).
Call the sum_of_elements function with the list of numbers and the appropriate keyword argument.
Print the sum of the elements, considering the user's choice to exclude or include negative numbers.

"""
def sum_of_elements(numbers, exclude_negative=False):

    if exclude_negative:
        numbers = [num for num in numbers if num >= 0]
    return sum(numbers)

user_input = input("\nEnter a list of numbers separated by spaces: ")
try:
    numbers = [float(num) for num in user_input.split()]  
except ValueError: 
    print("Invalid input. Please try again.")
    exit()

exclude_negative_input = input("Do you want to exclude negative numbers? (yes or no): ").strip().lower()
exclude_negative = exclude_negative_input in ['yes', 'y']

result = sum_of_elements(numbers, exclude_negative=exclude_negative)

print(f"The sum of the elements is: {result}")

