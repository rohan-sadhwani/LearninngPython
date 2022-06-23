n = 35
guess = 3
attempt = 0
print("Welcome to guess the number game")
print("You will get 3 chances to guess the number\n")

while guess >= 1:
    num = int(input("Please enter number to guess : "))
    if num == n:
        attempt = attempt + 1
        print("Correct Ans. The number is :", n)
        print("You guessed the ans in ", attempt, "attempt")
        break
    else:
        guess = guess - 1
        if guess == 0:
            print("Game Over! You Failed")
            print("The correct Ans was :", n)
        else:
            if n > num:
                print("Wrong! The number is greater than ", n)
                print(guess, "attempts remaining\n")
                attempt = attempt + 1
            else:
                print("Wrong! The number is less than ", n)
                print(guess, "attempts remaining\n")
                attempt = attempt + 1
