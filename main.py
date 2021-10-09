import random
from graphic_view import *
from intro import *
from count import *

def try_again():
    decision = input("Do you want to try again? (Yes/No): ").lower()
    if decision == "y" or decision == "yes":
        main()
    else:
        print("\n**************************************************************************************************")
        exit

intro()
trial = 3
Pscore = 0
Cscore = 0
def main():
    global Pscore
    global Cscore
    global trial
    if trial >= 1:
        num = random.randint(1,3)
        print('\nChances left: ',trial)
        player = int(input("Enter the number: "))
        count()
        if num == player:
            print(Tied[player])
            main()
        elif num == 1 and player == 2:
            print(PlayerWins[player])
            Pscore+=1
            trial-=1
            main()
        elif num == 1 and player == 3:
            print(ComputerWins[num])
            Cscore+=1
            trial-=1
            main()
        elif num == 2 and player == 1:
            print(ComputerWins[num])
            Cscore+=1
            trial-=1
            main()
        elif num == 2 and player == 3:
            print(PlayerWins[player])
            Pscore+=1
            trial-=1
            main()
        elif num == 3 and player == 1:
            print(PlayerWins[player])
            Pscore+=1
            trial-=1
            main()
        elif num == 3 and player == 2:
            print(ComputerWins[num])
            Cscore+=1
            trial-=1
            main()
        else:
            print('''
            You have typed wrong value
            Please enter the correct value !!!
            ''')
            main()
    else:
        print(f'''
    _________________________________
    |   Computer     |    Player    |
    |________________|______________|
    |       {Cscore}        |      {Pscore}       |
    |________________|______________|  
    ''')
        if Pscore > Cscore :
            print('''
        !!! You Win The Game !!!

''')
            trial = 3
            Pscore = 0
            Cscore = 0
            try_again()
        else:
            print('''
        !!! You lost the Game !!!

''')
            trial = 3
            Pscore = 0
            Cscore = 0
            try_again()

main()