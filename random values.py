import random

for i in range(3):
    print(random.randint(10, 20))


import random

members = ['keerthana', 'raju', 'priya']
leader = random.choice(members)
print(leader)

import random


class dice:
    def roll(self):
        first = random.randint(1,6)
        second = random.randint(1,6)
        return first,second
  
    
dice = dice()
print(dice.roll())