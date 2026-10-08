class car:
    name = ''
    color = ''
    model = ''

    def set_values(self,n,c,m):
        self.name = n
        self.color = c
        self.model = m

        #method
    def intro(self):
        print(f'Name: {self.name}\n Color: {self.color}\nModel: {self.model}')

c1 = car()
c1.set_values('toyota','red', 123)

c1.intro()
c2 = car()
c2.set_values('a', 'blue', 256)
c2.intro()