try:

    def getdate():
        import datetime
        return datetime.datetime.now()


    def dietlog(nm):
        if nm != "Error":
            diet = input("Enter your current diet : ")
            timee = str(getdate())
            a = timee, " ", str(diet)
            with open(str(nm), "a") as f:
                f.write(str(a))
                f.write("\n")
            print("Diet logged Successfully!")

    def dietret(nm):
        if nm != "Error":
            with open(str(nm), "r") as f:
                content = f.read()
                print(content)
            print("Diet Retrieved Successfully!")

    def workret(nm):
        if nm != "Error":
            with open(str(nm), "r") as f:
                content = f.read()
                print(content)
            print("Exercise Retrieved Successfully!")


    def worklog(nm):
        if nm != "Error":
            work = input("Enter your current exercise : ")
            timee = str(getdate())
            a = timee, " ", str(work)
            with open(str(nm), "a") as f:
                f.write(str(a))
                f.write("\n")
            print("Exercise logged Successfully!")


    print("**********Menu**********")
    print("Press 1 for log\nPress 2 for retrieval")
    ch = int(input("Enter your choice : "))

    if ch == 1:
        print("\nPress 1 for Diet\nPress 2 for Exercise")
        logch = int(input("Enter your choice : "))
        if logch == 1:
            name = "error"
            print("\nWhich person diet log you want to Enter :")
            print("Press 1 for Rohan\nPress 2 fot Devesh\nPress 3 for Achint")
            dietch = int(input("Enter your choice : "))
            if dietch == 1:
                name = "14_rohandiet.txt"
            elif dietch == 2:
                name = "14_deveshdiet.txt"
            elif dietch == 3:
                name = "14_achintdiet.txt"
            else:
                print("Please Enter Proper Choice!")
            dietlog(name)
        elif logch == 2:
            name = "error"
            print("\nWhich person exercise log you want to Enter :")
            print("Press 1 for Rohan\nPress 2 fot Devesh\nPress 3 for Achint")
            dietch = int(input("Enter your choice : "))
            if dietch == 1:
                name = "14_rohanwork.txt"
            elif dietch == 2:
                name = "14_deveshwork.txt"
            elif dietch == 3:
                name = "14_achintwork.txt"
            else:
                print("Please Enter Proper Choice!")
            worklog(name)
        else:
            print("Please enter proper choice!")
    elif ch == 2:
        print("\nPress 1 for Diet\nPress 2 for Exercise")
        retch = int(input("Enter your choice : "))
        if retch == 1:
            name = "error"
            print("\nWhich person diet log you want to Enter :")
            print("Press 1 for Rohan\nPress 2 fot Devesh\nPress 3 for Achint")
            workch = int(input("Enter your choice : "))
            if workch == 1:
                name = "14_rohandiet.txt"
            elif workch == 2:
                name = "14_deveshdiet.txt"
            elif workch == 3:
                name = "14_achintdiet.txt"
            else:
                print("Please Enter Proper Choice!")
            dietret(name)
        elif retch == 2:
            name = "error"
            print("\nWhich person exercise log you want to Enter :")
            print("Press 1 for Rohan\nPress 2 fot Devesh\nPress 3 for Achint")
            workch = int(input("Enter your choice : "))
            if workch == 1:
                name = "14_rohanwork.txt"
            elif workch == 2:
                name = "14_deveshwork.txt"
            elif workch == 3:
                name = "14_achintwork.txt"
            else:
                print("Please Enter Proper Choice!")
            workret(name)
        else:
            print("Please enter proper choice!")
    else:
        print("Please enter proper choice!")
except Exception as e:
    print(e)
