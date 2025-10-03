#EC 1st while loop
import time
import random
#infinite loop
num = 1

while num <= 20:
    time.sleep(1)
    print(num)
    num += 1 #prevents an infinite loop
else:
    print("the condition was met")


goose = random.randint(1,20)
count = 0

while True:
    count =+ 1
    if count == goose:
        break
    else:
        print("duck")

print("GOOSE!")