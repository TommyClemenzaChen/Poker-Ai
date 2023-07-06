import random
from enum import Enum

class Action(Enum):
    FOLD = 0
    CALL = 1
    RAISE = 2

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.chips = 1000  

    def take_action(self): # Naive or CFR Approach here
  
        pass

class PokerGame:
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def __init__(self, players):
        self.players = players
        self.deck = [Card(suit, value) for suit in self.suits for value in self.values]

    def deal_cards(self):
        for player in self.players:
            player.hand = [self.draw_card(), self.draw_card()]
    
    def draw_card(self):
        return self.deck.pop(random.randint(0, len(self.deck) - 1))

    def play_round(self):
        self.deck = [Card(suit, value) for suit in self.suits for value in self.values]
        self.deal_cards()
        for player in self.players:
            print(f"{player.name}'s hand: {player.hand[0]}, {player.hand[1]}")
            player.take_action()

    def play_game(self, num_rounds):
        for _ in range(num_rounds):
            self.play_round()
            print("----")

players = [Player('Player 1'), Player('Player 2')]
game = PokerGame(players)
game.play_game(5)
