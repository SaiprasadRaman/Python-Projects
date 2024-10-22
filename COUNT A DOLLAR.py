'''This code belongs to Saiprasad Raman

By submitting this work, I assert that it is my own work and not copied from someone else or from some other source. 
Copied work will be assigned a grade of 0 and be subject to further academic penalties at the discretion of the College.

'''



#This program is a game that determines whether player's entered values for cents adds up to 1 Dollar. The player wins if it does!



#Define values for the coins. 
PENNY_VALUE = 1
NICKEL_VALUE = 5
DIME_VALUE = 10
QUARTER_VALUE = 25
PENNIES_IN_DOLLAR = 100




#Take inputs from the user which would be the count for each coin. 
Pennies = int(input("Enter the number of Pennies:"))
Nickels = int(input("Enter the number of Nickels:"))
Dimes = int(input("Enter the number of Dimes:"))
Quarters = int(input("Enter the number of Quarters:"))




#Formulae to calculate the total of cents
Total_cent = Pennies * PENNY_VALUE + Nickels * NICKEL_VALUE + Dimes * DIME_VALUE + Quarters * QUARTER_VALUE #Multiply each coin with its count and add all of them.
Total_dollars = Total_cent / PENNIES_IN_DOLLAR #The total pennies is then divided by 100. 




#Condition to print the result as per the calculation
if Total_dollars > 1:
    Result = "\n\n\t\t\t\tSorry, the amount you entered was more than one dollar.\n\n"
elif Total_dollars < 1:
    Result = "\n\n\t\t\t\tSorry, the amount you entered was less than one dollar.\n\n"
else:
    Result = '''                    
                                      
                              Congratulations!    

                The amount you entered was exactly one dollar!

                             You win the game!


                '''
    
print(Result)