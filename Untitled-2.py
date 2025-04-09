class Animal:
    def __init__(self, name, legs):
        self.name = name  # Name of the animal
        self.legs = legs  # Number of legs the animal has

    # 5. Method to get the number of legs
    def getLegs(self):
        return self.legs

    # 4. Method to set the number of legs
    def setLegs(self, legs):
        self.legs = legs

    # 6. Method to print all attributes of the Animal
    def printInfo(self):
        print(f"Name: {self.name}, Legs: {self.legs}")
        
        # 1. Create two realistic instances of Animals
dog = Animal("Dog", 4)
cat = Animal("Cat", 4)

        # 3. Change the amount of legs of one object using dot notation
dog.legs = 3  # Let's say the dog lost a leg

# Print after changing legs
print(dog.name + " has " + str(dog.legs) + " legs.")  # Output: Dog has 3 legs.

# 4. Add a method setLegs() to set the legs of an object and repeat task 3
cat.setLegs(3)  # Let's say the cat lost a leg too

# Print after using setLegs method
print(cat.name + " has " + str(cat.getLegs()) + " legs.")  # Output: Cat has 3 legs.

# 6. Print all attributes of both animals using printInfo()
dog.printInfo()  # Output: Name: Dog, Legs: 3
cat.printInfo()  # Output: Name: Cat, Legs: 3
