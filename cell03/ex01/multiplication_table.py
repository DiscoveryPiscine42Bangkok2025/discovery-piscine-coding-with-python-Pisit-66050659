input_number = input("Enter a number : ")
try:
    number = int(input_number)
    for i in range(0, 13):
        result = number * i
        print(f"{number} x {i} = {result}")
except ValueError:
    print("Invalid input. Please enter an integer number.")
