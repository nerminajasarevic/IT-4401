from Animals import Animal, Mammal, Bird

def generate_mammal():
    animal_type = input("What type of mammal would you like to create? ")
    animal_name = input("What is the mammal's name? ")
    hair_color = input("What color is the mammal's hair? ")
    mood = ""

    #create mammal object from subclass
    mammal = Mammal(animal_type, animal_name, mood, hair_color)
    
    return mammal

def generate_bird():
    animal_type = input("What type of bird would you like to create? ")
    animal_name = input("What is the bird's name? ")
    can_fly = input("Can the bird fly? ")
    mood = ""

    #create bird object from subclass
    bird = Bird(animal_type, animal_name, mood, can_fly)
    
    return bird

def main():
    
    print("Welcome to the animal generator!\nThis program creates Animal objects!\n")
    
    animals = []
    
    loop = True
    
    while loop:
        
        class_type = int(input("Would you like to create a Bird or a Mammal? \n1. Mammal \n2. Bird \nWhich would you like to create? "))

        #mammal
        if class_type == 1:
            mammal = generate_mammal()
            animals.append(f"{mammal.get_name()} the {mammal.get_animal_type()} is {mammal.get_mood()}")

        #bird
        elif class_type == 2:
            bird = generate_bird()
            animals.append(f"{bird.get_name()} the {bird.get_animal_type()} is {bird.get_mood()}")

        #value check
        else:
            print("Invalid choice. Please enter 1 for Mammal or 2 for Bird.")
        
        addAnother = input("Would you like to add more animals (y/n)? ")
        
        if addAnother.lower() != 'y':
            loop = False

    #print all animals in list
    print("Animal List:\n")
    
    for animal in animals:
        print(animal)

main()
