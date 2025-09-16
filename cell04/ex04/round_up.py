import math

num = input("Enter a number: ")
try:
    number = float(num)
    rounded_number = math.ceil(number)
    print(f"The rounded-up integer is: {rounded_number}")
except ValueError:
    print("Please enter a valid number.")
