import random
while True:
    options = ['Rock', 'Paper', 'Scissors']
    msg = "choose from options: " + " ".join(options) + " : "
    p1 = raw_input(msg)
    p2 = random.choice(options)
    print p1
    print p2
    if p1 == 'Rock' and p2 == 'Rock':
        print 'Tie'
    elif p1 == ' Rock' and p2 == 'Paper':
        print 'p2 wins'
    elif p1 == ' Rock' and p2 == 'Scissors':
        print 'p1 wins'
