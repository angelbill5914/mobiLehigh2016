from sys import argv

script, input_file = argv #Requires file name on the command lind

#Makes a function that reads the file specified
def print_all (f):
    print f.read()

#Reminds the file based on the file specified
def rewind(f):
    f.seek(0)

#Prints out a specific line
def print_a_line(line_count, f):
    print line_count, f.readline(), #Comma at the end fixes the spacing issue!


current_file = open(input_file) #Opens the file specified earlier

#Prints the entire file
print "First let's print the entire file:\n"
print_all(current_file)

#Rewinds the file
print "Now let's rewind, kind of like a tape"
rewind(current_file)

print "Let's print three lines"

#Prints out 3 three lines. Sets up a counter like numebering system
current_line = 1
print_a_line (current_line, current_file)

current_line += 1
print_a_line (current_line, current_file)

current_line += 1
print_a_line (current_line, current_file)
