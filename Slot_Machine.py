import random
slot_machine = []
cards = ['Cherry', '7', 'J', '10', 'Apple', 'A', 'Q','M']
#out = random.choice(cards)
n = 0
for i in range (0, 3):
    out = random.choice(cards)
    slot_machine.append(out)
    n += 1
print(slot_machine)    
