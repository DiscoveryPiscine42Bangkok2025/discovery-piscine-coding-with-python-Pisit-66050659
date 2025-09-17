import sys
args = sys.argv[1:]

def add_one(n):
    return n + 1

x = input("Enter a number: ")
print("Before:", x)
x = int(x)           
x = add_one(x)
print("After:", x)