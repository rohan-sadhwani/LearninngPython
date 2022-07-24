"""
Mini Project 1
Library Management System
"""
from abc import ABC, abstractmethod


class Methods(ABC):
    @abstractmethod
    def showbooks(self):
        return 0

    @abstractmethod
    def addbook(self):
        return 0

    @abstractmethod
    def borrow(self):
        return 0

    @abstractmethod
    def returnbookk(self):
        return 0


class Library(Methods):
    lendbook = {}

    def __init__(self, lst, libname):
        self.lst = lst
        self.libname = libname

    def printdetails(self):
        print("\n", end="")
        print("Books Available : ", end="")
        print(", ".join(self.lst))
        print(f"Library name : {self.libname}")

    def showbooks(self):
        print("\n", end="")
        print("Books Available : ", end="")
        print(", ".join(self.lst))

    def addbook(self):
        self.newbook = input("\nEnter book name you want to add : ")
        if self.newbook in self.lst:
            print("Book Already exist in Library")
        else:
            self.lst.append(self.newbook)
            print("Book successfully Added!")

    def borrow(self):
        self.lender = input("\nEnter your name : ")
        self.bookk = input("Enter book name you want to borrow : ")
        if self.bookk not in self.lst:
            print("Book not available in library")
        else:
            if self.bookk in self.lendbook.keys():
                print(f"This book is already borrowed {self.lendbook[self.bookk]}")
            else:
                print(f"Book : '{self.bookk}' is successfully lended to {self.lender}")
                self.lendbook[self.bookk] = self.lender

    def returnbookk(self):
        self.returnbook = input("\nEnter the book name you want to return : ")
        self.lendername = input("Enter the borrower name : ")
        if self.returnbook in self.lendbook.keys():
            if str(self.lendbook[self.returnbook]) == str(self.lendername):
                print("Book successfully returned")
                del self.lendbook[self.returnbook]
            else:
                print("Your name doesnt match with this book borrower")
        else:
            print(f"No book is borrowed named {self.returnbook}")


lst = []
print("**************Welcome to Library Management System**************")
print("Enter all the available books name")
print("Enter Stop to exit\n")
i = 0
while True:
    i += 1
    bookname = input(f"Book{i} : ")
    if bookname == "Stop" or bookname == "stop":
        break
    else:
        if bookname == "":
            continue
        else:
            lst.append(bookname)

rohanlib = Library(lst, "Rohan's Library")
while True:
    print("\n**************Menu**************")
    print("1. Display Books \n2. Lend Book \n3. Add Book \n4. Return Book \n5. Exit")
    n = input("Enter Your Choice(1/2/3/4/5) : ")
    match n:
        case "1":
            rohanlib.showbooks()
        case "2":
            rohanlib.borrow()
        case "3":
            rohanlib.addbook()
        case "4":
            rohanlib.returnbookk()
        case "5":
            break
        case other:
            print("Please enter correct choice")

print("Goodbye!!")