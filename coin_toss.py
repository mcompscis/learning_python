import random

def a_toss(sides = 2):
    toss = random.choice(choices)
    return toss

choices = ['Heads', 'Tails']

def main():
    sides = 2
    tossing = True
    while tossing:
        toss_again = input('Ready to toss? ENTER=toss. S + ENTER = stop. \n')
        if toss_again != 's':
            toss = a_toss()
            print('You flipped a', toss, '! \n')
        else:
            tossing = False

    print('Thanks for tossing! \n')
main()


