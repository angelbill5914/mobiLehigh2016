
from sys import argv

#Needs user to enter the file name when running the command
script, file_name = argv

txt = open(file_name) #Opens the file specified

#Restates the name of the file and spits out what is inside.
print "Here's your file %s:" % file_name
print txt.read()

#Asks user for the file name again
print "Type the file name again:"
file_again = raw_input("Enter here:")

#Opens the file and then prints out what is inside
txt_again = open (file_again)
print txt_again.read()
