#!/usr/bin/env python3

# Created by: Felipe Garcia Affonso
# Created on: May 2021
# This program converts the schoolboard grade sistem to porcentage

import math


def grade_converter(level):
    # this function converts the schoolboard grade sistem to porcentage
    if level == "4+":
        porcentage = 98
    elif level == "4":
        porcentage = 90
    elif level == "4-":
        porcentage = 83
    elif level == "3+":
        porcentage = 78
    elif level == "3":
        porcentage = 75
    elif level == "3-":
        porcentage = 71
    elif level == "2+":
        porcentage = 68
    elif level == "2":
        porcentage = 65
    elif level == "2-":
        porcentage = 61
    elif level == "1+":
        porcentage = 58
    elif level == "1":
        porcentage = 55
    elif level == "1-":
        porcentage = 51
    elif level == "R":
        porcentage = 25
    else:
        porcentage = -1

    return porcentage


def main():
    # Is the main function
    grade_in_level = input("Enter your mark: ")

    grade_in_porcentage = grade_converter(grade_in_level)

    if grade_in_porcentage > 0:
        print("You got {}%".format(grade_in_porcentage))
    else:
        print("Invalid input, please insert a level.")

    print("\nDone.")


if __name__ == "__main__":
    main()
