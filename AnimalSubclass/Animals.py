import random

class Animal:

    def __init__(self, animal_type, name, mood):
        self.animal_type = animal_type
        self.name = name

        #set random mood
        moods = random.randint(1, 3)
        
        if moods == 1:
            self.mood = "happy"
        elif moods == 2:
            self.mood = "hungry"
        else:
            self.mood = "sleepy"

    def get_animal_type(self):
        return self.animal_type

    def get_name(self):
        return self.name

    def get_mood(self):
        return self.mood

class Mammal(Animal):
    
    def __init__(self, animal_type, name, mood, hair_color):

        #call method from animal class
        super().__init__(animal_type, name, mood)
        self.hair_color = hair_color

    def get_hair_color(self):
        return self.hair_color

class Bird(Animal):
    
    def __init__(self, animal_type, name, mood, can_fly):

        #call method from animal class
        super().__init__(animal_type, name, mood)
        self.can_fly = can_fly

    def get_can_fly(self):
        return self.can_fly
