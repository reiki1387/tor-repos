import sys

from random import randint

random_number = randint(int(sys.argv[1]), int(sys.argv[2]))

while True:
    try:
        number = int(
            input(f'Please choose a number between {sys.argv[1]} and {sys.argv[2]}:  '))
        if number >= int(sys.argv[1]) and number <= int(sys.argv[2]):
            if number == random_number:
                print("You're a genius!")
                break
        else: 
            print("That's outside of the range! Enter again")
            continue
    except ValueError:
        print("That is not a number! Please enter a number")
        continue