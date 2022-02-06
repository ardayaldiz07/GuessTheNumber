import random
import time

print("""
Guess numbers from 1 to 40.
""")

randomnumber = random.randint(1, 40)
chance_value = 7

while True:
    guess = int(input("What is your estimate?: "))

    if (guess < randomnumber):
        print("Checking...")
        time.sleep(1)
        chance_value -= 1
        print(f"Please enter a larger number...\nRemaining right = {chance_value}")
    elif (guess > randomnumber):
        print("Checking...")
        time.sleep(1)
        chance_value -= 1
        print(f"Please enter a smaller number...\nRemaining right = {chance_value}")
    else:
        print("Correct!!!")
        tryagain = input("Enter 'R' to try again and 'Q' to exit: ")
        if tryagain.lower() == "r":
            chance_value = 7
            continue
        if tryagain.lower() == "q":
            print("Exiting the program...")
            break
    if chance_value <= 0:
        print(
            f"Unfortunately, your rights are completely gone.\nCorrect answer = {randomnumber}")
        failure = input("Enter 'R' to try again and 'Q' to exit: ")
        if failure.lower() == "r":
            chance_value = 7
            continue
        if failure.lower() == "q":
            print("Exiting the program...")
            break
