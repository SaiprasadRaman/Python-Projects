'''This code belongs to Saiprasad Raman

By submitting this work, I assert that it is my own work and not copied from someone else or from some other source. 
Copied work will be assigned a grade of 0 and be subject to further academic penalties at the discretion of the College.
'''



#This program is an example of a shopping cart. 



#Initialize a blank dictionary for the shopping carts
shopping_Cart = {}

#Function for the main menu
def User_choice():
    print(('''

                    *****   WELCOME TO THE AMANDO SHOPPING SITE   *****
                        
                            1. Add a product to the cart
                            2. Search for a product 
                            3. Delete a product from the cart
                            4. Display the contents the cart
                            5. Purchase items
                            6. Quit
        '''                        
        ))




#Function to add products to the cart
def Add_product():

    if len(shopping_Cart) >= 5: #This condition checks whether the products in the cart has gone above 5
            print("Cart is full.") #prints cart is full if it reaches 5
            return       #returns the value of shopping cart
    
    while True: # Condition to check if products can be added. If not then go back to the main menu
    
        add_option = input("Would you like to add products to your cart? Y/N : ")  #Takes input from the user to add more items to the cart
        

        if add_option in ['Y','y']:    #If the user enters Y or y it asks for the product to be added
         
            product_name = input("Enter the product name: ")           #Takes product name as input
            product_price = float(input("Enter the product price in $: "))   #Takes product price as input
            product_brand = input("Enter the product brand name: ")     #Takes product brand as input
            
            shopping_Cart[product_name] = {            #This statement adds the product taken as input above to the shopping_Cart dictionary for example: Smartphone : {
                'product-price-details': product_price,                                                                                                     # product-price : 1000
                'product-brand-details': product_brand                                                                                                      # product-brand : Apple}
            }

        elif add_option in ['N','n']: #If the user enters N or n it goes out of the loop
            break    #Comes out of the while loop




#Function to search for a product in the dictionary
def Search():
    product_name = input("Enter the product name to search: ") #takes input from the user to search a product 
    if product_name in shopping_Cart:     #This condition checks whether the product is in the shopping_Cart dictionary
        product_details = shopping_Cart[product_name]  #if the product is available it will find the product name and puts the item,key and values to product_details variable
        print(f"Product found: {product_name}, Price: ${product_details['product-price-details']}, Brand: {product_details['product-brand-details']}") #This statement prints the found product along with its price and brand values using the product_details variable.  
    else:
        print("No product exists with this name.") #This displays product unavailable if it is not present in the shopping_cart dictionary.




#Function to delete a product from the dictionary
def Delete():        
    if len(shopping_Cart) == 0: #This condition checks whether there is any product in the shopping_cart dictionary
            print("Cart is empty, no item is found.") #print as empty cart if the cart is empty
            return #returns the value of shopping cart
    else:
        Display()
    product_name = input("\n\nEnter the product name to delete: ") #Asks the user to input the product to delete from the shopping_cart dictionary
    if product_name in shopping_Cart:   #Checks whether the product name is present in the shopping_cart dictionary
        del shopping_Cart[product_name]   #if the condition finds the product, this statement deletes it. 
        print(f"Deleted {product_name} from the cart.") #This displays the deleted product 
    else:
        print("Product not found in cart.") #this prints if the product is not present in the shopping_Cart dictionary

    


#Function to display the dictionary
def Display():
   
    if len(shopping_Cart) == 0: #This condition checks whether the product is present in the shopping cart.  
        print("Cart is empty.") #If no product is present, it will print as empty cart
    else:
        print("\nContents of the cart:") 
        for product_name, product_details in shopping_Cart.items(): #This forloop will run through the no. of items in the dictionary
            print(f"Product: {product_name}, Price: ${product_details['product-price-details']}, Brand: {product_details['product-brand-details']}") #This prints the product from the dictionary along with its brand and price




#Function to purchase items from the shpopping cart
def Purchase_items():
   
    if len(shopping_Cart) == 0: #Checks whether the shopping_Cart dictionary is empty 
            print("Cart is empty, please select an item before completing purchase.") #if empty dictionary it prints this statement
            return #returns the value of shopping cart
    
    total_price = sum(product_details['product-price-details'] for product_details in shopping_Cart.values()) #Adds the prices of all the products present in the shopping cart using a for loop
    print(f"Total price of items in the cart: ${total_price}") #prints the total price of the shopping cart
    
    while True: #Use while loop to run through the conditions if True and come out of the if condition if it is Untrue 
        purchase_confirmation = input("Complete purchase (Y/N)? ") #Takes the input from the user if they would like to purchase the products
        if purchase_confirmation in ['Y', 'y']: #if condition for the y input received
            print("Thank you for your business.") #prints if Y is the input
            shopping_Cart.clear()  # Empties the shopping_cart dictionary
            break #comes out of the if condition 
        elif purchase_confirmation in ['N', 'n']: #if condition for n input 
            print("Please continue shopping.") 
            break #comes out of the if condition
        else:
            print("Please enter either Y or N.") #asks the user to enter either y or n if they enter something other than that
    
    






def Main_loop():
    while True: #This while loop is to run through each function and come back to the main menu after completing the function
  
        User_choice() #calls the User_choice function
        user_choice = input("Select an option (1-6): ") #asks the user for the input
            
        if user_choice == '1': #if condition for input = 1
            Add_product() #calls the functions respectively
            
        elif user_choice == '2' :
            Search()
        elif user_choice == '3' :
            Delete()
        elif user_choice == '4' :
            Display()
        elif user_choice == '5' :
            Purchase_items()
        elif user_choice == '6' :
            break #Comes out of the while loop when user chooses the 6 as their choice 
        else:
            print("Invalid choice. Please select a valid option.") #prints as invalid if it is not one of the choises listed in the main menu

Main_loop()