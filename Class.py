
import random
class Game:
    def __init__(self):
        # points_alt to jest do liczenia punktów w przypadku gdy jest as i trzeba go liczyć jako 1 a nie 11
        self.player_points = 0
        self.player_points_alt = 0
        # is_A_in_player_cards to jest do sprawdzania czy w kartach gracza jest as, potrzebne do liczenia punktów gdy gracz ma więcej niż 2 karty
        self.is_A_in_player_cards = False
        self.AI_points = 0
        self.AI_points_alt = 0
        self.is_A_in_AI_cards = False
        # Ai_cards i player_cards to są listy w których będą przechowywane karty gracza i AI, potrzebne do grafiki i liczenia punktów
        self.Ai_cards = []
        self.player_cards = []
        # player_used_graphic i AI_used_graphic to są listy w których będą przechowywane grafiki kart gracza i AI, potrzebne do dodawania nowych kart do grafiki
        self.player_used_graphic = []
        self.AI_used_graphic = []
        # cards_number to jest słownik w którym przechowywana jest liczba kart danego rodzaju, potrzebne do losowania kart i sprawdzania czy dana karta jest jeszcze dostępna
        self.cards_number = {
            "A":4,
            "K":4,
            "Q":4,
            "J":4,
            "10":4,
            "9":4,
            "8":4,
            "7":4,
            "6":4,
            "5":4,
            "4":4,
            "3":4,
            "2":4
        }
        # cards_value to jest słownik w którym przechowywana jest wartość punktowa danej karty, potrzebne do liczenia punktów
        self.cards_value = {
            "A":1,
            "K":10,
            "Q":10,
            "J":10,
            "10":10,
            "9":9,
            "8":8,
            "7":7,
            "6":6,
            "5":5,
            "4":4,
            "3":3,
            "2":2
        }
    def game_start(self):
        # AI draws 2 cards
        for g in range(0,2):
            while len(self.Ai_cards)<2:
                ran = random.randint(0,12)
                counter = 0
                for char,num in self.cards_number.items():
                    if counter == ran:
                        if num > 0:
                            if char == 'A':
                                self.is_A_in_AI_cards = True
                                if self.AI_points_alt == 0:
                                    self.AI_points_alt = self.AI_points
                                if self.AI_points + 11 > 21 and self.is_A_in_AI_cards == True:
                                    self.AI_points = self.AI_points + 1
                                    self.AI_points_alt = self.AI_points_alt + 1
                                    self.cards_number[char] = self.cards_number[char] - 1
                                    self.Ai_cards.append(char)
                                    added_card = char
                                    break
                                else:
                                    self.AI_points = self.AI_points + 11
                                    self.AI_points_alt = self.AI_points_alt + self.cards_value[char]
                                    self.cards_number[char] = self.cards_number[char] - 1
                                    self.Ai_cards.append(char)
                                    added_card = char
                                    break     
                            self.AI_points = self.AI_points + self.cards_value[char]
                            if self.is_A_in_AI_cards == True:
                                self.AI_points_alt = self.AI_points_alt + self.cards_value[char]
                            self.cards_number[char] = self.cards_number[char] - 1
                            self.Ai_cards.append(char)
                            added_card = char
                            break
                        else:
                            ran = (ran + 1) % 12
                            continue
                    else:
                        counter += 1
                        continue
        # AI cards graphic
        self.AI_graphics = ['┌─────────┐ ┌─────────┐',f'│xxxxxxxxx│ │{self.Ai_cards[1]}        │','│xxxxxxxxx│ │         │','│xxxxxxxxx│ │         │',f'│xxxxxxxxx│ │        {self.Ai_cards[1]}│','└─────────┘ └─────────┘']
        self.AI_graphics_2 = ['┌─────────┐ ┌─────────┐',f'│xxxxxxxxx│ │{self.Ai_cards[1]}       │','│xxxxxxxxx│ │         │','│xxxxxxxxx│ │         │',f'│xxxxxxxxx│ │       {self.Ai_cards[1]}│','└─────────┘ └─────────┘']
        if self.Ai_cards[1] == '10':
            self.AI_used_graphic = self.AI_graphics_2
            for line in self.AI_graphics_2:
                print(line)
        else:
            self.AI_used_graphic = self.AI_graphics
            for line in self.AI_graphics:
                print(line)
        # Player draws two cards
        for g in range(0,2):
            while len(self.player_cards)<2:
                ran = random.randint(0,12)
                counter = 0
                for char,num in self.cards_number.items():
                    if counter == ran:
                        if num > 0:
                            if char == 'A':
                                self.is_A_in_player_cards = True
                                if self.player_points_alt == 0:
                                    self.player_points_alt = self.player_points
                                if self.player_points + 11 > 21 and self.is_A_in_player_cards == True:
                                    self.player_points = self.player_points + 1
                                    self.player_points_alt = self.player_points_alt + 1
                                    self.cards_number[char] = self.cards_number[char] - 1
                                    self.player_cards.append(char)
                                    added_card = char
                                    break
                                else:
                                    self.player_points = self.player_points + 11
                                    self.player_points_alt = self.player_points_alt + self.cards_value[char]
                                    self.cards_number[char] = self.cards_number[char] - 1
                                    self.player_cards.append(char)
                                    added_card = char
                                    break     
                            self.player_points = self.player_points + self.cards_value[char]
                            if self.is_A_in_player_cards == True:
                                self.player_points_alt = self.player_points_alt + self.cards_value[char]
                            self.cards_number[char] = self.cards_number[char] - 1
                            self.player_cards.append(char)
                            added_card = char
                            break
                        else:
                            ran = (ran + 1) % 12
                            continue
                    else:
                        counter += 1
                        continue
        # Player cards graphic
        self.player_graphics = ['┌─────────┐ ┌─────────┐',f'│{self.player_cards[0]}        │ │{self.player_cards[1]}        │','│         │ │         │','│         │ │         │',f'│        {self.player_cards[0]}│ │        {self.player_cards[1]}│','└─────────┘ └─────────┘']
        self.player_graphics_1 = ['┌─────────┐ ┌─────────┐',f'│{self.player_cards[0]}       │ │{self.player_cards[1]}        │','│         │ │         │','│         │ │         │',f'│       {self.player_cards[0]}│ │        {self.player_cards[1]}│','└─────────┘ └─────────┘']
        self.player_graphics_2 = ['┌─────────┐ ┌─────────┐',f'│{self.player_cards[0]}        │ │{self.player_cards[1]}       │','│         │ │         │','│         │ │         │',f'│        {self.player_cards[0]}│ │       {self.player_cards[1]}│','└─────────┘ └─────────┘']
        self.player_graphics_3 = ['┌─────────┐ ┌─────────┐',f'│{self.player_cards[0]}       │ │{self.player_cards[1]}       │','│         │ │         │','│         │ │         │',f'│       {self.player_cards[0]}│ │       {self.player_cards[1]}│','└─────────┘ └─────────┘']
        print('\n\n')
        if self.player_cards[0] == '10' and self.player_cards[1] != '10':
            self.player_used_graphic = self.player_graphics_1
            for line in self.player_graphics_1:
                print(line)
        elif self.player_cards[1] == '10' and self.player_cards[0] != '10':
            self.player_used_graphic = self.player_graphics_2
            for line in self.player_graphics_2:
                print(line)
        elif self.player_cards[0] == '10' and self.player_cards[1] == '10':
            self.player_used_graphic = self.player_graphics_3
            for line in self.player_graphics_3:
                print(line)
        else:
            self.player_used_graphic = self.player_graphics
            for line in self.player_graphics:
                print(line)
        if self.is_A_in_player_cards == True:
            print(f'\n points: {self.player_points}/{self.player_points_alt}')
        else:
            print(f'\n points: {self.player_points}')
    def draw_card(self):
        for g in range(0,1):
            des = len(self.player_cards) + 1
            while len(self.player_cards) < des:
                ran = random.randint(0,12)
                counter = 0
                for char,num in self.cards_number.items():
                    if counter == ran:
                        if num > 0:
                            if char == 'A':
                                self.is_A_in_player_cards = True
                                if self.player_points_alt == 0:
                                    self.player_points_alt = self.player_points
                                if self.player_points + 11 > 21 and self.is_A_in_player_cards == True:
                                    self.player_points = self.player_points + 1
                                    self.player_points_alt = self.player_points_alt + 1
                                    self.cards_number[char] = self.cards_number[char] - 1
                                    self.player_cards.append(char)
                                    added_card = char
                                    break
                                else:
                                    self.player_points = self.player_points + 11
                                    self.player_points_alt = self.player_points_alt + self.cards_value[char]
                                    self.cards_number[char] = self.cards_number[char] - 1
                                    self.player_cards.append(char)
                                    added_card = char
                                    break     
                            self.player_points = self.player_points + self.cards_value[char]
                            if self.is_A_in_player_cards == True:
                                self.player_points_alt = self.player_points_alt + self.cards_value[char]
                            self.cards_number[char] = self.cards_number[char] - 1
                            self.player_cards.append(char)
                            added_card = char
                            break
                        else:
                            ran = (ran + 1) % 12
                            continue
                    else:
                        counter += 1
                        continue
        # Player cards graphic
        if added_card == '10':
            self.player_used_graphic[0] = self.player_used_graphic[0] + ' ┌─────────┐'
            self.player_used_graphic[1] = self.player_used_graphic[1] + f' │{self.player_cards[len(self.player_cards)-1]}       │'
            self.player_used_graphic[2] = self.player_used_graphic[2] + ' │         │'
            self.player_used_graphic[3] = self.player_used_graphic[3] + ' │         │'
            self.player_used_graphic[4] = self.player_used_graphic[4] + f' │       {self.player_cards[len(self.player_cards)-1]}│'
            self.player_used_graphic[5] = self.player_used_graphic[5] + ' └─────────┘'
        else:
            self.player_used_graphic[0] = self.player_used_graphic[0] + ' ┌─────────┐'
            self.player_used_graphic[1] = self.player_used_graphic[1] + f' │{self.player_cards[len(self.player_cards)-1]}        │'
            self.player_used_graphic[2] = self.player_used_graphic[2] + ' │         │'
            self.player_used_graphic[3] = self.player_used_graphic[3] + ' │         │'
            self.player_used_graphic[4] = self.player_used_graphic[4] + f' │        {self.player_cards[len(self.player_cards)-1]}│'
            self.player_used_graphic[5] = self.player_used_graphic[5] + ' └─────────┘'
        print('\n\n')
        for line in self.AI_used_graphic:
            print(line)
        print('\n\n')
        for line in self.player_used_graphic:
            print(line)
        if self.is_A_in_player_cards == True:
            print(f'\n points: {self.player_points}/{self.player_points_alt}')
        else:
            print(f'\n points: {self.player_points}')
    def pass_(self):
        # tera robisz tak że grafike ai robisz na nowo 4 opcje pamiętaj o 10 i braku xxxxxxx wtedy sprawdxzisz czy dobrze liczy punkty
        self.AI_graphics = ['┌─────────┐ ┌─────────┐',f'│{self.Ai_cards[0]}        │ │{self.Ai_cards[1]}        │','│         │ │         │','│         │ │         │',f'│        {self.Ai_cards[0]}│ │        {self.Ai_cards[1]}│','└─────────┘ └─────────┘']
        self.AI_graphics_1 = ['┌─────────┐ ┌─────────┐',f'│{self.Ai_cards[0]}       │ │{self.Ai_cards[1]}        │','│         │ │         │','│         │ │         │',f'│       {self.Ai_cards[0]}│ │        {self.Ai_cards[1]}│','└─────────┘ └─────────┘']
        self.AI_graphics_2 = ['┌─────────┐ ┌─────────┐',f'│{self.Ai_cards[0]}        │ │{self.Ai_cards[1]}       │','│         │ │         │','│         │ │         │',f'│        {self.Ai_cards[0]}│ │       {self.Ai_cards[1]}│','└─────────┘ └─────────┘']
        self.AI_graphics_3 = ['┌─────────┐ ┌─────────┐',f'│{self.Ai_cards[0]}       │ │{self.Ai_cards[1]}       │','│         │ │         │','│         │ │         │',f'│       {self.Ai_cards[0]}│ │       {self.Ai_cards[1]}│','└─────────┘ └─────────┘']
        if self.Ai_cards[0] == '10' and self.Ai_cards[1] != '10':
            self.AI_used_graphic = self.AI_graphics_1
        elif self.Ai_cards[1] == '10' and self.Ai_cards[0] != '10':
            self.AI_used_graphic = self.AI_graphics_2
        elif self.Ai_cards[0] == '10' and self.Ai_cards[1] == '10':
            self.AI_used_graphic = self.AI_graphics_3
        else:
            self.AI_used_graphic = self.AI_graphics
        if self.is_A_in_player_cards == True:
            if self.player_points > 21:
                sett = self.player_points_alt
            else:
                sett = self.player_points
        else:
            sett = self.player_points
        while self.AI_points < sett or (self.is_A_in_AI_cards == True and self.AI_points_alt < sett):
            ran = random.randint(0,12)
            des = len(self.Ai_cards) + 1
            while len(self.Ai_cards) < des:
                counter = 0
                for char,num in self.cards_number.items():
                    if counter == ran:
                        if num > 0:
                            #alt_points to jest do liczenia punktów w przypadku gdy jest as i trzeba go liczyć jako 1 a nie 11
                            if char == 'A':
                                self.is_A_in_AI_cards = True
                                if self.AI_points_alt == 0:
                                    self.AI_points_alt = self.AI_points
                                if self.AI_points + 11 > 21 and self.is_A_in_AI_cards == True:
                                    self.AI_points = self.AI_points + 1
                                    self.AI_points_alt = self.AI_points_alt + 1
                                    self.cards_number[char] = self.cards_number[char] - 1
                                    self.Ai_cards.append(char)
                                    added_card = char
                                    break
                                else:
                                    self.AI_points = self.AI_points + 11
                                    self.AI_points_alt = self.AI_points_alt + self.cards_value[char]
                                    self.cards_number[char] = self.cards_number[char] - 1
                                    self.Ai_cards.append(char)
                                    added_card = char
                                    break     
                            self.AI_points = self.AI_points + self.cards_value[char]
                            if self.is_A_in_AI_cards == True:
                                self.AI_points_alt = self.AI_points_alt + self.cards_value[char]
                            self.cards_number[char] = self.cards_number[char] - 1
                            self.Ai_cards.append(char)
                            added_card = char
                            break
                        else:
                            ran = (ran + 1) % 12
                            continue
                    else:
                        counter += 1
                        continue
            if added_card == '10':
                self.AI_used_graphic[0] = self.AI_used_graphic[0] + ' ┌─────────┐'
                self.AI_used_graphic[1] = self.AI_used_graphic[1] + f' │{self.Ai_cards[len(self.Ai_cards)-1]}       │'
                self.AI_used_graphic[2] = self.AI_used_graphic[2] + ' │         │'
                self.AI_used_graphic[3] = self.AI_used_graphic[3] + ' │         │'
                self.AI_used_graphic[4] = self.AI_used_graphic[4] + f' │       {self.Ai_cards[len(self.Ai_cards)-1]}│'
                self.AI_used_graphic[5] = self.AI_used_graphic[5] + ' └─────────┘'
            else:
                self.AI_used_graphic[0] = self.AI_used_graphic[0] + ' ┌─────────┐'
                self.AI_used_graphic[1] = self.AI_used_graphic[1] + f' │{self.Ai_cards[len(self.Ai_cards)-1]}        │'
                self.AI_used_graphic[2] = self.AI_used_graphic[2] + ' │         │'
                self.AI_used_graphic[3] = self.AI_used_graphic[3] + ' │         │'
                self.AI_used_graphic[4] = self.AI_used_graphic[4] + f' │        {self.Ai_cards[len(self.Ai_cards)-1]}│'
                self.AI_used_graphic[5] = self.AI_used_graphic[5] + ' └─────────┘'
        print('\n\n')
        for line in self.AI_used_graphic:
            print(line)
        print('\n\n')
        for line in self.player_used_graphic:
            print(line)
        # trzeba zrobić żeby jak jest as to pokazywało dwie wartości punktów
        if self.is_A_in_player_cards == True and self.is_A_in_AI_cards == True:
            print(f'\n points: {self.player_points}/{self.player_points_alt}\n AI points: {self.AI_points}/{self.AI_points_alt}')
        elif self.is_A_in_player_cards == True and self.is_A_in_AI_cards == False:
            print(f'\n points: {self.player_points}/{self.player_points_alt}\n AI points: {self.AI_points}')
        elif self.is_A_in_player_cards == False and self.is_A_in_AI_cards == True:
            print(f'\n points: {self.player_points}\n AI points: {self.AI_points}/{self.AI_points_alt}')
        else:
            print(f'\n points: {self.player_points}\n AI points: {self.AI_points}')

   