input1 = input("Enter a number: ")
input2 = input("Enter another number: ")
print("Thank you")
try:
    num1 = int(input1)
    num2 = int(input2)
    print(f"{num1} + {num2} = {num1 + num2}")
    print(f"{num1} - {num2} = {num1 - num2}")
    print(f"{num1} * {num2} = {num1 * num2}")
    if num2 != 0:
        print(f"{num1} / {num2} = {num1 / num2}")
    else:
        print(" Not allowed.")
except ValueError:
    print("Error")
