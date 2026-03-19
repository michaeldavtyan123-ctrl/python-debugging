#! /usr/bin/env python3

import sys

def area_of_rectangle(height, width=None):
    # Fix 1: Only set width to height if width is NOT provided
    if width is None:
        width = height
    return height * width

if __name__ == '__main__':
    # Fix 2: Check for 2 or 3 total items (Script name + 1 or 2 numbers)
    if not (2 <= len(sys.argv) <= 3):
        message = ("{n}: Use 1 arg for square or 2 for rectangle.".format(n=sys.argv[0]))
        sys.exit(message)

    try:
        # Fix 3: Convert strings to floats
        height = float(sys.argv[1])
        
        if len(sys.argv) == 3:
            width = float(sys.argv[2])
        else:
            width = None

        area = area_of_rectangle(height, width)
        
        # Determine what to print for the message
        w_display = width if width is not None else height
        print("The area of a {h} X {w} rectangle is {a}".format(h=height, w=w_display, a=area))
        
    except ValueError:
        sys.exit("Error: Please provide numbers only.")
