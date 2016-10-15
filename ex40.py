
#Starts a class
class Song (object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday = Song([
"Happy birthday to you.",
"I don't want to get sued.",
"So I'll stop right there."])

bulls_on_parade = Song ([
"They rally around the family.",
"With pockets full of shells"])

yellow_bus = Song ([
"The wheels on the bus go round and round.",
"Round and round."
])

song = "WTF IS THIS SHIT!!" #Defines a variable as a string
test_song = Song ([song]) #Class uses the variable as an input

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()
yellow_bus.sing_me_a_song()
test_song.sing_me_a_song()




class Math(object):
    def __init__(self,number):
        self.test = number

    def calculate(self):
        for nums in self.test:
            print nums * 2

    def calculate2(self):
        for nums in self.test:
            print nums

test_number = Math([5, 4, 3, 2, 1])

test_number.calculate()
test_number.calculate2()
