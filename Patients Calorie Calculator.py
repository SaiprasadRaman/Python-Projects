'''This code belongs to Saiprasad Raman

By submitting this work, I assert that it is my own work and not copied from someone else or from some other source. 
Copied work will be assigned a grade of 0 and be subject to further academic penalties at the discretion of the College.

'''



#This program calculates the decrease in patients calories within the specified number of days



#Take inputs from the user
def Take_inputs():
    global calories_intake
    global calorie_decrease_percentage
    global number_of_days
    
    calories_intake = float(input("Enter the daily calorie intake: "))
    calorie_decrease_percentage = float(input("Enter the average daily calorie decrease in percentage: "))
    number_of_days = int(input("Enter the number of days: ")) 

Take_inputs()

 #Check if the user enters a positive digit number
def Positive_number_checker():
    Take_inputs()
    day = 1
    if day == day + 1:
        calories_intake = calories_intake + 1
    if (calories_intake)  < 0:
        print("Please enter a positive digit number.")       


#Calculate the daily calorie reduction as the percentage entered in Take_inputs() 
def Calorie_calculator():

    Take_inputs()
for days in range(number_of_days):     
    calories_intake -= (calorie_decrease_percentage/100)*calories_intake    
    print("Calories Reduced: ",days, round(calories_intake,1))
    if int(calories_intake) < 1200:
        print("Diet stabilised")
        break
    








