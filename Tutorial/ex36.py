
ten_things = "Apples Oranges Crows Telephones Light Sugar"

print "Wait there's not 10 things in that list, let's fix that."

stuff = ten_things.split(' ') #Splits the thing into a list
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10: #Counts the number of things in the split list
    next_one = more_stuff.pop() #Pops the last one from the more_stuff list
    print "Adding: ", next_one
    stuff.append(next_one) #Adds it to the split list
    print "There's %d items now." % len (stuff)

print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff [1] #Prints 2nd
print stuff[-2] #Prints out 2nd to last one from the list
print stuff.pop() #Removes the last one from the list
print ' '.join(stuff) #Combines the list into a string again
print '#'.join(stuff[3:5]) #Prints out elements 3,4. Doesn't include 5!!!
