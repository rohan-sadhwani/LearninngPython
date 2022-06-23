# Snake Water Gun Game
import random

uscore = 0
cscore = 0
tie = 0

def startgame(usr, cmp):
    global uscore, cscore, tie
    if user != "error":
        if usr == "Snake":
            if cmp == "Snake":
                print(f"User : {usr} | Comp : {cmp}")
                print("Tie! No point")
                tie = tie + 1
            elif cmp == "Water":
                print(f"User : {usr} | Comp : {cmp}")
                print("User Won")
                uscore = uscore + 1
            elif cmp == "Gun":
                print(f"User : {usr} | Comp : {cmp}")
                print("Comp Won")
                cscore = cscore + 1
        elif usr == "Water":
            if cmp == "Snake":
                print(f"User : {usr} | Comp : {cmp}")
                print("Comp Won")
                cscore = cscore + 1
            elif cmp == "Water":
                print(f"User : {usr} | Comp : {cmp}")
                print("Tie! No point")
                tie = tie + 1
            elif cmp == "Gun":
                print(f"User : {usr} | Comp : {cmp}")
                print("User Won")
                uscore = uscore + 1
        else:
            if cmp == "Snake":
                print(f"User : {usr} | Comp : {cmp}")
                print("User Won")
                uscore = uscore + 1
            elif cmp == "Water":
                print(f"User : {usr} | Comp : {cmp}")
                print("Comp Won")
                cscore = cscore + 1
            elif cmp == "Gun":
                print(f"User : {usr} | Comp : {cmp}")
                print("Tie! No point")
                tie = tie + 1
    else:
        print("Please enter correct choice!")


game = ["Snake", "Water", "Gun"]
print("******Snake Water Gun Game******")
print("Best of 10 rounds wins")
for i in range(0, 10):
    print("\nPress S for Snake... W for Water... G for Gun")
    usch = input("Enter your choice : ")
    if usch == "S" or usch == "s":
        user = "Snake"
    elif usch == "W" or usch == "w":
        user = "Water"
    elif usch == "G" or usch == "g":
        user = "Gun"
    else:
        user = "error"
    comp = random.choice(game)

    startgame(user, comp)

print(f"\nUser Score : {uscore} | Computer Score : {cscore} | Tie : {tie}")
if uscore > cscore:
    print("User Won")
else:
    print("Comp Won")
