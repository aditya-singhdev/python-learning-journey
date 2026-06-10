friends = 10
# friends += 3
# friends -= 3
# friends *= 3
# friends /= 3
# friends **= 3
# friends -= 4
print(f"You have {friends} friends")
remainder = friends % 3

print(remainder)

x = 3.14
y = -4
z = 5

result1 = x
result2 = 873588655.3345678
result = (result1 + result2)
result5 = abs(y)
result6 = pow(y, 6)
result4 = max(x, y, z)
result8 = min(x, y, z)
print(f"{result:,}, {result5}, {result6}, {result4}, {result8}")

import math
x = 9
print(math.sqrt(x))
print(math.pi)
print(math.e)
print(math.ceil(9.89))
print(f"{math.floor(9.89)},{x}")

r = float(input("What is the radius of the circle?: "))
circumference = 2*math.pi*r
print(f"The circumference of the circle is {round(circumference,2)}cm"
      f" and the area of the circle is {round(math.pi*pow(r,2),2)}cm")
a = 3
b = 4
c = math.sqrt(pow(a,2)+pow(b,2))
print(c)

# If statements only happen if conditions are met otherwise else conditions happen

age = int(input("Whats is your age so you can enter the club?: "))
if age >= 18:
    print("You're 18, Welcome to the club!.")
elif age <10 :
    print("Minors aren't allowed here")
else:
    print("Grow up, then you're welcome")


response = (input("Would you like a drink with your popcorn for the movie[Y/N]?: "))
if response == "Y":
    print("Here's the drink with your popcorn, Enjoy the Movie!")
else:
    print("Enjoy the movie with your popcorn")
