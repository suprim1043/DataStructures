#Revising object oriented programming, from geeksforgeeks

#class
#classes are the blueprints which object is based off of.

class Dog:
    species = "Husky" # this is attribute of class iteself, *******class variable*******
    def __init__(self, name, age):
        self.name = name
        self.age = age #this is attribute for the instance, ********instance variable******


#object is an instance of class

first_dog = Dog("Loki", 7)
print(first_dog) #prints the object and holds attribute values for name and age
print(Dog.species) # this is attribute of class itself



#Inheritance

#allows child class to aquire properties and methods from other parent class, basically inherits them

class inherit(Dog):
    def printname(self):
        print(self.species, self.name)

testInherit = inherit("german shephard", 2)


#Polymorphism

#When 2 classes have methods with same name, polymorphism can be used to invoke specific methods

class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

# Using polymorphism
def animal_speak(animal):
    print(animal.speak())

dog = Dog()
cat = Cat()

animal_speak(dog)  # Output: Woof!
animal_speak(cat)  # Output: Meow!


#encapsulation

#public, protected with '_' and private '__'