
from sys import argv

script, file_name = argv

print "We are going to erase %s" %file_name
print "If you don't want that, enter CONTROL-C"
print "If you want that, hit RETURN!"

raw_input("?")

print "Hacking your file...."
target = open (file_name, 'w') #Opens the file IN WRITING MODE ONLY!!!

print "Deleting this file now. Goodbye!"
target.truncate() #Deletes the words inside of the file

print "Now I am going to ask you for three lines."

line1 = raw_input("Enter Line 1: ")
line2 = raw_input("Enter Line 2: ")
line3 = raw_input ("Enter Line 3: ")

print "I am going to write those lines to the files."

#Writes the three lines to the file. each on seperate lines
target.write(line1 + "\n" + line2 + "\n" + line3)

target.close() #Closes the file
