# Logical Operators = evaluate multiple conditions in boolean type prompts(or, and, not)
#                or = at least one condition must be true
#               and = both conditions must be true
#               not = inverts the conditions
guests = 50
is_rainy = False
if guests <= 20  and not is_rainy:
    print("The party is NOT cancelled")
    print("Make sure to be on time!")
elif is_rainy and not guests < 30:
    print("The party is cancelled")
    print("We'll plan a party for next time")
else :
    print("We'll plan a party for next time")
#Conditional Operators = A one_line shortcut for the if-else statement
#                        Print or Assign one of two values based on a condition
#                        X if conditions else Y

num =91
# print("Over 80" if 70<= num <= 80 else "Less than 70")
result1 = "EVEN" if num%2==0 else "ODD"
print(result1)

# string methods
# name = input(""Enter your Full name: ")
# phone_number = input("Enter your phone #: ")
# result = len(name) counts every digit or word including space in the string and shows as result
# result = name.rfind("i") does a reverse check for the alpha or string in the bracket
#          and gives its position as result
# name=name.upper/lower() converts all letters in upper/lower letters
# name = name.capitalize() makes the first letter of the string capital
# result = name.isdigit() gives a boolean statement of true or false
#          if there is only digits in the 'name' string
# result = name.isalpha() gives a boolean statement if true or false
#          if there is only alphabets in the 'name' command
# result = phone_number.count("9") # Counts the instances and gives the result as integers
# phone_number = phone_number.replace("7","9")
# Replaces the old string(left of comma in bracket) with the new one(right of comma)
# print(phone_number)
# print(type(phone_number))

# exercise time
# Validate user input exercise
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits
username = input("Enter Your Username: ")
if len(username)<=12 and username.isalpha():
    print(f"Welcome {username}")
else:
    print("Your username is not valid")