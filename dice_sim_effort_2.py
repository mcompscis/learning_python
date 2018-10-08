import random

def a_roll(sides = 6):
    num_rolled = random.randint(1, sides)
    return num_rolled
def main():
    rolling = True
    while rolling:
        roll = input('To roll, ENTER=roll. S=Stop')
        if roll != 's':
            num_rolled = a_roll()
            print('You rolled a', num_rolled)
        else:
            rolling = False
    print('Thanks for rollin''!')
main()



