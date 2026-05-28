# ========================================
# Python Basics: Complete Tutorial
# ========================================

print("=" * 50)
print("1. VARIABLES")
print("=" * 50)
# Variables store data values
name = "Deepu"
age = 25
height = 5.9
print(f"Name: {name}, Age: {age}, Height: {height}")

print("\n" + "=" * 50)
print("2. STRINGS")
print("=" * 50)
# Strings are sequences of characters
greeting = "Hello, World!"
message = 'Welcome to Python'
multiline = """This is a
multiline string
in Python"""

print(f"Greeting: {greeting}")
print(f"Message: {message}")
print(f"Multiline:\n{multiline}")

# String operations
text = "Python"
print(f"Length of '{text}': {len(text)}")
print(f"Uppercase: {text.upper()}")
print(f"Lowercase: {text.lower()}")
print(f"First 3 characters: {text[:3]}")

print("\n" + "=" * 50)
print("3. INTEGERS")
print("=" * 50)
# Integers are whole numbers
num1 = 10
num2 = 20
num3 = -5
num4 = 0

print(f"Integer examples: {num1}, {num2}, {num3}, {num4}")
print(f"Addition: {num1} + {num2} = {num1 + num2}")
print(f"Subtraction: {num2} - {num1} = {num2 - num1}")
print(f"Multiplication: {num1} * {num2} = {num1 * num2}")
print(f"Division: {num2} / {num1} = {num2 / num1}")
print(f"Floor Division: {num2} // {num1} = {num2 // num1}")
print(f"Modulus: {num2} % {num1} = {num2 % num1}")

print("\n" + "=" * 50)
print("4. FLOATS")
print("=" * 50)
# Floats are decimal numbers
price = 19.99
temperature = -5.5
pi = 3.14159

print(f"Float examples: {price}, {temperature}, {pi}")
print(f"Addition: {price} + 5.01 = {price + 5.01}")
print(f"Multiplication: {temperature} * 2 = {temperature * 2}")
print(f"Pi rounded to 2 decimals: {round(pi, 2)}")

print("\n" + "=" * 50)
print("5. BOOLEANS")
print("=" * 50)
# Booleans are True or False
is_student = True
is_employed = False

print(f"is_student: {is_student}")
print(f"is_employed: {is_employed}")

# Boolean operations
print(f"True and False: {True and False}")
print(f"True or False: {True or False}")
print(f"not True: {not True}")

# Comparison operations return booleans
print(f"10 > 5: {10 > 5}")
print(f"10 == 5: {10 == 5}")
print(f"10 != 5: {10 != 5}")

print("\n" + "=" * 50)
print("6. TYPE CASTING")
print("=" * 50)
# Converting between data types

# String to Integer
str_num = "42"
int_from_str = int(str_num)
print(f"String '{str_num}' to Integer: {int_from_str}, Type: {type(int_from_str)}")

# String to Float
str_decimal = "3.14"
float_from_str = float(str_decimal)
print(f"String '{str_decimal}' to Float: {float_from_str}, Type: {type(float_from_str)}")

# Integer to String
num = 100
str_from_int = str(num)
print(f"Integer {num} to String: '{str_from_int}', Type: {type(str_from_int)}")

# Integer to Float
int_num = 50
float_from_int = float(int_num)
print(f"Integer {int_num} to Float: {float_from_int}, Type: {type(float_from_int)}")

# Float to Integer
float_num = 7.99
int_from_float = int(float_num)
print(f"Float {float_num} to Integer: {int_from_float}, Type: {type(int_from_float)}")

# String to Boolean
print(f"bool('Hello'): {bool('Hello')}")
print(f"bool(''): {bool('')}")
print(f"bool(1): {bool(1)}")
print(f"bool(0): {bool(0)}")

print("\n" + "=" * 50)
print("7. USER INPUT")
print("=" * 50)

# Taking input from user

user_name = input("Enter your name: ")
print(f"Hello, {user_name}!")

user_age_str = input("Enter your age: ")
user_age = int(user_age_str)  # Convert string to integer
print(f"You are {user_age} years old")

user_height_str = input("Enter your height (in meters): ")
user_height = float(user_height_str)  # Convert string to float
print(f"Your height is {user_height} meters")

# Simple calculation with user input
num1_user = float(input("Enter first number: "))
num2_user = float(input("Enter second number: "))
result = num1_user + num2_user
print(f"{num1_user} + {num2_user} = {result}")

print("\n" + "=" * 50)
print("END OF TUTORIAL")
print("=" * 50)

