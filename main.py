import random

secret_number = random.randint(1, 100)
attempt = 0
while True:
    guess_number = int(input("Guess a number between <1,100>  "))
    attempt += 1
    
    if guess_number > secret_number:
        print("GUESS LOWER")
    elif guess_number < secret_number:
        print("GUESS HIGHER")
    else:
        print(f"LESSGOO!!!CONGRATULATIONS!!! you got it in {attempt} attempts ")
        break
