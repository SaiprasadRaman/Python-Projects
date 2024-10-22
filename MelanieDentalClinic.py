'''This code belongs to Saiprasad Raman

By submitting this work, I assert that it is my own work and not copied from someone else or from some other source. 
Copied work will be assigned a grade of 0 and be subject to further academic penalties at the discretion of the College.

'''



#This program is to calculate the medical report according to the inputs received. 



#Import math for calculation and import datetime from datetime to calculate the date. 
import math
from datetime import datetime



#Enter inputs for the patient's details
print('\n\t\t\t\tMelanie Dental Clinic\n')
Patient_name = input("1. Patient's name:")
Former_patient = str(input("2. Has the patient been here before? (y/n):"))
Patient_height = int(input("3. What is the patient's height (in cm)?:"))
Patient_weight = float(input("4. What is the patient's weight (in kg)?:"))
Last_weighed = input("5. When was the patient last weighed in (1/1/2000 if never weighed)? (in mm/dd/yyyy):")
Last_weighed_weight = float(input ("6. What was the patient's weight (in kg, -1 if never weighed)?:"))
Practitioner_assessment = int(input("7. Practitioner's overall assessment of the patient's health (-5=very poor to +5=excellent, 0 for neutral)"))




#This equation is to calculate the initial Bmi of the patient
Bmi = float((Patient_weight/(Patient_height**2))*10000)
round(Bmi, 1) #Rounds the value of Bmi to 1 decimal point




#Conditional statement to determine the conclusion of Bmi score.
#We compare the Bmi to determine the state of patient's health
#The patient is given a health score
if Bmi > 30: 
    Intermediate_health_score = 0
    Obese = 0
    Bmi_conclusion = 'Patient is Obese.'
elif Bmi >= 25 <= 29.9:
    Intermediate_health_score = 3
    Overweight = 3
    Bmi_conclusion = 'Patient is Overweight.'
elif Bmi >= 18.5 <= 24.9:
    Intermediate_health_score = 5
    Healthy = 5
    Bmi_conclusion = 'Patient is healthy.' 
elif Bmi >= 17 <= 18.4:
    Intermediate_health_score = 3
    Underweight = 3
    Bmi_conclusion =  'Patient is underweight.'
else:
    Intermediate_health_score = 0
    Too_thin = 0
    Bmi_conclusion =  'Patient is too thin.' 




#The health score is increased or decreased based on changes in the patient's weight since last visit. 
if Last_weighed_weight == "-1":
    Intermediate_health_score = Intermediate_health_score + 1
elif Last_weighed_weight == +1 or -1:
    Intermediate_health_score = Intermediate_health_score - 1
elif Underweight - 1:
    Intermediate_health_score = Intermediate_health_score - 3
elif Underweight + 1:
    Intermediate_health_score = Intermediate_health_score + 2
elif Too_thin - 1:
    Intermediate_health_score = Intermediate_health_score - 5
elif Too_thin + 1:
    Intermediate_health_score = Intermediate_health_score + 5
elif Overweight + 1:
    Intermediate_health_score = Intermediate_health_score - 3
elif Overweight - 1:
    Intermediate_health_score = Intermediate_health_score + 2
elif Obese + 1:
    Intermediate_health_score = Intermediate_health_score - 5
elif Obese - 1:
    Intermediate_health_score = Intermediate_health_score + 5

Intermediate_health_score = Intermediate_health_score + (Practitioner_assessment) # The patient's health score is then added to the Practitioner's initial assessment.




#The Final Health Score calculated above is then given a description.  
if Intermediate_health_score > 5:
    Final_score = 'Great Condition!'
elif Intermediate_health_score >= 3 <= 5:
    Final_score = 'Need a little work'
elif Intermediate_health_score >= 1 <= 3:
    Final_score = 'Need a lot of work'
elif Intermediate_health_score < 1:
    Final_score = 'At risk!'




#Using the datetime module we can convert the string value of date into the date format.  
Date_format = '%m/%d/%Y'
Last_weighed_date = datetime.strptime(Last_weighed, Date_format)#convert string into the date format of mm/dd/yyyy
Today = datetime.now() #Assign today's date to a variable




#This condition is to calculate the days since the patient's last visit.
if Last_weighed == "1/1/2000":
    Days_since_visit =  0
else:
    Days_since_visit = Today - Last_weighed_date




#This condition is to calculate whether the patient had a weight loss or patient gained weight since their last visit
if Last_weighed_weight < Patient_weight:
    Patient_weight_loss = 'Gained weight by ' + str(Patient_weight - Last_weighed_weight) + ' kg'    
elif Last_weighed_weight > Patient_weight:
    Patient_weight_loss = 'Lost weight by ' + str(Last_weighed_weight - Patient_weight) + ' kg'
else:
    Patient_weight_loss = 'No change'
   



#This conditional statement is to print a report according to whether the patient is a former or new. 
if Former_patient == "y":

    print (f'''
           



                                                                          Melanie Diet Clinic
                                                                      *------------------------*
                                                        
                                                        Receipt for patient name: {Patient_name}
                                                                  Patient Weight: {Patient_weight} kg
                                                             Patient weight loss: {Patient_weight_loss}
                                                           Days since last visit: {Days_since_visit}
                                                    ------------------------------------------------------------------       
                                                                             Bmi: {Bmi_conclusion}
                                                                          Health: {Practitioner_assessment}
                                                             -----------------------------------------------
                                                                         Overall: {Final_score}     





        ''')

else:

    print (f'''
           



                                                                            Melanie Diet Clinic
                                                                        *------------------------*
                                                                
                                                            Receipt for patient name: {Patient_name}
                                                                      Patient Weight: {Patient_weight} kg
                                                                         Patient New: Yes
                                                                         First Visit: {Today}
                                                        -------------------------------------------------------------------        
                                                                                 Bmi: {Bmi_conclusion}
                                                                              Health: {Practitioner_assessment}
                                                            -----------------------------------------------------
                                                                             Overall: {Final_score}        




        ''')




