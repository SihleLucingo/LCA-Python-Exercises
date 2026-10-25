# Question 1: Arithmetic and Assignment Operators
x = 10
y = 2
x += 3
y *= 2
result = x / y
print(result)

# Question 2: Comparison and Logical Operators
a = 5
b = 4
c = 3
a_greater_than_b = a > b
b_is_even = b % 2 == 0
c_less_than_or_equal_to_a = c <= a
final_condition = a_greater_than_b or (b_is_even and c_less_than_or_equal_to_a)
print(final_condition)

# Question 3: Conditional Statements
score = float(input("Enter a test score (0-100): "))
if 90 <= score <= 100:
	grade = "A"
elif 80 <= score < 90:
	grade = "B"
elif 70 <= score < 80:
	grade = "C"
elif 60 <= score < 70:
	grade = "D"
elif 0 <= score < 60:
	grade = "F"
else:
	grade = "Invalid score"
print(grade)

# Question 4: Combining Operators and Conditionals
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter an operation (+, -, *, /): ").strip()

if operation == "+":
	operation_result = num1 + num2
elif operation == "-":
	operation_result = num1 - num2
elif operation == "*":
	operation_result = num1 * num2
elif operation == "/":
	if num2 == 0:
		operation_result = "Cannot divide by zero"
	else:
		operation_result = num1 / num2
else:
	operation_result = "Invalid operation"

print(operation_result)
