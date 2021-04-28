#!/usr/bin/env python3

# Created by: Youngjun Kim
# Created on: April 2021
# This program calculates the volume of a cone
#    with radius and height inputted from the user

import math


def main():
    # this function calculates the volume of a cone

    # main function
    print("We will be calculating the area of a cone. ")

    # input
    radius_of_cone = int(input("Enter radius of a cone (mm): "))
    height_of_cone = int(input("Enter height of a cone (mm): "))

    # process
    volume_of_cone = 1/3 * math.pi * radius_of_cone * radius_of_cone * height_of_cone

    # output
    print("")
    print("Volume is {0} mm³.".format(volume_of_cone))
    print("")
    print("Done.")


if __name__ == "__main__":
    main()
