def jackpot(CountJackpot,previous_count): #Takes input for jackpot and previous count

    if CountJackpot[0]== CountJackpot[1] and CountJackpot[1] == CountJackpot[2]: # looks for jackpot 
        previous_count += 1    
    else:
      previous_count = previous_count # previous count will stay the same in the case of no jackpot
    return previous_count   

import random

def unmatch(): # function to create mismatch roll
    slot_machine = []
    cards = ['Cherry', '7', 'J', '10', 'Apple', 'A', 'Q','M']
    for i in range (0, 3):
        out = random.choice(cards)
        slot_machine.append(out)
    return slot_machine

def match(): # function to creat matiching roll
    slot_machine = []
    cards = ['Cherry', '7', 'J', '10', 'Apple', 'A', 'Q','M']
    out = random.choice(cards)
    for i in range (0, 3):
        slot_machine.append(out)
    return slot_machine

block = {'unmatch' : unmatch(), 'match' : match(), 'unmatch1' : unmatch()} # dictionary which hosts two fuctions that gives 1/3 jackpot chance

count = 0           # initial while loop count
startcount = 0      # initial jackpot count

while count < 1000:     #loop :)
    key = random.choice(list(block))
    #print(block[key])                        #in case you want to go manual (not recommended!)
    game = jackpot(block[key],startcount)
    startcount  = game
    count += 1
print(f"total jackpot count {game} ")    
