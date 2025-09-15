input_num = input("Enter a number: ")
try:
	num = float(input_num)
	if num == int(num):
		print("The number is int.")
	else:
		print("The number is a decimal.")
except ValueError:
	print("Invalid input.")
