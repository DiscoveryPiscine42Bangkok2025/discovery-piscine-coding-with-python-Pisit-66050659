params = input("Enter parameters separated by spaces: ").split()

if not any(params):
    print("none")
else:
    print(f"parameters: {len(params)}")
    for param in params:
        print(f"{param} {len(param)}")