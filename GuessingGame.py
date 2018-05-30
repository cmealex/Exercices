# import random
#
# # numbers_list = [x for x in xrange(0, 10)]
# # rndNp = random.choice(numbers_list)
#
# rndNp = random.randint(1,9)
# # print rndNp
#
# how_many_guesses = 0
# while True:
#     guess = raw_input("Guess the number: ")
#     how_many_guesses += 1
#     if guess == 'exit':
#         break
#     elif int(guess) < rndNp:
#         print 'too low'
#     elif int(guess) > rndNp:
#         print 'too high'
#     else:
#         print 'thats it!!!'
#         print 'you guessed in: {} tries'.format(how_many_guesses)
#         break

import random
# rndN=random.randint(1, 1000)
rndN = 13
while True:
    guess = int(input("Input a number: "))
    if guess < rndN:
        print("Try Highed")
    elif guess > rndN:
        print("Try Lower")
    else:
        print("Congratulations")
        break



