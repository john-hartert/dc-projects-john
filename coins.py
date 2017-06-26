coin = 1
c = True
while c:
    b = raw_input('Do you want a coin? ')
    if b == "yes":
        print "You have %d" % coin
        coin = coin + 1
    else:
        print "Bye"
        c = False