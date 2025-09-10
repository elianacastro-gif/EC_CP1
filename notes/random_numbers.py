#EC 1st random numbers notes

import random

# generate stat options 
stat_one = random.randit (1,10) + random.randint(1,10)
stat_two = random.randit (1,10) + random.randint(1,10)
stat_three = random.randit (1,10) + random.randint(1,10)
stat_four = random.randit (1,10) + random.randint(1,10)
stat_five = random.randit (1,10) + random.randint(1,10)
stat_six = random.randit (1,10) + random.randint(1,10)
stat_seven = random.randit (1,10) + random.randint(1,10)


# telling user the stat choice
print(f"your stat options are: {stat_one},  {stat_two}, {stat_three}, {stat_four},  {stat_five},  {stat_six}, {stat_seven}")

#set stats
strenght = int(input("what stat do you want as your strength; \n"))


print(f"this is a random number from 0 - 1: {random.random()}")
print(f"this is a random number from 0 - 20: P{random.randint(1,20)}")
