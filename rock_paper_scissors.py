#rock paper scissors

from random import randint
player = raw_input('rock (r) paper (p) scissors (s)?')

chosen = randint(1,3)
#print(chosen)

if chosen == 1:
    computer = 'r'
elif chosen == 2:
    computer = 'p'
elif chosen == 3:
    computer = 's'

print (player + ' vs ' + computer)

if player == computer:
    print ("DRAW!!!")
elif player == 'r' and computer == 's':
    print ("PLAYER WINS!!!")
elif player == 's' and computer == 'p':
    print ("PLAYER WINS!!!")
elif player == 'p' and computer == 'r':
    print ("PLAYER WINS!!!")
elif player == 'r' and computer == 'p':
    print ("COMPUTER WINS!!!")
elif player == 'p' and computer == 's':
    print ("COMPUTER WINS!!!")
elif player == 's' and computer == 'r':
    print ("COMPUTER WINS!!!")
