# number = [10, 16, 30, 21]
# print(max(number)) #displays the largest value
# print(min(number)) #displays the lowest value
# print("hello".upper()) #Change the text to capital letters
# print("WELCOME".lower()) #Changes text to lowercase

# def order_pizza(): 
#     quantity = 7
#     price = 10
#     total_order = quantity * price
#     print(f"Total order  $:  {total_order}" )

# order_pizza() #Running functions.

# def order_pizza(quantity): 
#     price = 10
#     total_order = quantity * price
#     print(f"Total order  $:  {total_order}" )

# order_pizza(7)

def order_pizza():
    quantity = int(input("How many pizzas would you like to order? "))
    price = 10
    total_order = quantity * price
    print(f"Total order  $:  {total_order}")

order_pizza()

# def sum():
#     first = 10
#     second = 20
#     total = first+second
# print(total)

# total = 50 #Global variable : variable are declared outside the function. 
# def sum():
#     first = 10
#     second = 20
#     total = first+second #Local variable: Variable are declared in functions.
#     print(total)
# print(total)
# sum()
