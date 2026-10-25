"""Practice creating and using lists and dictionaries."""

# Question 1: Creating and Modifying Lists
fruits = ["apple", "banana", "orange"]
fruits.append("grape")
fruits.insert(0, "mango")
fruits.remove("banana")
print("Modified fruits:", fruits)

#-------------------------------------------------------------------------
# Question 2: List Operations
numbers = [1, 2, 3, 4, 5]
squared_numbers = [number ** 2 for number in numbers]
total = sum(numbers)
average = total / len(numbers)
print("Squared numbers:", squared_numbers)
print("Sum:", total)
print("Average:", average)

#-------------------------------------------------------------------------
# Question 3: Creating and Modifying Dictionaries
capitals = {
	"France": "Paris",
	"Japan": "Tokyo",
	"Italy": "Rome",
}
capitals["Canada"] = "Ottawa"
capitals["Japan"] = "Kyoto"
del capitals["Italy"]
print("Modified capitals:", capitals)

#-------------------------------------------------------------------------
# Question 4: Dictionary Operations
fruit_colors = {
	"apple": "red",
	"banana": "yellow",
	"grape": "purple",
}
print("Fruits:", list(fruit_colors.keys()))
print("Colors:", list(fruit_colors.values()))
for fruit, color in fruit_colors.items():
	print(f"{fruit}: {color}")

fruit_to_check = "banana"
if fruit_to_check in fruit_colors:
	print(f"The color of {fruit_to_check} is {fruit_colors[fruit_to_check]}.")
else:
	print(f"{fruit_to_check} is not in the dictionary.")
