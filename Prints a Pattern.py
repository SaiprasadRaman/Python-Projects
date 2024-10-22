'''This code belongs to Saiprasad Raman

By submitting this work, I assert that it is my own work and not copied from someone else or from some other source. 
Copied work will be assigned a grade of 0 and be subject to further academic penalties at the discretion of the College.

'''


#This program prints the pattern below
##
# #
#  #
#   #
#    #
#     #
#      #




#Constants defined  
HASH1 = [1]
HASH2 = [1]
SPACE = [0, 1, 2, 3, 4, 5, 6]
print("##") #print the first line of #


for x_count in HASH1:#this iterates through the first #
    hash_output = '' #defining variable
    num = ''    #defining variable
    for x_count2 in HASH2: #This iterates through 2nd #
        hash_output2 = '' # defnining variable
        for x_count3 in SPACE: #This is to iterate through the list to add space between the two hashes
            hash_output3 = '' #defining variable
        for count in range (x_count): #This loops through the first #
            hash_output+='#' #defining value for the output to be printed
        for count2 in range (x_count2): #Loops thorugh the 2nd #
            hash_output2+= '#' #defining value for the output to be printed 
        for count3 in range (x_count3): #Adds space according to the list
            hash_output3+= ' '  #defining value for the output to be printed        
            
            print (hash_output,hash_output3,hash_output2) #Print the output with a space between the hash



