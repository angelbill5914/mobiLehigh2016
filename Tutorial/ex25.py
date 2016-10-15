

def break_words (stuff):
    """This function will break up words for us"""
    words = stuff.split (' ') #Very important to leave a space.
    return words #Returns the words in a broken up format

def sort_words (words):
    """Sorts the words"""
    return sorted (words)

def print_first_word (words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print word

def print_last_word (words):
    """Prints the last word after popping it off."""
    words = words.pop(-1)
    print word

def sort_sentence (sentence):
    """Takes in full sentence and returns the sorted words."""
    words = break_words (sentence) #Breaks apart the sentence
    return sort_words (words) #Formats the broken up words

def print_first_and_last (sentence):
    """Prints the first and last words of the sentence"""
    words = break_words (sentence)
    print_first_word
    print_last_word

def print_first_and_last_sorted (sentence):
    """Sort the words then prints the first and last one."""
    words = sort_sentence (sentence)
    print_first_word (words)
    print_last_word (words)
