
formatter = "%r %r %r %r" #Sets up four different places that are to be replaced

print formatter % (1, 2, 3, 4) #Puts 1 2 3 4 in thr four spots
print formatter % ("One", "Two", "Three", "Four") #Replaces the four spots with strings
print formatter % (True, False, False, True) #Replaces the four spots with true and false statements
print formatter % (formatter, formatter, formatter, formatter) # Replaces the four spots with more of the variable formatter

#Replaces the four spots with long strings. Looks more organized. Don't forget COMMAS!!!
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing",
    "So I said goodnight"
)
