import sys
args = sys.argv[1:]
input_u = input("Enter a list of numbers : ").split()
args = input_u
numbers = [int(x) for x in input_u]
remove_duplicates = [x for x in numbers if numbers.count(x) == 1]
new_u = [x + 2 for x in remove_duplicates]
print(list(numbers))
print(list(new_u))