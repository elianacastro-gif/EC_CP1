#EC 1st lists notes
import random

sibs = ["alex", "katie", "andrew", "vienna", "tia", "treyson", "jefferson", "jake"]

print(sibs[5])
print(f"The list is {len(sibs)} people long")
print(sibs)
sibs[0] = "eric"
sibs[6:-1] = ["xavier", "hailey"]
sibs.pop()
sibs.pop(3)
sibs.remove("andrew")
#sibs.clear
#sibs.append("andrew") adds to end of list
sibs.insert(2, "andrew")
sibs.extend(["joseph", "israel", "zee"])
print(sibs)

board = [[1,2,3]
        [4,5,6]
        [7,8,9]
        ]

Fruit = ("apple", "orange", "pineapple") #tuple ordered, not changeable

veggies = {"spinah", "kale", "broccoli", "carrot"} #set unordered, changeable 
print(veggies)