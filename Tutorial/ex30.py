
people = 30
cars = 40
buses = 15

#Prints the corresponding line depending on the value of the variables
if cars > people:
    print "We should take the cars."
elif cars < people:
    print "We should not take the cars."

#Prints the corresponding line depending on the value of the variables
if buses > cars:
    print "That's too many buses"
else:
    print "We can't decide"


#Prints the corresponding line depending on the value of the variables
if buses > cars:
    print "That's too many buses"
elif buses < cars:
    print "Maybe we could take the buses"
else:
    print "We still can't decide"


#Prints the corresponding line depending on the value of the variables
if people > buses:
    print "Alright, let's just take the buses"
else:
    print "Fine, let's stay home then."
