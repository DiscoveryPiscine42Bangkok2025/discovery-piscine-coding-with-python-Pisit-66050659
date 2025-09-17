
import sys
args = sys.argv[1:]
if not args:
    user_input = input("Enter two numbers : ").split()
    args = user_input
if len(args) != 2:
    print("none")
else:
    try:
        start = int(args[0])
        end = int(args[1])
        step = 1 if start <= end else -1
        numbers = list(range(start, end + step, step))
        print(numbers)
    except ValueError:
        print("none")
