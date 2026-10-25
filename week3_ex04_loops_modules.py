import random


# Question 1: Using a for loop with a list
fruits = ["apple", "banana", "orange", "grape"]
for fruit in fruits:
	print(fruit)

# -------------------------------------------------------------------------
# Question 2: Using a while loop for countdown
countdown = 5
while countdown >= 1:
	print(countdown)
	countdown -= 1

# -------------------------------------------------------------------------
# Question 3: Using a for loop with range()
for number in range(1, 11):
	print(number ** 2)

# -------------------------------------------------------------------------
# Question 4: Using the random module
colors = ["red", "blue", "green", "yellow", "purple"]
for color in random.sample(colors, 3):
	print(color)

# -------------------------------------------------------------------------
# Question 5: Custom math operations (defined here because this exercise
# is restricted to a single file; these functions mirror math_operations.py).
def add(a, b):
	return a + b


def subtract(a, b):
	return a - b


def multiply(a, b):
	return a * b


def divide(a, b):
	if b != 0:
		return a / b
	return "Error: Division by zero"


while True:
	operation = input("Enter +, -, *, /, or q to quit: ").strip().lower()
	if operation == "q":
		break
	if operation not in {"+", "-", "*", "/"}:
		print("Invalid operation")
		continue

	try:
		first_number = float(input("Enter the first number: "))
		second_number = float(input("Enter the second number: "))
	except ValueError:
		print("Please enter valid numbers")
		continue

	operations = {"+": add, "-": subtract, "*": multiply, "/": divide}
	print(operations[operation](first_number, second_number))
