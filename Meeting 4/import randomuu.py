import random

names = []

print('Add names to shuffle! \nPress "S" to stop adding names')

# Add names to the list
while True:
    add_name = input('Add name: ')
    if add_name.lower() != 's':
        names.append(add_name)
    else:
        if not names:
            print('No names were added.')
            exit()
        break

# Continuously choose random names
print('Press "Q" to stop choosing names')
while True:
    random_name = random.choice(names)
    print('Chosen person: ' + random_name)
    
    continue_choice = input('Press Enter to choose another name, or "Q" to quit: ')
    if continue_choice.lower() == 'q':
        break
