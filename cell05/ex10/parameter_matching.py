input_user = input("Enter something: ")

if input_user == "Hello" or input_user == "hello":
    print("Good job!")
elif input_user.isnumeric():
    print("none")
else:
    print("Nope, sorry...")