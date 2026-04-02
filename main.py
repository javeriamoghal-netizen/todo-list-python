tasks=[]

while True:
    print("\n----TO DO LIST----")
    print("1.Add Task")
    print("2.View Tasks")
    print("3.Delete Task")
    print("4.Exit")

    choice=input("Enter your choice:")

    if choice=="1":
        task=input("Enter task:")
        tasks.append(task)
        print("Task added sucessfully!")

    elif choice=="2":
        if len(tasks)==0:
            print("No tasks available")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(i+1,".",tasks[i])

    elif choice=="3":
        if len(tasks)==0:
            print("No tasks to delete.")
        else:
            num=int(input("Enter task number to delete:"))
            if 1<=num<=len(tasks):
                tasks.pop(num-1)
                print("Tasks deleted successfully!")
            else:
                print("Invalid task number.")

    elif choice=="4":
        print("Exiting program...")
    
    else:
        print("Invalid choice.Try again.")