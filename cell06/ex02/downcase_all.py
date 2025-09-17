def downcase_it(s):
    return s.lower()

user_input = input("Enter text: ").split('"')

args = [s.strip() for s in user_input if s.strip()]

if not args:
    print("none")
else:
    for arg in args:
        print(downcase_it(arg))