import random
import string
print("Welcome to Email Maker!")


# name_list = ["swift", "taylor"]
adjectives_list = ["sleepy", "slow", "fluffy", "red", "yellow", "green", "blue"]

# name = random.choice(name_list)  
name = input("What's your name ? ")
adjective = random.choice(adjectives_list)
number = random.randrange(0, 100)

email = name+ adjective + str(number) 
print("Recommended email: " + email+"@mail.com") 
