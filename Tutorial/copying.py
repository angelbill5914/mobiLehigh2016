from sys import argv
from os.path import exists #Determines if a file exists or not

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

#in_file = open(from_file)
#indata = in_file.read()

#Combine the two statements above. Also Python CLOSES the file by itself!!!
indata = open (from_file).read()

print "The input file is %d bytes long" % len(indata) #Gives size of the file

print "Does the output file exist? %s" % exists(to_file)
print "Ready? Hit RETURN to continue, CTRL-C to quit."

raw_input("THE CHOICE IS YOURS!!!")

out_file = open(to_file, 'w') #Opens the file for WRITING ONLY
out_file.write(indata) #Write to the file what was stored on the other file

print "Alright all done."

out_file.close()
