'''This code belongs to Saiprasad Raman

By submitting this work, I assert that it is my own work and not copied from someone else or from some other source. 
Copied work will be assigned a grade of 0 and be subject to further academic penalties at the discretion of the College.

'''



#In this program we take two numbers from the user and ask them to choose an operator for the calculation and display the result as per the chosen operator. 




def takeInput(): #Function to take inputs
    
    #Define global variables for it to be used in the another function
    global First_number
    global Second_number
    global Operator

    #Take inputs from the user
    First_number = int(input("What is your first number:"))    
    Second_number = int(input("What is your second number:"))    
    Operator = input("What mathematical calculation would you like to perform (+,-,*,/):")

takeInput()




def displayResult(): #Function to perform calculations
    
    #Condition for performing operations
    if Operator == "+":
        Ans = First_number + Second_number
    elif Operator == "-":
        Ans = First_number - Second_number
    elif Operator == "*":
        Ans = First_number * Second_number
    elif Operator == "/":
        Ans = First_number / Second_number    
    return Ans




print ('Answer:',displayResult()) #Print the Output

