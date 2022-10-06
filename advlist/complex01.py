#!/usr/bin/env python3


"""Bonacuse Industries | Duncan
   List - simple list"""

def main():
    # create a list called list1
    list1 = ["cisco_nxos", "arista_eos", "cisco_ios"]

    # display list1
    print(list1)

     # display list1[1] which should only display arista_eos
    print(list1[1])
    
    # create new list containing single item
    list2 = ["juniper"]

    # extend list1 by list2 and combine them
    list1.extend(list2)

    # display list1 (now contains juniper)
    print(list1)

    # create list3
    list3 = ["10.1.0.1", "10.2.0.1", "10.3.0.1"]
    
    # append list1 by list3
    list1.append(list3)

    # display new complex list1
    print(list1)

    # display item 5 of list1, the set of IP addresses
    print(list1[4])

    # display the first IP address
    print(list1[4][0])
    
    # create animal list and print it, separated by space
    animals = ["fly", "bee", "cat", "dog", "cow"]
    print(' '.join(animals))
    
    wordbank = ["indentation", "spaces"]

    tlgstudents= ["Aaron", "Andy", "Asif", "Brent", "Cedric", "Chris", "Cory", "Ebrima", "Franco", "Greg", "Hoon", "Joey", "Jordan", "JC", "LB", "Mabel", "Shon", "Pat", "Zach"]

    # append integer 4 to wordbank list
    wordbank.append(4)

    # input for asking for number between 0 and 18, save as variable num
    number_input  = input("Please enter a number between 0 and 18: ", number_input)
    num = str(number_input)

    # use num to slice elements from tlgstudents list, save as student_name
    student_name = tlgstudents[num(choice)]

    # print <student_name> always uses <4> <spaces> to indent
    print(f"{student_name} always uses {wordbank[2]} {wordbank[1]} to indent.")

main()

