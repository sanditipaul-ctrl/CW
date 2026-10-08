class car:
    name = ''
    color = ''

    def __init__(self, name, color, model):
        self.name = name
        self.color = color
        self.model = model

    def intro(self):
        print(f'Name: {self.name}')
        print(f'Color: {self.color}')
        print(f'Model: {self.model}')

c1 = car()
c1.set_values('toyota','red')

c1.intro()
c2 = car()
c2.set_values('a', 'blue')
c2.intro()
print("Thanks")