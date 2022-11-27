#!/usr/bin/env python3

# Created By: Patrice Pat-Odita
# Date: Nov 24, 2022
# This program Calculates the area of a triangle
# Using base and area gotten from the user.

# calculates the area of the triangle with the inputted base and height
def calculate_area(base_int, height_int):
    area = (base_int * height_int) / 2
    print("The area of your triangle is {}cm^2".format(area))


def main():
    # gets user input
    base = input("What is the base length of your triangle in cm: ")
    height = input("What is the height of your triangle in cm: ")
    try:
        # converts to floats
        height_int = float(height)
        base_int = float(base)
        # only calls the function if the variables are positive
        if (base_int > 0) and (height_int > 0):
            # calls the function with the arguments base_int and height_int
            calculate_area(base_int, height_int)
        else:
            print("Please enter a positive number")
    except ValueError:
        print("Invalid input")


if __name__ == "__main__":
    main()
