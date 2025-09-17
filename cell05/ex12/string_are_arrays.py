user_input = input("Enter a string: ")

params = user_input.split()

if len(params) != 1:
    print("none")
else:
    s = params[0]
    z_count = s.count('z')
    if z_count == 0:
        print("none")
    else:
        print("z" * z_count)