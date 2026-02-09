import Class
import game_rules
import os
import time
while True:
    with open('high_score.bytes', 'rb') as f:
        high_score = f.read().decode('utf-8')
        high_score = int(high_score) if high_score else 0
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
                money2 = money
                money2 = str(money2).encode('utf-8')
                with open('high_score.bytes', 'wb') as f:
                    f.write(money2)
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