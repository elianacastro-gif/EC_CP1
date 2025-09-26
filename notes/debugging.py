#EC 1st debugging

#syntax error - grammar error 
#print "eliana"
# =. read error message, go to that line of code, fix the syntax

#logic error - we gave wrong steps
numone = "2"
numtwo = "5"

print(numone + numtwo)

# have well thought out plan, step by step go though logic

#runtime error -happen when code runs 
import random 
while True:
    denominator = random.randint(0,5)   
    
    print (10/denominator)