from random import randint

x = randint(1,9)
guess = -1

print("Guess the number below 10:")
while guess != x:
    guess = int(input("Guess: "))

    if guess != x:
        print("Wrong guess")
    else:
        print("Guessed correctly")
