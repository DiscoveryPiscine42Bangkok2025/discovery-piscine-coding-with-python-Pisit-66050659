number = [2, 8, 9, 48, 8, 22, -12, 2]
remove_duplicates = [x for x in number if number.count(x) == 1]
new_u = [x + 2 for x in remove_duplicates]
print(list(number))
print(list(new_u))
