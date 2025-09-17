import sys
args = sys.argv[1:]
input_u = input("Enter a list of numbers : ").split()
args = input_u
numbers = [int(x) for x in args]
result = [x + 2 for x in numbers if x > 5]
print(result)
