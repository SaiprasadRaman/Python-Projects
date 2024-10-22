
'''This code belongs to Saiprasad Raman

By submitting this work, I assert that it is my own work and not copied from someone else or from some other source. 
Copied work will be assigned a grade of 0 and be subject to further academic penalties at the discretion of the College.

'''



#This is a program to manage a phone directory 

 

#Initializing an empty dictionary
phoneDirectory = {}

#Function to display the menu
def Menu():
    print ('''
           
           
           WELCOME TO THE GRANN'S PHONE DIRECTORY
           1. Add a record
           2. Search a record
           3. Update a record
           4. Sort the record alphabetically
           5. Delete a record
           6. Quit
           
           
           ''')


#Function to add a record 
def Add_record():

    while True:                                                 #We use while loop to use an if statement under it and get back to the while loop for any wrong conditions
        Contact_name = input("Enter name: ")                        #Takes user's input on the records to be stored
        Contact_number = input("Enter your 10-digit phone number: ")
        
        if len(Contact_number) > 10:                            #Condition to check if the phone number is greater than 10 digit
            print("Please enter a valid 10 digit number")       
            return                                              #returns the value of Contact_number
        phoneDirectory [Contact_name] = Contact_number          #stores the value of contact_name and contact_number as a key and value pair. 
        break
    

#Function to search a record in the dictionary
def Search_record():                
    Contact_name = input("Enter name to search: ")              #Asks input from the user    
    
    if Contact_name in phoneDirectory:                          #checks if the contact_name exists in the dictionary
            Contact_number = phoneDirectory[Contact_name]       #combines value of the Contact_name which is the key to the Contact_number
            print(f"{Contact_name} : {Contact_number}")         #prints Contact name and contact number of the search name
    else:                               
        print("No record exists")                               #prints in case of unrecognized name
    

#Function to update a record in the dictionary
def Update_record():
    Contact_name = input("Enter name: ")                        #Takes input from the user
    Contact_number = input("Enter new 10-digit phone number: ") #asks for a new contact_number
    phoneDirectory.update({Contact_name:Contact_number})        #replaces the old contact number with a new contact number
    print("Record updated")                                     #prints once completed


#Function to sort the records in an alphabetical order
def Sort_record():    
    dict_keys = list(phoneDirectory.keys())                     #stores the keys of all the contacts i.e. contact_name in a variable
    dict_keys.sort()                                            #sorts the keys in an alphabetical order
    sorted_dict = {i:phoneDirectory[i] for i in dict_keys}      #stores the Contact_name and Contact_number in a variable

    #Using the replace function to remove the special characters
    special_characters = ['\'','{','}']                         #stores the special characters in a variable
    sorted_without_char = str(sorted_dict)                      #converts the sorted text from a list into a str for its special characters to be considered as a str 
    for j in special_characters:                                #forloop to run through the special characters list
        sorted_without_char=sorted_without_char.replace(j,"")   #replace the special characters     

    print("Sorted Record is: ",sorted_without_char)             #print the new text


#Function to delete a record from the dictionary
def Delete_record():
    if len(phoneDirectory) == 0:                                #checks if the length of the dictionary is 0
        print("Phone directory is empty")                       #prints as empty if the len is 0
        return                                                  #returns the value of the phone directory
    else:
        Contact_name = input("Enter name: ")                    #Asks input from the user for the contact name 
        if Contact_name in phoneDirectory:                      #checks if the contact_name is present in the dictionary
            del phoneDirectory[Contact_name]                    #deletes the contact if the above condition is true
            print("Record deleted")                             #prints record deleted
        else:
            print("Record not found")                           


#Funtion to call all other functions as per user's choice
def Main_loop():

    while True:                                                 #while loop is used so that we can use if statement underneath it which comes back to the while loop if the condition is false
        Menu()                                                  #calls Menu() function
        user_choice = input("Enter your choice: ")              #Asks user to input their choice

        if user_choice == '1':                                  #Condition to check if the input is 1
            Add_record()                                        #calls Add_record() function
        elif user_choice == '2':                                #Condition to check if the input is 2
            Search_record()                                     #calls Search_record() function
        elif user_choice == '3':                                #Condition to check if the input is 3
            Update_record()                                     #calls Update_record() function
        elif user_choice == '4':                                #Condition to check if the input is 4
            Sort_record()                                       #calls Sort_record() function
        elif user_choice == '5':                                #Condition to check if the input is 5
            Delete_record()                                     #calls Delete_record() function
        elif user_choice == '6':                                #Condition to check if the input is 6
            break
        else:
            print("Enter a valid option")                       #prints if the user enters an invalid option

Main_loop()                                                     #Runs the main_loop() function
