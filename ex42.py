
## Animal is-a object
class Animal(object):
    pass

## Dog is-a kind of animal
class Dog(Animal):
    def __init__(self,name):
        ## Dog has-a name
        self.name = name

## Cat is-a kind of animal
class Cat(Animal):
    def __init__(self, name):
        ## Cat has-a name
        self.name = name

## Person is-a object
class Person(object):
    def __init__(self,name):
        ## Peron has-a name
        self.name = name

        ## Person has-a pet
        self.pet = None

## Employee is-a kind of Person
class Employee(Person):
    def __init__(self, name, salary):
        ## class Employee has-a name of the parent class Person
        super(Employee, self).__init__(name)

        ## Employee has-a salary
        self.salary = salary

## Fish is-a object
class Fish(object):
    pass

## Salmon is-a Fish
class Salmon(Fish):
    pass

## Halibut is-a Fish
class Halibut(Fish):
    pass

## rover is-a Dog
rover = Dog("Rover")

## satan is-a cat
satan = Cat("Satan")

## mary is-a person
mary = Person("Mary")


## Frank is-a Employee that has-a 120,000 salary
frank = Employee("Frank", 120000)

## Mary has-a pet that is-a cat named Satan
mary.pet = satan

## Frank has-a pet that is-a dog named Rover
frank.pet = rover

## Fish has-a flipper
flipper = Fish()

## Salmon has-a crouse
crouse = Salmon()

## Halibut has-a hairy
harry = Halibut()
