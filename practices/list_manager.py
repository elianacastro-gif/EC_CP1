#EC 1st list manager

Shopping_list = ["flour", "milk", "eggs", "flour", "cake mix", "cooking spray", "sugar"]

while True:
    action = int(input "\n1. add task\n2. remove task\n3. show list\n4. exit")

    if action == 1:
        task = input("enter task: ")
        Shopping_list.append(task)
        print("f'{task}' added")
    elif action == "exit":
        break