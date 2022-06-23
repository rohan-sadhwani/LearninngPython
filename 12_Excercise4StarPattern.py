n = int(input("Enter no of rows : "))
inp = input("Enter Boolean Type: 1 for True / 0 for False : ")
if inp == "1":
    bol = True
    a = 0
    for i in range(n):
        a = a + 1
        print(a * "* ")

elif inp == "0":
    bol = False
    a = n
    for i in range(n):
        print(a * "* ")
        a = a - 1
else:
    print("Please enter 1 or 0 only")
