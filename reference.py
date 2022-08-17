# Hello world message.
# Variables
# May only contain letters, number, and underscores- cannot start with number.
message = "Hello, World!"
print(message)

message = "Hello, Python Crash Course!"
print(message)


# Strings- anything inside single or double quotes.
# Changing case in a string.
name = "ryan hoover"
print(name)
print(name.title())
print(name.upper())
print(name.lower())
# Using variables in strings
first_name = "Ryan"
last_name = "Hoover"
full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}!")
message = f"Hello, {full_name.title()}!"
print(message)