#EC 1st list manager

Shopping_list = []

while True:
    action = input("\n1. add task\n2. remove task\n3. print list\n4. exit\n")

    if action == "1":
        task = input("enter task: ")
        Shopping_list.append(task)
        print(f"'{task}' added")
    elif action == "4":
        break
    elif action == "2": 
        task = int(input("what item do you want to remove: "))
        task = Shopping_list[task-1]
        if task in Shopping_list:
            Shopping_list.remove(task)
            print(f"{task} was removed from list")
        else:
            print("item not found")
    elif action == "3":
        print(Shopping_list)