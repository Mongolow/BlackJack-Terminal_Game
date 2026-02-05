import Class
# Rozegranie gry (return is_game_won) jak jest wygrana to 'WIN', przegrana 'LOSE', remis 'DRAW'
def game(stake: int):
    game = Class.Game()
    game.game_start()
    def best_score(points, points_alt, has_ace):
        # zwraca najlepszy (największy <=21) wynik lub najmniejszy gdy wszystkie >21
        if has_ace:
            candidates = [points, points_alt]
        else:
            candidates = [points]
        valid = [c for c in candidates if c <= 21]
        if valid:
            return max(valid)
        return min(candidates)
    def is_bust(points, points_alt, has_ace):
        if has_ace:
            return points > 21 and points_alt > 21
        return points > 21
    while True:
        choice = int(input('\n1. STAND\n2. HIT\n'))
        if choice == 2:
            # przegrana podczas dobierania
            game.draw_card()
            if is_bust(game.player_points, game.player_points_alt, game.is_A_in_player_cards):
                return ['LOSE',0]
        if choice == 1:
            # wynik przy STAND
            game.pass_()
            # użyj uproszczonej logiki porównania wyników z uwzględnieniem asa
            if is_bust(game.player_points, game.player_points_alt, game.is_A_in_player_cards):
                return ['LOSE',0]
            if is_bust(game.AI_points, game.AI_points_alt, game.is_A_in_AI_cards):
                return ['WIN',stake*2]
            player_best = best_score(game.player_points, game.player_points_alt, game.is_A_in_player_cards)
            ai_best = best_score(game.AI_points, game.AI_points_alt, game.is_A_in_AI_cards)
            if player_best > ai_best:
                return ['WIN',stake*2]
            elif player_best < ai_best:
                return ['LOSE',0]
            else:
                return ['DRAW',stake]







if __name__ == '__main__':
    wynik = game(100)
    print(wynik)
