import Class
import game_rules
import os
import time
while True:
    with open('high_score.txt', 'r') as f:
        high_score = int(f.read())
    os.system('clear')
    print('--------------------------')
    print('       BLACK JACK')
    print('--------------------------')
    print(f'High Score: {high_score}')
    print('\nSELECT AN OPTION')
    choice = int(input('1. Start Game\n2. Quit\n'))
    if choice == 2:
        break
    if choice == 1:
        money = 1000
        while True:
            if money > high_score:
                with open('high_score.txt', 'w') as f:
                    f.write(str(money))
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
                try:
                    choice_stake = int(input('Stake: '))
                except ValueError:
                    print('WRONG INPUT')
                    time.sleep(3)
                    continue
                os.system('clear')
                if choice_stake > money:
                    print('YOU HAVE NO MONEY')
                    time.sleep(3)
                    continue
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