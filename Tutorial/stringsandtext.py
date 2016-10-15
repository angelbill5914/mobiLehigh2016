#Substitues %d with 10
x = "There are %d types of people" % 10

binary = "binary"
do_not = "don't"

#Replaces the %s with corresponding strings which are defined by the variable
y = "Those who know %s and those who %s" % (binary, do_not)

print x
print y

#%r seems to be uniersal. Replaces it with the string associated with x
print "I said %r" % x

#Substitues %s with the string assosciated with the variable y
print "I also said: '%s'." % y

#Makes the variable hilarious come out as False
hilarious = False

#Prints out the joke_evaluation string and replaces %r with the variable hilarious
joke_evaluation = "Isn't that joke so funny?! %r"
print joke_evaluation % hilarious

w = "I can fuck you from the left side or"
e = " I can fuck you from the right side."

#Adds the two string togethers
print w + e
