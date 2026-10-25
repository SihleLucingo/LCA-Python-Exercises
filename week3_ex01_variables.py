# Question 1: Variable Assignment and String Manipulation

name = input("Enter your name: ")
surname = input("Enter your surname: ")
age = input("Enter your age: ")

print("Hello, " + name + " " + surname + "! You are " + age + " years old.")

# Question 2: Integer Operations
# ============================================================

length = int(input("Enter the rectangle length: "))
width = int(input("Enter the rectangle width: "))

area = length * width

print("The area of the rectangle is " + str(area) + ".")

# Question 3: Working with Floats
# ============================================================

celsius = float(input("Enter temperature in Celsius: "))
print(celsius)

fahrenheit = (celsius * 9 / 5) + 32

print(f"{celsius}°C is equal to {fahrenheit}°F.")