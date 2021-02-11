'''Game info:

The player has five strokes forward through the chamber.
He has a chance to find a chest with each step.
There are four types of chests, each with a different color.
The colour of the chest indicates how rare it is:

- green - 75% - about 1000 gold
- orange - 20% - about 4000 gold
- purple - 4% - about 9000 gold
- legendary - 1% - about 16000 gold
'''

import random

gameLength = 0
isThereChest = ['yes', 'no']
chests = ['green', 'orange', 'purple', 'legendary']
treasureAcquire = {chests[reward] : (reward + 1) * (reward + 1) for reward in range(len(chests))}
sumOfGold = 0
print(treasureAcquire)


def findApproximateValue(value):
    newValue = random.randint(value - value*0.1, value + value*0.1)
    return newValue

while gameLength < 5:
    moveForward = input('Do you want to move forward? y/n: ')
    if moveForward.lower() == 'y':
        print("Ok, let's see what you got...")
        isThereSomething = random.choices(isThereChest, [60, 40])
        print(isThereSomething)
        
        if isThereSomething == ['yes']:
            chest = random.choices(chests, [75, 20, 4, 1])[0]
            print('You have found' ,chest, 'chest.')
            
            treasure = treasureAcquire[chest] * 1000

            newValue = findApproximateValue(treasure)
            
            print('Gold acquired:', newValue)
            sumOfGold += newValue
            gameLength += 1
  
        elif isThereSomething == ['no']:
            print('There is nothing.')
            gameLength += 1
            continue
        
    elif moveForward.lower() == 'n':
        print('Player does not move.')
        continue
    else:
        print('Incorrect value')

print('Sum of gold:', sumOfGold)
    
