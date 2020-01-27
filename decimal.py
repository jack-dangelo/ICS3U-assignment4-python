#!/usr/bin//env python3

# Created by: Jack D'Angelo
# Created on: January 2020
# This is program compares 2 numbers with up to 3 decimal places


def main():
    # This functions compares 2 numbers
    print("The program compares two numbers")
    print("")

    # Input
    num_1 = input("Number 1: ")
    num_2 = input("Number 2: ")
    # Process

    try:
        float_1 = float(num_1)
        float_2 = float(num_2)

        float_1b = round(float_1, 3)
        float_2b = round(float_2, 3)
        # Compares the numbers that were rounded

        if float_1b == float_2b:
            print("These numbers are the same up to three decimal places.")
        elif float_1b > float_2b:
            print("{} is the larger of the two numbers".format(float_1))
        elif float_1b < float_2b:
            print("{} is the larger of the two numbers".format(float_2))
        else:
            print("Please enter a valid number")

    except Exception:
        print("Error")


if __name__ == "__main__":
    main()
