
# print("Hello World") 
# print(""" A Hello world! program is generally
#        a computer program that outputs or
#        displays the message Hello World """)

#this is comment hhhhhh vkhkjhkj

"""
this is multiline comment
"""

# movie_title = "Captain Marvel"
# release_year = 2019
# rating = 7.9
# is_general_audiences= False
# print(movie_title)

# top_up_amount = 50 #great top up value
# count = 3 #how many times to top up
# discount= 2 #big discount

# #get total payment
# total_payment = top_up_amount * count
# print(total_payment)

# #total payment after discount
# total_discount = discount * 3
# payment_after_discount = total_payment - total_discount
# print(payment_after_discount)

# print("total payment : " + str(total_payment))
# print("total payment after discount : " + (payment_after_discount)) #wrong
# print("total payment after discount : " + str(payment_after_discount)) #right

""""Python expects a string on the right side of the + operator. 
Here, payment_after_discount seems to be a numerical value (perhaps a float or an integer), not a string.
 Python doesn't automatically convert it to a string in this context, so it raises an error."""

# name = input("What's your name ? ")
# print(name)
# print("Hello my name is " + name)

# print("""Burger Pricelist : 
# 1. Beef Burger $15 
# 2. Cheese Burger $20 
# 3.Kids Burger $9   """)
# menu_price = input("Menu price : ") #menu price value based on input
# amount = input("Amount : ")
# # bill= menu_price*amount #Purchase totals
# bill= int(menu_price)* int(amount)#From string is changed to integer
# print("You need to pay $" +str(bill))

# Python program for student data

# Input first name, last name, and class code
# first_name = input("Enter your first name: ")
# last_name = input("Enter your last name: ")
# class_code = input("Enter your class code: ")

# Display student data
# print("\nStudent Data:")
# print("--------------")
# print("First Name:" + first_name)
# print("Last Name:"+ last_name)
# print("Class Code:" + class_code)

# print("Your Information:" + first_name, last_name, "-", class_code)
# print("Your Information:" )
# print(first_name, last_name, "-", class_code)

# # Step 1: Save the age of the applicant in a list called ages
# ages = [14, 15, 8, 10, 17, 18, 20, 21, 19, 10, 25, 21, 10, 20, 15]

# # Step 2: Sort the items in the ages list
# ages.sort()

# # Step 3: Create a new list named new_ages to save the eligible ages of applicants
# new_ages = [age for age in ages if 16 <= age <= 25]

# # Output the sorted ages and the eligible ages
# print("Sorted ages:", ages)
# print("Eligible ages:", new_ages)

temperature = [ #Outer list
    [25, 27, 28, 27], #Inside is another list. 
    [23, 24, 26, 26],
    [24, 24, 27, 27],
    [22, 24, 25, 24]
]

print(temperature)
print(temperature[0])
print(temperature[0][0])

temperature.append([23,24,24,26])
print(temperature)
print(len(temperature))

