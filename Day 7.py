Information = []
while True:
    name=input("Please Enter Your Name: ")
    if name=="":
        continue
    age=int(input("Please Enter Your Age: "))
    if age<=0:
        continue
    city=input("Enter The City You Live In: ")
    Informant=name,age,city
    Information.append(Informant)
    if not city=="":
        break
    else:
        continue
for infor in Information:
    print(infor[0],end="  ")
    print(infor[1])
    print(infor[2])
while True:
    name=input("Please Enter Your Name: ")
    if name=="":
        continue
    age = int(input("Please Enter Your Age: "))
    if age <= 0:
        continue
    city = input("Enter The City You Live In: ")
    if not city=="":
        break
    else:continue
Format=(name,age,city)
print(Format[0],end="  ")
print(Format[1])
print(Format[2])