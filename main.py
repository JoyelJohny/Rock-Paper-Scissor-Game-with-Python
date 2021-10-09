import random
from graphic_view import *
from intro import *
from count import *
trial = 3
Pscore = 0
Cscore = 0
intro()
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

********************************************************************************************************
''')
        else:
            print('''
        !!! You lost the Game !!!

*********************************************************************************************************        
''')

main()
