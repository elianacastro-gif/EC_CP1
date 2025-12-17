#EC 1st Final

#add stats of each character 
#your stats
player_hp = 1000
player_damage = 10-50

#character one BC
#health, damage/attack, 
BC_hp = 1000
BC_damage = 10-80
BC_defence = 30
#Character two LK
#health, damage/attack, 
LK_hp = 1000
LK_damage = 10-60
LK_defence = 30
#character three CB
#health, damage/attack, 
CB_hp = 1000
CB_damage = 10-60
CB_defence = 30
#character four HJ
#health, damage/attack, 
HJ_hp = 1000
HJ_damage = 10-60
HJ_defence = 30
#character five JS
#health, damage/attack, 
JS_hp = 1000
JS_damage = 10-60
JS_defence = 30
#character six LX
#health, damage/attack, 
LX_hp = 1000
LX_damage = 10-40
LX_defence = 30
#character seven SM
#health, damage/attack, 
SM_hp = 1000
SM_damage = 10-60
SM_defence = 30
#character eight IN
#health, damage/attack, 
IN_hp = 1000
IN_damage = 10-60
IN_defence = 30
#final boss JYP 
#health, damage/attack, 
JYP_hp = 5000
JYP_damage = 200-250
JYP_defence = 30

#name all the rooms and turn them into varibles
Room_1 = ()
Room_2 = ()
Room_3 = ()
Room_4 = ()
Room_5 = ()
Room_6 = ()
Room_7 = ()
Room_8 = ()
#name all the weapons and what happens/whose in the room
#start area (inside front company building)
print ("you are in the JYPE building. There are 8 rooms you can go in.", [Room_1, Room_2, Room_3, Room_4, Room_5, Room_6, Room_7, Room_8])
#choose which of 8 rooms to go to describe how to get there and what surroundings are like
#make a path and ask which on they will take 
print("you walk down a long hallway. where would you like to go: ")

#ask what room they want to go into 
#make it so which ever room they choose it will go to that rooms design and story
room = (Room_1, Room_2, Room_3, Room_4,Room_5, Room_6, Room_7, Room_8)



#named variable of room (1/rec studio)
#what room looks is like in a print statement
def room ():
    if room == Room_1:
        print("you have entered the recording studio. There is only one light in the room above the table. oh! BC is here!")
    else:
        print("you have entered (Room_2-Room_8))
              

#items in the room and how you get them what the do (lightstick that gives health)
game =()
#whose in the room (BC) and how do you fight them? write code to fight
print("You and BC will fight to see who can write the most lyrics. it will be an easy gae of ne round"
#import random to generate numbers for the fight
import random

hit_roll = random.randint(10-80) + BC_damage
if hit_roll == 20:
    print("you got a crit! that means you get to roll for damage twice!")
    damage_roll = random.randint(10,80) + random.randint(10,80) + player_damage
    print(f"you did {damage_roll-BC_defence} damage.")
    BC_hp -= (damage_roll-BC_defence)
elif  hit_roll == 1:
    print("you roll a critical failure! now the monster gets to attack you!")
    damage_roll = random.randint(10,80) + BC_damage
    player_hp -= (damage_roll)
    print(f"BC rolled {damage_roll}, you hp is now {player_hp} ")
elif hit_roll + player_damage >= 12:
    print("you hit! roll for damage!")
    damage_roll = random.randint(10,80) + player_damage
    if damage_roll > BC_defence:
        print(f"you did {damage_roll-BC_defence} damage.")
        BC_hp -= (damage_roll-BC_defence)
    else:
        print("you did no damage.")
else:
    print("you missed.")

print("your turn is over")

while game:
    BC_hp -= 1000
if BC_hp <= 0:
    print("you win")
    game = False

#let them leave the room
leave_room=()
def leave_room():
    print("leaving room")
    



#describe paths and rooms they can enter
Print("you are in the hallway again. Which room do you want to go into: )
#named varible of room (2/dance pract. room)
Room_2 =()
#what room looks like and how it works. whose in the room (LK)
def room():
    if room == Room_2:
        print("you have entered the dance practice room. The room is big and has a long lenth mirror on one of the walls. You look around and...oh! LK is here!")
    else: 
        print (Room_1-Room_8)



#set up fighting code
#figure out how to do the dance fight
#describe paths and rooms they can enter
print("your ack in the hallway. which room should we go into next: ")
#named varibale of room (3/)
Room_3 =()
#describe room in a print statement and what youll do 
#add whose in the room (CB)
def room():
    if room == Room_3:
        print("you have entered CB's dorm room. You look around and see CB on the couch. He looks ready for that rap battle.")
#set up fighting code and how to play/win the game
print("you will compete in a battle with CB on who can rap the fastest)
#show your stats for rapping and his stats to start the battle
#add a random number within your range and roll to see who wins
#add the print stament that you win when you win and how much your stats go up
#if lose give them a choice to replay till they win
hit_roll = random.randint(10-60) + CB_damage
if hit_roll == 20:
    print("you got a crit! that means you get to roll for damage twice!")
    damage_roll = random.randint(10,60) + random.randint(10,80) + player_damage
    print(f"you did {damage_roll-CB_defence} damage.")
    CB_hp -= (damage_roll-CB_defence)
elif  hit_roll == 1:
    print("you roll a critical failure! now the monster gets to attack you!")
    damage_roll = random.randint(10,60) + CB_damage
    player_hp -= (damage_roll)
    print(f"CB rolled {damage_roll}, you hp is now {player_hp} ")
elif hit_roll + player_damage >= 12:
    print("you hit! roll for damage!")
    damage_roll = random.randint(10,60) + player_damage
    if damage_roll > CB_defence:
        print(f"you did {damage_roll-CB_defence} damage.")
        CB_hp -= (damage_roll-CB_defence)
    else:
        print("you did no damage.")
else:
    print("you missed.")

print("your turn is over")

while game:
    CB_hp -= 1000
if CB_hp <= 0:
    print("you win")
    game = False
#let them leave room
print("leaving room")



#describe paths and rooms they can enter

#named value for room(4/dance prat. room 2nd)
Room_4 =()
#describe the room and what you will have to do/movements
#add who is in the room (HJ) and how you will fight them
def room():
    if room == Room_4:
        print("You have entered the 2nd dance practice room. The room is smaller but it still has that long length mirror on the wall.' Oop...HJ there you are!' ")
#set up fighting code
#show stats of each of the characters
#once they win print they have won and give them their "prize"
#if they lost give hem ths chance to retry

hit_roll = random.randint(10-60) + HJ_damage
if hit_roll == 20:
    print("you got a crit! that means you get to roll for damage twice!")
    damage_roll = random.randint(10,60) + random.randint(10,60) + player_damage
    print(f"you did {damage_roll-HJ_defence} damage.")
    HJ_hp -= (damage_roll-HJ_defence)
elif  hit_roll == 1:
    print("you roll a critical failure! now the monster gets to attack you!")
    damage_roll = random.randint(10,60) + HJ_damage
    player_hp -= (damage_roll)
    print(f"HJ rolled {damage_roll}, you hp is now {player_hp} ")
elif hit_roll + player_damage >= 12:
    print("you hit! roll for damage!")
    damage_roll = random.randint(10,60) + player_damage
    if damage_roll > HJ_defence:
        print(f"you did {damage_roll-CB_defence} damage.")
        HJ_hp -= (damage_roll-HJ_defence)
    else:
        print("you did no damage.")
else:
    print("you missed.")

print("your turn is over")

while game:
    HJ_hp -= 1000
if HJ_hp <= 0:
    print("you win")
    game = False
#let them leave the room
print("leaving the room")
#describe paths and rooms they can enter

#named variable of room (5/)
Room_5 =()
#describe room and movements  also who is in the room (JS)
def room():
    if room == Room_5:
        print("You have entered the Cafeteria. The room is full of staff eating food. You keep walking and find JS who is eating. 'Now is not the time for eating JS!' ")
#who will you fight and how to win
#fighting code 
#if won their stats go up (one of three)
#if lost let them retry

hit_roll = random.randint(10-60) + JS_damage
if hit_roll == 20:
    print("you got a crit! that means you get to roll for damage twice!")
    damage_roll = random.randint(10,60) + random.randint(10,60) + player_damage
    print(f"you did {damage_roll-JS_defence} damage.")
    JS_hp -= (damage_roll-HJ_defence)
elif  hit_roll == 1:
    print("you roll a critical failure! now the monster gets to attack you!")
    damage_roll = random.randint(10,60) + JS_damage
    player_hp -= (damage_roll)
    print(f"JS rolled {damage_roll}, you hp is now {player_hp} ")
elif hit_roll + player_damage >= 12:
    print("you hit! roll for damage!")
    damage_roll = random.randint(10,60) + player_damage
    if damage_roll > JS_defence:
        print(f"you did {damage_roll-JS_defence} damage.")
        JS_hp -= (damage_roll-JS_defence)
    else:
        print("you did no damage.")
else:
    print("you missed.")

print("your turn is over")

while game:
   JS_hp -= 1000
if JS_hp <= 0:
    print("you win")
    game = False
#let them leave the room
print("leaving the room")

#describe path and rooms they can enter
print(you are back in the hallway. which room do you want to enter: )



#named variable room (6/dorm room Kit.)
Room_6 =()
#add the description of the room
#whose in the room (LX) and how to defeat them
def room ():
    if room == Room_6:
        print("You have entered LX's dorm room. You can smell a scent of food. You walk and find LX in the kitchen. 'LX! Why are you cooking?!' ")
#any items they can get if any (frying pan used as a weapon)
#fighting code and if they win or lose


hit_roll = random.randint(10-60) + LX_damage
if hit_roll == 20:
    print("you got a crit! that means you get to roll for damage twice!")
    damage_roll = random.randint(10,60) + random.randint(10,60) + player_damage
    print(f"you did {damage_roll-HJ_defence} damage.")
    LX_hp -= (damage_roll-LX_defence)
elif  hit_roll == 1:
    print("you roll a critical failure! now the monster gets to attack you!")
    damage_roll = random.randint(10,60) + LX_damage
    player_hp -= (damage_roll)
    print(f"LX rolled {damage_roll}, you hp is now {player_hp} ")
elif hit_roll + player_damage >= 12:
    print("you hit! roll for damage!")
    damage_roll = random.randint(10,60) + player_damage
    if damage_roll > LX_defence:
        print(f"you did {damage_roll-LX_defence} damage.")
        LX_hp -= (damage_roll-LX_defence)
    else:
        print("you did no damage.")
else:
    print("you missed.")

print("your turn is over")

while game:
    LX_hp -= 1000
if LX_hp <= 0:
    print("you win")
    game = False
#let them leave the room
print("leaving the room")

#describe path and rooms they can enter

#named variable room (7/vocal room)
Room_7 =()
#room description
def room():
    if room == Room_7:
        print("You have entered the vocal room. 'hmm I wonder if SM is in here...'")
#add any items if (microphone dropped after you beat him)
#whose in the room (SM) and how to defeat them
#fighting code  if they win/lose
hit_roll = random.randint(10-60) + SM_damage
if hit_roll == 20:
    print("you got a crit! that means you get to roll for damage twice!")
    damage_roll = random.randint(10,60) + random.randint(10,60) + player_damage
    print(f"you did {damage_roll-SM_defence} damage.")
    SM_hp -= (damage_roll-SM_defence)
elif  hit_roll == 1:
    print("you roll a critical failure! now the monster gets to attack you!")
    damage_roll = random.randint(10,60) + SM_damage
    player_hp -= (damage_roll)
    print(f"SM rolled {damage_roll}, you hp is now {player_hp} ")
elif hit_roll + player_damage >= 12:
    print("you hit! roll for damage!")
    damage_roll = random.randint(10,60) + player_damage
    if damage_roll > SM_defence:
        print(f"you did {damage_roll-SM_defence} damage.")
        SM_hp -= (damage_roll-SM_defence)
    else:
        print("you did no damage.")
else:
    print("you missed.")

print("your turn is over")

while game:
    SM_hp -= 1000
if SM_hp <= 0:
    print("you win")
    game = False
#let them leave the room

#descriibe which rooms they can choose (out of 8)

#room (8/)
Room_8 = ()
#add description
#who is in the room (IN)and how to beat them in your fight
def room():
    if room == Room_8:
        print("You have entered the ___. You walk and see IN.")
#if they win or lose add the print statement for it and add ore to their stats(one of 3)

hit_roll = random.randint(10-60) + IN_damage
if hit_roll == 20:
    print("you got a crit! that means you get to roll for damage twice!")
    damage_roll = random.randint(10,60) + random.randint(10,60) + player_damage
    print(f"you did {damage_roll-IN_defence} damage.")
    IN_hp -= (damage_roll-HJ_defence)
elif  hit_roll == 1:
    print("you roll a critical failure! now the monster gets to attack you!")
    damage_roll = random.randint(10,60) + IN_damage
    player_hp -= (damage_roll)
    print(f"IN rolled {damage_roll}, you hp is now {player_hp} ")
elif hit_roll + player_damage >= 12:
    print("you hit! roll for damage!")
    damage_roll = random.randint(10,60) + player_damage
    if damage_roll > IN_defence:
        print(f"you did {damage_roll-IN_defence} damage.")
        IN_hp -= (damage_roll-IN_defence)
    else:
        print("you did no damage.")
else:
    print("you missed.")

print("your turn is over")

while game:
    IN_hp -= 1000
if IN_hp <= 0:
    print("you win")
    game = False
#let them leave the room
print("leaving the room")
#describe paths and rooms they can enter
#let them leave room

#once you defeat evceryone you will get a story that will lead you to the concert venue 

#area 9 the venue
area_9 = ()
#add who the person is you are fighting (JYP) and how to beat him.
if room == area_9:
    print("You have arrived at the stadium with all the members! 'That was hard but i did it...oh who is that...?' ")
#you will use all the stats youve earned. His stats will show up as you battle after each attack
#make battle code (damage and health)
#ask what attack they want (any of 4) ask after every attack
#add print statement that theyve won 
#if they lose give them an option to retry

#after the game is done. Ask if they want to play again
#if yes then bring them back to the start
print("The End", "would you like to play again :")

    
