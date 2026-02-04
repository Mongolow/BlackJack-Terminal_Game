import Class 
while True:
    print('--------------------------')
    print('       BLACK JACK')
    print('--------------------------')
    print('SELECT AN OPTION')
    choice = int(input('1. Start Game\n2. Quit\n'))
    if choice == 2:
        break
    if choice == 1:
        game = Class.Game()
        game.game_start()
        while True:
            choice = int(input('\n1. STAND\n2. HIT\n'))
            if choice == 2:
                game.draw_card()
                if game.is_A_in_player_cards == True:
                    if game.player_points > 21 and game.player_points_alt > 21:
                        print('\nYOU LOST\n')
                        break
                else:
                    if game.player_points > 21:
                        print('\nYOU LOST\n')
                        break
            if choice == 1:
                # co jeśli karty ai już mają większą wartość niż gracz
                game.pass_()
                # Delete
                if game.is_A_in_AI_cards == True:
                    if game.is_A_in_player_cards == True:
                        if game.AI_points_alt > game.player_points_alt:
                            print('\nYOU LOST\n')
                            break
                        if (game.AI_points == game.player_points_alt) and game.player_points > 21:
                            print('\nDRAW\n')
                            break
                    if game.AI_points > 21 and game.AI_points_alt > 21:
                        print('\nYOU WIN\n')
                        break
                    elif (game.AI_points > game.player_points and game.AI_points <= 21) or (game.AI_points_alt > game.player_points and game.AI_points_alt <= 21):
                        print('\nYOU LOST\n')
                        break
                    elif game.AI_points == game.player_points or game.AI_points_alt == game.player_points:
                        print('\nDRAW\n')
                        break
                else:
                    if game.is_A_in_player_cards == True:
                        if game.is_A_in_AI_cards == False:
                            if game.AI_points > game.player_points_alt and game.player_points > 21 and game.AI_points < 21:
                                print('\nYOU LOST\n')
                                break
                        if (game.AI_points == game.player_points_alt) and game.player_points > 21:
                            print('\nDRAW\n')
                            break
                    if game.AI_points == game.player_points:
                        print('\nDRAW\n')
                        break
                    elif game.AI_points > 21:
                        print('\nYOU WIN\n')
                        break
                    elif game.AI_points > game.player_points and game.AI_points <= 21:
                        print('\nYOU LOST\n')
                        break
                    break