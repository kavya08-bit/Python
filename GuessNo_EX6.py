import random

lowest_num=1
higest_num=100
answer =random.randint(lowest_num,higest_num)
guesses =0
is_running = True

print("Python num guess game")
print(f"Select the number between {lowest_num} and {higest_num}")

while is_running:
    guess = input("enter your guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses +=1

        if guess < lowest_num or guess > higest_num:
            print("that guess is out of range")
            print(f"Select the number between {lowest_num} and {higest_num}")
        elif guess < answer:
            print("too low!")
        elif guess > answer:
            print("Too High! try again")
        else:
            print(f"Correct! the answer was {answer}")
            print(f"number of guesses{guesses}")
            is_running = False
    else:
        print("invalid guess")
        print(f"Select the number between {lowest_num} and {higest_num}")
