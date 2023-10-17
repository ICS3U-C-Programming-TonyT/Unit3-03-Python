#!/usr/bin/env python3
# Created By: Tony Tran
# Date: Oct. 11, 2023
# This is program will generate a random number and you'll have to guess it.


from random import randint


def main():
    guess = int(input("Give me a number 0 - 9:\n"))
    random_number = randint(0, 9)

    if guess == random_number:
        print(f"Correct the number is {random_number}")
    else:
        print(f"Wrong it was {random_number}")


if __name__ == "__main__":
    main()
