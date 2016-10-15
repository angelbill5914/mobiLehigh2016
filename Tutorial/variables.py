
#Assigns the variable car a value of 100
cars = 100

#Assigns the variable space_in_a_car a value of 4
space_in_a_car = 4

#Assings the variable drivers a value of 30
drivers = 30

#Assigns the variable passenger a value of 90
passengers = 90

#Assigns the variable cars_not_driven a value of 100 - 30 which is 70
cars_not_driven = cars - drivers

#Assigns the variable cars_driven the same as the varaible drivers
cars_driven = drivers

#Finds the carpool_capacity by multiplying 100 by 4 which is 400
carpool_capacity = cars * space_in_a_car

#Finds the average passenger per car by dividing 90 by 30 which is 30
average_passenger_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven ,"empty cars today."
print "We can transport", carpool_capacity , "people today."
print "We have", passengers ,"to transport today."
print "We need to put about", average_passenger_per_car ,"people per car."
