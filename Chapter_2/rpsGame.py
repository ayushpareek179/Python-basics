# Rock, paper, scissors!
import random, sys

print ("ROCK, PAPER, SCISSORS")
wins, loss, tie = 0, 0, 0
while True:
    #print (str(wins)+" Wins, "+str(loss)+" Losses, "+str(tie)+" Ties")
    print ("%s Wins, %s Losses, %s Ties" %(wins, loss, tie))
    while True: # The player input loop
        print ("Enter your move: (r)ock (p)aper (s)cissors or (q)uit")
        playerMove = input()
        if playerMove == "q":
            sys.exit() # Quit the program
        if playerMove == "r" or playerMove == "p" or playerMove == "s":
            break
        print ("Type one of r, p, s or q.")
    # Display what the player chose:
    if playerMove == 'r':
        print ("ROCK versus...")
    elif playerMove == 'p':
        print ("PAPER versus...")
    else:
        print ("SCISSORS versus...")
    # Display what the computer chose:
    randNum = random.randint(1,3)
    if randNum == 1:
        compMove = 'r'
        print("ROCK")
    elif randNum == 2:
        compMove = 'p'
        print ("PAPER")
    else:
        compMove = 's'
        print ("SCISSORS")
    # Display and record the win/loss/tie:
    if compMove == playerMove:
        print ("It is a tie!")
        tie += 1
    elif compMove == 'r' and playerMove == 'p' or compMove == 's' and playerMove == 'r' or compMove == 'p' and playerMove == 's':
        print ("You win!")
        wins += 1
    else:
        print ("You lose!")
        loss += 1


