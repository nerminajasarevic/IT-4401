from Animal import Animal
 
print("Welcome to the animal generator!")
print("This program creates Animal objects.")

    #set empty list of animals
    animals = []

while True:
        
    animal_type = input("What type of animal would you like to create? ")
    
    name = input("What is the animal's name? ")
    
    #create object
    animal = Animal(animal_type, name)
    
    #add animal object to list
    animals.append(animal)

    anotherAnimal = input("Would you like to add more animals (y/n)? ").lower()
    
    if anotherAnimal != 'y':
        break

print("Animal List:")

#iterate through list and print
for animal in animals:
    print(f"{animal.get_name()} the {animal.get_animal_type()} is {animal.check_mood()}")
