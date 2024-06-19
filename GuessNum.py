import random

def guess(x):
    random_number = random.randint(0,x)
    guessed = 0
    while guessed != random_number:
        guessed = int(input("Guess the number"))
        if guessed > random_number:
            print("your guess is greater than the number")
        elif guessed < random_number :
            print("your guess is greater than the number")

    print (f'yayyy correct number {random_number}')

def computer_guess(x):
    feedback = ''
    low = 0
    high = x
    while feedback != 'c':
        guess = int(random.randint(low, high))
        print(guess)
        feedback = input("(L)Low (H)high (C) correct".lower())
        if feedback == 'l':
            low = guess+1
            guess = input("enter number")
        if feedback == 'h':
            high = guess-1
            guess = input("enter number")



computer_guess(10)

