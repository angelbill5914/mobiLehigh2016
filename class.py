

class Human():
    number_of_humans = 0

    def __init__(self, name, gender, coolness):
        self.name = name
        self.gender = gender
        self.coolness = coolness
        Human.number_of_humans += 1

    def my_name(self):
        print "My name is %s" % self.name

    def my_gender(self):
        print "My gender is %s" % self.gender

    def my_coolness(self, age):
        print "I have a coolness rating of %i" % self.coolness
        print "I am at the age of %i" % age

#Creats an object called will
will = Human("Williams Smartpants", "Male", 75)

tom = Human("Tom Dumbpants", "Female", 75)

#Checks if the objects are at the same address
if will is not tom:
    print "They are not at the same address."

will.my_name()
will.my_gender()
will.my_coolness(5)
