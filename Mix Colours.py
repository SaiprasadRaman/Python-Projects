'''This code belongs to Saiprasad Raman

By submitting this work, I assert that it is my own work and not copied from someone else or from some other source. 
Copied work will be assigned a grade of 0 and be subject to further academic penalties at the discretion of the College.

'''


#This program takes two colours as input from the user and displays the mixed colour as output 



#These are the constants defined
RED = "red"
BLUE = "blue"
YELLOW = "yellow"

#We take input from the user for their choice of colour
colour1 = input("Enter the first primary colour in lower case letters: ")
colour2 = input("Enter the second primary colour in lower case letters: ")

#This condition uses the 1st and 2nd input from the user and displays the result  when both the colours are mixed or returns an error if the colour is not the ones defined as constants. 
if colour1 == RED:
    if colour2 == BLUE:
        print ("The colours when mixed produces Purple")
    elif colour2 == YELLOW:
        print ("The colours when mixed produces Orange")
    elif colour1 != RED and BLUE and YELLOW:
        print ("Error: Invalid Colour 1")
    elif colour2 != RED and BLUE and YELLOW:
        print ("Error: Invalid Colour 2")

if colour1 == BLUE:
    if colour2 == RED:
        print ("The colours when mixed produces Purple")
    elif colour2 == YELLOW:
        print ("The colours when mixed produces Green")

if colour1 == YELLOW:
    if colour2 == RED:
        print ("The colours when mixed produces Orange")
    elif colour2 == BLUE:
        print ("The colours when mixed produces Green")
