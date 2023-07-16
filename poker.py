import random
from enum import Enum
from flask import abort 

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
        self.low_values = ['2', '3', '4', '5', '6', '7', '8']
    def set_hand(self, hand):
        self.hand = hand

    def set_position(self, position):
        self.position = position

    def count_values(self):
        values = [card.value for card in self.hand]
        return {value: values.count(value) for value in values}

    def has_high_card(self):
        return any(card.value in self.high_values for card in self.hand)
    
    def has_medium_card(self):
        return any(card.value in self.medium_values for card in self.hand)
    
    def has_low_card(self):
        return any(card.value in self.low_values for card in self.hand)
    
    def has_pair(self):
        values = [card.value for card in self.hand]
        return len(set(values)) == 1  # Pair has two same value cards

    def is_suited(self):
        suits = [card.suit for card in self.hand]
        return len(set(suits)) == 1  # Suited if all suits are the same

    def has_potential_straight(self):
        values = [self.values.index(card.value) for card in self.hand]
        return max(values) - min(values) == 1  # Potential straight if values are consecutive

    def calculate_hand_strength(self):
        hand_strength = 0
        if self.has_pair():
            pair_value = self.hand[0].value  # Since it's a pair, we can just take the value of the first card
            if pair_value in self.high_values:
                hand_strength = 8  # High pair
            elif pair_value in self.medium_values:
                hand_strength = 6  # Medium pair
            else:
                hand_strength= 4  # Low pair
        elif self.is_suited():
            if self.has_high_card():
                hand_strength = 7  # Suited high card
            elif self.has_medium_card():
                hand_strength = 5  # Suited medium card
            else:
                hand_strength = 3  # Suited low card
        elif self.has_potential_straight():
            if self.has_high_card():
                hand_strength = 6  # Potential high straight
            elif self.has_medium_card():
                hand_strength = 4  # Potential medium straight
            else:
                hand_strength = 2  # Potential low straight
        else:
            if self.has_high_card():
                hand_strength = 5  # High card
            elif self.has_medium_card():
                hand_strength = 3  # Medium card
            else:
                hand_strength = 1  # Low card

        return hand_strength

    def take_action(self, min_bet):
        # If player doesn't have enough chips for the minimum bet, they must fold
        if self.chips < min_bet:
            return Action.FOLD

        hand_strength = self.calculate_hand_strength()

        # Based on the strength of hand and position, decide the action
        if self.position in ['Small Blind', 'Big Blind', 'UTG']:  # Early position
            if hand_strength >= 7:  # Strong hand
                return Action.RAISE
            else:
                return Action.FOLD
        elif self.position in ['UTG+1', 'UTG+2']:  # Middle position
            if hand_strength >= 6:  # Medium or strong hand
                return Action.CALL
            else:
                return Action.FOLD
        else:  # Late position
            if hand_strength > 4:  # Medium or strong hand
                return Action.CALL
            else:  # Low card
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
    
    def get_optimal_action(self, player_name, min_bet):
        player = next(player for player in self.players if player.name == player_name)
        return player.take_action(min_bet)

def player_action(player_name, hand, position, min_bet):
    player = Player(player_name)
    player.set_hand(hand)  # Set player's hand. Now `hand` is a list of `Card` objects
    player.set_position(position)  # Set player's position

    game = PokerFlop([player])  # Create a game with just the one player

    optimal_action = game.get_optimal_action(player_name, min_bet)  # Get optimal action

    game_state = game.state
    game_state['current_player'] = player_name
    game_state['player_states'][player_name]['hand'] = [str(card) for card in player.hand]
    game_state['player_states'][player_name]['position'] = position
    game_state['player_states'][player_name]['action'] = optimal_action.name

    return game_state, optimal_action

def get_action_from_input(player_name, card1_value, card2_value, are_suited, position, min_bet):
    # Check if the player is trying to enter two cards that are the same and suited
    if card1_value == card2_value and are_suited:
        abort(400, description="Invalid input: You cannot have two identical cards that are suited.")

    # Create Card objects for the hand
    card1 = Card('Spades', card1_value)
    card2 = Card('Clubs', card2_value)

    if are_suited:
        # If the cards are suited, they should have the same suit
        card2.suit = 'Spades'

    # Call the player_action function
    game_state, optimal_action = player_action(player_name, [card1, card2], position, min_bet)

    return game_state, optimal_action


# players = [Player(f'Player {i}', 1000) for i in range(1, 7)]
# game = PokerFlop(players)
# game_state = game.play_round()

# player_name = 'Player 1'
# game_state, optimal_action = player_action(player_name, [('2', 'Clubs'), ('3', 'Spades')], 'Small Blind', 10)
# #print the player_state 
# print(game_state['player_states'][player_name])
# print(optimal_action)

# print(get_action_from_input('Player 1', 'K', 'K', False, 'Small Blind', 10))
    
    
    
    