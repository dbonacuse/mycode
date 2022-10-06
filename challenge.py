#!/usr/bin/env python3
""" Bonacuse Industries | Duncan
    print() - concatenate vs print a series of items """

def main():

    # collect string input for name
    name_input = input("Please enter your name: ")
    
    # collect string input for day of week
    day_input = input("Please enter the day of the week: ")

    # print() greeting with day of week
    print("Hello,", name_input +  "!", "Happy",  day_input + "!")

main()
