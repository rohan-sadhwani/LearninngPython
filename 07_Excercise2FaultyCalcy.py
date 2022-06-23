# Design a calculator which will correctly solve all thr problems except the following:
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4

num1 = int(input("Enter number 1 : "))
num2 = int(input("Enter number 2 : "))
op = input("Enter operator for the equation : ")

if op == "+":
    if num1 == 56 and num2 == 9:
        print("Ans is 77")
    else:
        print("Ans is :", num1 + num2)
elif op == "-":
    print("Ans is :", num1 - num2)
elif op == "*":
    if num1 == 45 and num2 == 3:
        print("Ans is 555")
    else:
        print("Ans is :", num1 * num2)
elif op == "/":
    if num1 == 56 and num2 == 6:
        print("Ans is 4")
    else:
        print("Ans is :", num1 / num2)
else:
    print("Please Enter correct operator!")
