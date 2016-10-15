#Gives a function with variables cheese_counts and boxes_of_crackers
def cheese_and_crackers (cheese_counts, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_counts
    print "You have %d boxes of crackers." %boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"

#Directly gives those variables an integer value
print "We can just give the function numbers directly:"
cheese_and_crackers (20,30)

#Defines those variables with another variable
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers (amount_of_cheese, amount_of_crackers)

#Defines those variables using math
print "We can even do math inside too:"
cheese_and_crackers (10 + 20, 5 + 6)

#Defines those variables using both variables and math
print "And we can combine the two, variables and math:"
cheese_and_crackers (amount_of_cheese + 100, amount_of_crackers + 1000)
