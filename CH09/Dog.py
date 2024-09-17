class Dog:

    # __init__ is a constructor
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def sit(self):
        print(f'{self.name} is now sitting!')

    def roll_over(self):
        print(f'{self.name} is rolling over.')

    def bark(self):
        print(f'The {self.colour} dog is barking :o')
