import random
def guess_number():
    number=random.randint(1,50)
    attempt=10
    print("Welcome to the Number Guessing Game1")
    name=input("Enter your name: ")
    print("You have 10 attempts to guess the number between 1 and 50.")
    while attempt>0:
        guess_number=int(input('Guess your number:'))
        if guess_number<number:
            print("your guess number is low")
        elif guess_number>number:
            print("your guess number is high")
        else:
            print(f"Congratulations! {name} guessed the number correctly.")
            break
        attempt-=1
        print(f'you have {attempt} attempts left')
    if attempt==0:
        print(f'Sorry, {name} have used all your attempts. The correct number was {number}.')
guess_number()