

#i = 0
#numbers = []

#while i < 6:
#    print "At the top i is %d" % i
#    numbers.append(i)

#    i = i + 1
#    print "Numbers now: ", numbers
#    print "At the bottom i is %d" % i

#print "The numbers: "

#for num in numbers:
#    print num

def test (number, increment):
    i = 0
    numbers = [] #Sets up an empty list

    while i < number:
        print "At the top i is %d" % i
        numbers.append(i) #Adds numbers to the list

        i = i + increment
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

    print "The numbers: "

    #Prints every number in the list
    for num in numbers:
        print num

#Calls the function
test (6,1)
