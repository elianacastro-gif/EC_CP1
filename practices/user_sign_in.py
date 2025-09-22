#EC 1st user sign in

valid_username = "Elianac"
valid_password = "5342"
user_name = input("What is your user_name: ").strip().capitalize()
password = input("What is your password: ").strip()
if user_name == valid_username and password == valid_password:
    print("You succesfully logged in")
else: 
    print("you did not log in")