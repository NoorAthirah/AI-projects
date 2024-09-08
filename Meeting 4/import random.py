import random

names = []

print('Add names to shuffle! \nPress "S" to stop')
while True:
    add_name = input('Add name: ')
    if add_name.lower() != 's':  # Correct condition
        names.append(add_name)
    else:
        if names:  # Check if there are any names in the list
            random_name = random.choice(names)  # Correct function
            print('Chosen person: ' + random_name)  # Correct concatenation
        else:
            print('No names to choose from.')
        break
