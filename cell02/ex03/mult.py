first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
result = first_number * second_number
print("The result is = ", result)
if result > 0:
    print("This number is positive.")
elif result < 0:
    print("This number is negative.")
else:
    print("This number is zero.")