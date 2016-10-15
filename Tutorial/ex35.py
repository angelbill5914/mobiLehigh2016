
from sys import exit

def gold_room():
    print "This room is full of gold. How much do you take?"

    next = raw_input("> ")
    how_much = float(next) #Converse the user string input into a float number

    #if "0" in next or "1" in next:
    #    how_much = int(next)
    #else:
    #    dead("Man, learn to type a number.")

    if how_much < 50:
        print "Nice, you are not greedy. You win!"
        exit (0) #Exits the program
    else:
        dead("You greedy bastard. Go die.")

def bear_room():
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"
    bear_moved = False

    while True:
        next = raw_input("> ")

        if "take" in next: #Looks for the string "take" in the user input
            dead ("The pissed bear beats the crap out of you.")
        elif "taunt" in next and not bear_moved:
            print "The bear has moved from the door. You can go through it now."
            bear_moved = True
        elif "taunt" in next and bear_moved:
            dead ("The bear gets pissed off and chews your leg off.")
        elif "open" in next and bear_moved:
            gold_room() #Goes to the gold room
        else:
            print "I got no idea what that means"

def dragon_room():
    print "Here you see the great evil Cthulu"
    print "He, it, whatever stares at you and you go insane."
    print "Do you flee for your life or eat your head?"

    next = raw_input("> ")

    if "flee" in next:
        start ()
    elif "head" in next:
        dead("Well that was tasty!")
    else:
        dragon_room()

#Exits the game after ending with Good Job!
def dead(why):
    print why, "Good job!"
    exit(0)

def start ():
    print "You are in a dark room."
    print "There is a door to your right and left."
    print "Which one do you take?"

    next = raw_input("> ")

    if next == "left":
        bear_room()
    elif next == "right":
        dragon_room()
    else:
        dead("You stumble across the room until you starve")

start () #Starts the game
