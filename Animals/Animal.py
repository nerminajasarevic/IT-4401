import random

class Animal:

    #set default values
    def __init__(self, animal_type, name):
        self.__animal_type = animal_type
        self.__name = name
        self.__mood = self.set_mood()

    #randomly set mood through switch statement
    def set_mood(self):
        moods = {
            1: "happy",
            2: "hungry",
            3: "sleepy"
        }
        mood = random.randint(1, 3)
        return moods[mood]
    
    #return type
    def get_animal_type(self):
        return self.__animal_type

    #return name
    def get_name(self):
        return self.__name

    #return randomly set mood from set_mood
    def check_mood(self):
        return self.__mood
