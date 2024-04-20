#ages = [27, 16, 3, 7, 99, 20, 14, 101]

#dot operator 
#ages.append(200)

class Animal:
    #properties
    age = 0
    name = '*nameless creature*'
    energy  = 5
    sound = '*ominous silence*'

    #methods
    def grow_older(self):
        self.age += 1
    
    def __init__(self,name = ''):
        if not name:
            return
        self.name = name # Updating the 'name' property

    def make_sound(self):
        print(f'{self.name}: {self.sound}')

class Giraffe(Animal):
    def make_sound(self):
        print(f'{self.name}: Aruuuuuu')

class Pig(Animal):
    def __init__(self, name = ''):
        super().__init__(name)
        self.sound = 'ooink'


generic  = Animal('')
generic.make_sound()


giraffe = Giraffe('Long Neck')
giraffe.make_sound()

pig = Pig('Chris P. Bacon ')
pig.make_sound()