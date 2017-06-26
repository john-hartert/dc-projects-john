#import random
def firstFunc():
    #secret_number = random.randint(1, 25)
    secret_number = 22
    return secret_number

print "I'm thinking of a number between 1 and 25"

def lastFunc():
    guess = 6
    if guess > 0:
        guess = guess - 1
        print "You have", guess, "guesses left!"
    else:
        False
    return guess

def secFunc():
    a = 1
    #guess = 6
    while a < 25:
        #while guess:
            #guess = guess - 1
        #if guess > 1:
        #    guess = guess - 1
        #    print "You have", guess, "guesses left!"
        #    break
        b = int(raw_input('Guess a number? '))
        if b == firstFunc():
            print "You win!"
            break
        elif b < firstFunc():
            print "That\'s too low!"
        else:
            print "That\'s too high!"
    return secFunc


def main():
    secret_number = firstFunc()
    guess = lastFunc()
    secFunc()
    
    
main()
