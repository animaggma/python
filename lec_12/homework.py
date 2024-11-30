"""
Create a file that will contain 100 lines, each line will contain  20 random  numbers. 
Read all the file lines and using map function convert the line into integer array.
Using filter function filter the numbers which are > 40 
Write the data back to file
Read the same file as a generetor(use yield to achieve that)
Create decorator that will measure the function execution time 

"""

import random
import time

def execution_time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time of {func.__name__}: {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@execution_time_decorator
def create_file(filename, num_lines=100, num_numbers_per_line=20):
    try:
        with open(filename, 'w') as file:
            for _ in range(num_lines):
                numbers = [str(random.randint(1, 100)) for _ in range(num_numbers_per_line)]
                file.write(" ".join(numbers) + "\n")
        print(f"File '{filename}' created successfully.")
    except IOError as e:
        print(f"Error creating file: {e}")

@execution_time_decorator
def filter_and_write_back(filename, threshold=40):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

        filtered_lines = []
        for line in lines:
            numbers = list(map(int, line.split()))
            filtered_numbers = list(filter(lambda x: x > threshold, numbers))
            filtered_lines.append(" ".join(map(str, filtered_numbers)))

        with open(filename, 'w') as file:
            for line in filtered_lines:
                file.write(line + "\n")

        print(f"File '{filename}' filtered successfully.")
    except IOError as e:
        print(f"Error reading or writing to file: {e}")

@execution_time_decorator
def read_file_as_generator(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                yield line.strip()
    except IOError as e:
        print(f"Error reading file: {e}")

if __name__ == "__main__":
    filename = "random_numbers.txt"

    create_file(filename)

    filter_and_write_back(filename)

    print("\nReading the file as a generator:")
    generator = read_file_as_generator(filename)
    for i, line in enumerate(generator):
        print(f"Line {i + 1}: {line}")
        if i >= 4:
            break
