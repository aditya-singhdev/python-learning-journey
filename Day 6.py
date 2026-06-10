# for loops = execute specific code for the given time
# for x in range(80,0,-1):
#     print(x)
# credit="1234-5678-9012-3456"
# for x in credit[::-1]:
#     print(x)
# let's build a countdown timer
import time
timer=int(input("Enter the time needed in seconds: "))
for x in range(timer,0,-1):
    seconds = int(x) %60
    minutes=int(x/60)%60
    hours=int(x/3600)
    time.sleep(1)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
print("Time's UP!!!")


for x in range(1,6):
    for y in range(1,11):
        print(f"{x}x{y}={x*y}")