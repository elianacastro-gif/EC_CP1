#EC 1st functions
#set variables first

#define functions
def add(x,y):
    return x+y

def initials(name):
    names = name.split("")
    initials = ""
    for name in names: 
     initials += name [0]

total = add(5,5)
print(total)
print(f"10 + 72 + {add(10,72)}")
x = 0
while x < add(3,9):
    print("duck")
    x+= 1

print("Goose")

#use fro project

print(f"a = {ord("a")}")
print(f"98 = {chr(98)}")