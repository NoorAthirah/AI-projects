class Person:

    # constructor
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def say_hello(self):
        print(f'\nHello {self.name}, nice to meet you!')

    def ride(self):
        self.say_hello()
        if self.age > 10 and self.height >= 100:
            print(f'Congratulations {self.name}! You may ride the roller coaster.')
        else:
            print(f'Sorry {self.name}, you may not ride the roller coaster.')


# objects
james = Person("James", 10, 140)
rose = Person("Rose", 12, 150)
dove = Person("Dove", 12, 150)
diva = Person("Diva", 8, 130)

while True:

    person_name = input("\nEnter name: ").strip().lower()  # Convert input to lowercase

    if person_name == 'james':
        james.ride()
    elif person_name == 'rose':
        rose.ride()
    elif person_name == 'dove':
        dove.ride()
    elif person_name == 'diva':
        diva.ride()
    else:
        print("Invalid input")

    ans = input("\nPress 'y' to continue / 'n' to quit: ").strip().lower()

    if ans == 'n':
        break