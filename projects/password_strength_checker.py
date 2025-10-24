#EC 1st password strength checker 

#make variable to start the loop
start = True

#print the program
print("this will check how strong your password is")
#make score 0
score = 0
#check varible and add the values
len = "no"
upper = "no
lower = "no"
digit = "no"
special = "no"

#ask for password
password = ("what is your password: ")
#check length
length = len(password)
 if length >= 8:
    score += 1
     len ="yes"

#check uppercase
#check if true if true +1 for score
for character in password:
    if character.isupper():
        upper = "yes"
if up == "yes":
    score += 1

#check lowercase
#check if true if true +1 to score
for character in password:
    if character.islower():
        lower = "yes"
if lower == "yes":
    score += 1
    
#check for numbers
#check if true and if true +1 to score
for characters in password:
    if characters.isdigit():
        digit = "yes"
if digit == "yes" :
    score += 1
#check for special signs
#check if true and add 1 to score if true
for characters in password:
    if chracter.isspecial():
        special = "yes"
if special == "yes":
    score += 1
#calculate score
if score == 1:
    print("your password is very weak")
elif score == 2:
    print("your password is weak")
elif score == 3:
    print("your password is mid")
elif score == 4:
    print("your password is ok")
elif score == 5:
    print("your password is strong")
else:
    ("your password is weak")

#end code ask if they want to check again
start_2 = int(input("do you want to check again: )
if start_2 == 2:
    start = false
    print("goodbye")
