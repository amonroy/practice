#from reddit.com/r/dailyprogrammer/
#challenge #149[easy] disemvowler

#output, text with all vowels removed, all removed vowels
def disemvowler():
    """This function takes your input and disemvowels it, and also regurgitates your vowels."""

    prompt = '> '
    sentence = raw_input('What\'s your sentence?' + prompt)
    vowels = 'aeiou'
    no_space = sentence.replace(" ","")
    no_vowels = "".join(letter for letter in no_space if letter not in vowels)
    vowels = "".join(letter for letter in no_space if letter in vowels)
    print "This is the disemvoweled text: " + no_vowels
    print "This is the leftovers: " + vowels

disemvowler()
#text = raw_input("Enter string: ").replace(" ","")
#vowels = ["a", "e", "i", "o", "u"]
#print "".join(letter for letter in text if letter not in vowels)
#print "".join(letter for letter in text if letter in vowels)

