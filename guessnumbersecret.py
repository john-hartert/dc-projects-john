import random
secret_number = random.randint(1, 25)
a = 1
guess = 6
print "I'm thinking of a number between 1 and 25"
while a < 25:
    while guess:
        guess = guess - 1
        print "You have", guess, "guesses left!"
        break
    b = int(raw_input('Guess a number? '))
    if b == secret_number:
        print "You win!"
        break
    elif b < secret_number:
        print "That\'s too low!"
    else:
        print "That\'s too high!"
