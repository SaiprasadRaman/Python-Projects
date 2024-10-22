'''This code belongs to Saiprasad Raman

By submitting this work, I assert that it is my own work and not copied from someone else or from some other source. 
Copied work will be assigned a grade of 0 and be subject to further academic penalties at the discretion of the College.

'''



#This program takes month, day and year as input from the user and displays the date. 



#Take inputs from the user for the month, day and year in 2 digits. 
month = int(input("Enter the month in the numeric form: "))
day = int(input("Enter the day in numeric form: "))
year = input("Enter the year in two numeric digits: ")


#This condition checks whether the month is not more than 12, all the inputs are 2 digits, and the days in the month of february is below 29. If all conditions are met it displays the date otherwise gives an error.  
if month > 12:
    print ("Error: Invalid Month Input")
    print ("There is no such date in the calender")     
elif month == 2 and day > 29:     
    print ("Error: Invalid day Input")
    print ("There is no such date in the calender")
elif ((month == 4 or 6 or 7 or 9 or 11) and day > 30):
    print ("Error: Invalid day Input")
    print ("There is no such date in the calender")
elif day > 31:
    print("Error: Invalid day input")
    print ("There is no such date in the calender")
elif (month == str(month) and len(month)) > 2:
    print ("Error: Invalid Month Input")
    print ("There is no such date in the calender")
elif (day == str(day) and len(day)) > 2:
    print ("Error: Invalid day Input")
    print ("There is no such date in the calender")
elif len(year) > 2:
    print ("Error: Invalid Year Input")
    print ("There is no such date in the calender")
else:
    print("Success! You entered the correct date.")
    print (month,"/",day,"/",year)
    

