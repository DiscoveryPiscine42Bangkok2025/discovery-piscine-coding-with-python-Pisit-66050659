import sys
args = sys.argv[1:]
input_u = input("Enter a list of numbers : ").split()
args = input_u
print([int(x) + 2 for x in args])
