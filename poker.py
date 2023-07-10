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
    def __init__(self, name, chips=1000):
        self.name = name
        self.hand = []
        self.chips = chips
        self.position = None
        self.values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

        self.high_values = ['J', 'Q', 'K', 'A']  # consider these as high value cards
        self.medium_values = ['9', '10']  # consider these as medium value cards
    
    def count_values(self):
        values = [card.value for card in self.hand]
        return {value: values.count(value) for value in values}

    def has_pair(self):
        counts = self.count_values()
        return 2 in counts.values()

    def has_two_pair(self):
        counts = self.count_values()
        return list(counts.values()).count(2) >= 2

    def has_three_of_a_kind(self):
        counts = self.count_values()
        return 3 in counts.values()

    def has_straight(self):
        values = [self.values.index(card.value) for card in self.hand]
        values.sort()
        return max(values) - min(values) == 4 and len(set(values)) == 5

    def calculate_hand_strength(self):
        if self.has_straight():
            return 5
        elif self.has_three_of_a_kind():
            return 4
        elif self.has_two_pair():
            return 3
        elif self.has_pair():
            return 2
        else:
            return 1  # High card
    
    def take_action(self, min_bet):
        # If player doesn't have enough chips for the minimum bet, they must fold
        if self.chips < min_bet:
            return Action.FOLD

        # Calculate the strength of hand
        hand_strength = self.calculate_hand_strength()

        # Based on the strength of hand and position, decide the action
        if hand_strength >= 4 and self.position != 'Small Blind' and self.position != 'Big Blind':  # Strong hand and not in blinds
            return Action.RAISE
        elif hand_strength >= 2 and self.position != 'Small Blind' and self.position != 'Big Blind':  # Medium hand and not in blinds
            return Action.CALL
        else:
            return Action.FOLD
        
class PokerFlop:
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def __init__(self, players):
        self.players = players
        self.deck = [Card(suit, value) for suit in self.suits for value in self.values]
        self.state = {
            'rounds_played': 0,
            'current_player': None,
            'pot': 0,
            'player_states': {player.name: {'chips': player.chips, 'hand': [], 'action': None, 'position': None} for player in self.players}
        }

    def deal_cards(self):
        for player in self.players:
            player.hand = [self.draw_card(), self.draw_card()]

    def draw_card(self):
        return self.deck.pop(random.randint(0, len(self.deck) - 1))

    def play_round(self):
        self.deck = [Card(suit, value) for suit in self.suits for value in self.values]
        self.deal_cards()
        self.set_positions()

        min_bet = 10  # This is the big blind
        small_blind_bet = 5  # This is the small blind

        players_in_round = self.players.copy()  # list of players still in the round

        # The player in the small blind position must post the small blind
        players_in_round[0].chips -= small_blind_bet
        self.state['player_states'][players_in_round[0].name]['chips'] = players_in_round[0].chips
        self.state['pot'] += small_blind_bet

        # The player in the big blind position must post the big blind
        players_in_round[1].chips -= min_bet
        self.state['player_states'][players_in_round[1].name]['chips'] = players_in_round[1].chips
        self.state['pot'] += min_bet

        # Players decide their action
        for player in players_in_round:
            print(f"{player.name}'s hand: {player.hand[0]}, {player.hand[1]} at {player.position}")
            action = player.take_action(min_bet)
            print(f"{player.name} decided to {action}")

            self.state['current_player'] = player.name
            self.state['player_states'][player.name]['hand'] = [str(card) for card in player.hand]
            self.state['player_states'][player.name]['action'] = action.name
            self.state['player_states'][player.name]['position'] = player.position

        self.state['rounds_played'] += 1

        return self.state

    def set_positions(self):
        # Rotate the players' positions.
        self.players = self.players[1:] + self.players[:1]
        positions = ['Small Blind', 'Big Blind', 'UTG', 'Hijack', 'Cut-off', 'Dealer']
        for player, position in zip(self.players, positions):
            player.position = position  # Assign position as a string.

players = [Player(f'Player {i}', 1000) for i in range(1, 7)]
game = PokerFlop(players)
game_state = game.play_round()
