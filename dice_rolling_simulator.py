import random

'''print('\n')
print('Welcome to the Dice simulator! \n')
print('Simply write "roll" or "Roll" and let the magic happen \n')


action = input()
print('\n')


if(action == 'roll'):
    value = random.randint(1,7)
    print(value)
elif(action == 'Roll'):
    value = random.randint(1, 7)
    print(value)
else:
    print ('Please type "roll or Roll"')'''


def roll(sides=6):
    num_rolled = random.randint(1,sides)
    return num_rolled
def main():
    sides = 6
    rolling = True
    while rolling:
        roll_again = input('Ready to roll? ENTER=Roll. Q=Quit.')
        if roll_again.lower() != "q":
            num_rolled = roll(sides)
            print('Yor rolled a', num_rolled)
        else:
            rolling = False

    print('Thanks for playing!')


main()