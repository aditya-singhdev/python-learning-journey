# Typecasting is a way to change variables
# Either from int to float or vice versa or int and float to string or vice versa using
# str() int() float() bool() commands
name = "Aditya Singh"
age = 19
cgpa = 7.65
is_student = True

age = int(age)
age += 1
print(age)

# input() = A function that prompts the user to input data
#           Returns said entered data as string
age = int(input("What is your age?: "))
age += 10
print("Happy Birthday!!")
print(f"you are {age} years old now.")
milk = float(input("How much milk would you lke?: "))
milk -= 10.5
print(f"Here you go,{milk} litre's milk")

