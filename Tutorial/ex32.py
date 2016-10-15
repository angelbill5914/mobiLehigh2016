

#Sets up various lists
the_counts = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#Loop runs with number as a variable that changes values as it goes through the list
for number in the_counts:
    print "This is count %d" %number #Prints out each each of the elements in the string

for fruit in fruits:
    print "A fruit of type: %s" % fruit

for i in change:
    print "I got %r" % i

#Sets up an empty list
elements = []


for i in range(0,6): #Contains numbers 0, 1, 2, 3, 4, 5!!
    print "Adding %d to the list." % i
    elements.append(i) #Adds the numbers into the list "element"

for stuff in elements:
    print "Element was: %d" % stuff
