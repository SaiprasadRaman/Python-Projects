
'''This code belongs to Saiprasad Raman

By submitting this work, I assert that it is my own work and not copied from someone else or from some other source. 
Copied work will be assigned a grade of 0 and be subject to further academic penalties at the discretion of the College.

'''



#This program takes the current salary in German currency and a country to migrate to as inputs from the user and displays whether the user would be poor or rich in their country of choice. 



#Take input from user for salary and the county to migrate to
salary_german = float(input("Please enter your salary in German currency (euros): "))
country_migrate = input("Enter the country you want to migrate to between Canada, USA, Cambodia and United Kingdom: " )

#This function converts the german salary into its equivalence in different countries  
def convertSalary():
    global salary_canadian
    global salary_usa
    global salary_cambodia
    global salary_uk

    salary_canadian = salary_german * 1.51
    salary_usa = salary_german * 1.12
    salary_cambodia = salary_german * 4529
    salary_uk = salary_german * 0.84        
convertSalary()

#This is the function to display the result in Canada
def Canada():    
    if salary_canadian < 56000:
        print("You'll be poor in Canada with a salary of $", round(salary_canadian,1))
    else:
        print("You'll be rich in Canada with a salary of $", round(salary_canadian,1))
        

#This is the function to display the result in USA
def Usa():    
    if salary_usa < 45000:
        print("You'll be poor in USA with a salary of $", round(salary_usa,1))
    else:
        print("You'll be rich in USA with a salary of $", round(salary_usa,1))
  

#This is the function to display the result in Cambodia
def Cambodia():   
    if salary_cambodia < 7649856:
        print("You'll be poor in Cambodia with a salary of KHR", round(salary_cambodia,1))
    else:
        print("You'll be rich in Cambodia with a salary of KHR", round(salary_cambodia,1))

    

#This is the function to display the result in UK
def Uk():   
    if salary_uk < 45423:
        print("You'll be poor in United Kingdom with a salary of pound",  round(salary_uk,1))
    else:
        print("You'll be rich in United Kingdom with a salary of pound",  round(salary_uk,1))

   

#This condition checks the inputs from the user and based on their choice of country calls the function above to display the result
if country_migrate == 'Canada' or country_migrate == 'canada' or country_migrate == 'CANADA': 
    Canada()
elif country_migrate == 'Usa' or country_migrate == 'usa' or country_migrate == 'USA' or country_migrate == 'us' or country_migrate == 'US' or country_migrate == 'Us': 
    Usa()
elif country_migrate == 'Cambodia' or country_migrate == 'cambodia': 
    Cambodia()
elif country_migrate == 'United Kingdom' or country_migrate == 'united kingdom' or country_migrate == 'UK' or country_migrate == 'Uk' or country_migrate == 'uk': 
    Uk()
else:
    print("Please enter either Canada, Usa, Cambodia or United Kingdom")  



    
    