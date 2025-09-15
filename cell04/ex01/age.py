age = input("How old are you? ")
try:
	age = int(age)
	print(f"You are currently {age} years old")
	for years in [10, 20, 30]:
		future_age = age + years
		print(f"In {years} years you will be {future_age} years old")
except ValueError:
	print("Please enter a valid number.")
