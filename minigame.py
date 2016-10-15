from sys import exit #Import the exit function


start()

def start():
    print "You are at lit college party at a frat house"
    print "You get tired from dancing too long and decide to take a break"
    print "What do you decide to do?"

    While True:
        next = raw_input()

        if "fuck" in next or "sex" in next:
            print "You are too tired to have sexual intercourse. Do something else"

        elif "upstairs" in next:
            upstairs()

        elif "basement" in next or "downstairs" in next:
            basement()

        elif "stand" in next or "nothing" in next:
            print "Host of the party thinks you are boring as fuck."
            print "He then kicks you out of the party. Nice!"
            exit(0)

        elif "leave" in next or "out" in next:
            leave()

        else:
            print "What? Don't forget there are stairs leading upstairs and to the basement"

def upstairs():
    print "You start feeling the urge to urinate. You see there is a bathroom down the hall"
    print "Yet you also hear a moaning sound coming from a room."
    print "What do you decide to do?"

    piss = False

    while True:
        next = raw_input()

        if "downstairs" in next or "back" in next:
            start()

        elif "leave" in next or "out" in next:
            leave()

        elif "nothing" in next or "stand" in next:
            print "You pissed your pants and feel embarassed."
            print "You leave the party. Nice..."
            exit(0)

        elif "bathroom" in next and not piss:
            print "You took a piss and feel fine now."
            piss = True

        elif "bathroom" in next and piss:
            "You just took a piss. WTF?"

        elif "sound" in next or "room" in next or "moaning" in next:
            sexy_room()
