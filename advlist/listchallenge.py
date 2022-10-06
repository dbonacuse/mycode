#!/usr/bin/env python3
  

"""Bonacuse Industries | Duncan
   List - simple list"""

import random

def main():
    wordbank = ["indentation", "spaces"]

    tlgstudents= ["Aaron", "Andy", "Asif", "Brent", "Cedric", "Chris", "Cory",
                "Ebrima", "Franco", "Greg", "Hoon", "Joey", "Jordan",
                "JC", "LB", "Mabel", "Shon", "Pat", "Zach"]

    print(tlgstudents)

    # append integer 4 to wordbank list
    wordbank.append(4)

    print(wordbank)

    # input for asking for number between 0 and 18, save as variable num
    num = int( input("Please enter a number between 0 and 18: "))
    name = tlgstudents[num]

    print(f"The random student you chose is {name}!")

    #  print <student_name> always uses <4> <spaces> to indent
    print(f"{name} always uses {wordbank[2]} {wordbank[1]} to indent.")

    name = random.choice(tlgstudents)
    print(f"{name}")

main()
