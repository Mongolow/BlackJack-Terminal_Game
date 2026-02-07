import Class
import game_rules
import os
import time
while True:
    os.system('clear')
    print('--------------------------')
    print('       BLACK JACK')
    print('--------------------------')
    print('SELECT AN OPTION')
    choice = int(input('1. Start Game\n2. Quit\n'))
    if choice == 2:
        break
    if choice == 1:
        money = 1000
        while True:
            os.system('clear')
            print('------------------------')
            print(f'Money in bank: {money}')
            print('------------------------')
            choice2 = int(input('1.Play\n2.Quit\n'))
            if choice2 == 2:
                break
            if choice == 1:
                os.system('clear')
                if money == 0:
                    print('YOU HAVE NO MONEY')
                    time.sleep(3)
                    break
                choice_stake = int(input('Stake: '))
                os.system('clear')
                if choice_stake > money:
                    print('YOU HAVE NO MONEY')
                    time.sleep(3)
                    break
                money = money - choice_stake
                game_result = game_rules.game(choice_stake)
                money = money + game_result[1]
                print(f'\n{game_result[0]}')
                choice3 = input('\nPRESS ENTER TO CONINUE')
            else:
                print('WRONG INPUT')
                time.sleep(3)
    else:
        print('WRONG INPUT')
        time.sleep(3)

