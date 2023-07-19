import random
from enum import Enum
from flask import abort 
'''
Action enum, represents 3 distinct actions
'''
class Action(Enum):
    FOLD = 0
    CALL = 1
    RAISE = 2

'''
Card class, encapsulates Card functionality
'''
class Card:

  
    def __init__(self, suit, value):
          '''
        Initialized Card class

        Parameters: 
         suit
     '''
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"

class Player:
     '''
        Initializes the Player class

        Parameters:
        name: The name of the player
        chips: The number of chips the player has (default is 1000)
        '''
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
        '''
        Sets the player's hand

        Parameters:
        hand: A list of Card objects representing the player's hand
        '''
        self.hand = hand

    def set_position(self, position):
         '''
        Sets the player's position

        Parameters:
        position: A string representing the player's position
        '''
        self.position = position

    def count_values(self):
         '''
        Counts the occurrence of each card value in the player's hand
        
        Returns:
        A dictionary where keys are card values and values are the number of occurrences of that value in the hand
        '''
        values = [card.value for card in self.hand]
        return {value: values.count(value) for value in values}

    def has_high_card(self):
          '''
        Checks if the player's hand contains any high value cards

        Returns:
        True if the hand contains any high value cards, False otherwise
        '''
        return any(card.value in self.high_values for card in self.hand)
    
    def has_medium_card(self):
         '''
        Checks if the player's hand contains any medium value cards

        Returns:
        True if the hand contains any medium value cards, False otherwise
        '''
        return any(card.value in self.medium_values for card in self.hand)
    
    def has_low_card(self):
         '''
        Checks if the player's hand contains any low value cards

        Returns:
        True if the hand contains any low value cards, False otherwise
        '''
        return any(card.value in self.low_values for card in self.hand)
    
    def has_pair(self):
         '''
        Checks if the player's hand contains a pair
        
        Returns:
        True if the hand contains a pair, False otherwise
        '''
        values = [card.value for card in self.hand]
        return len(set(values)) == 1  # Pair has two same value cards

    def is_suited(self):
         '''
        Checks if the player's hand is suited (all cards have the same suit)
        
        Returns:
        True if the hand is suited, False otherwise
        '''
        suits = [card.suit for card in self.hand]
        return len(set(suits)) == 1  # Suited if all suits are the same

    def has_potential_straight(self):
         '''
        Checks if the player's hand has potential for a straight (values are consecutive)
        
        Returns:
        True if the hand has potential for a straight, False otherwise
        '''
        values = [self.values.index(card.value) for card in self.hand]
        return max(values) - min(values) == 1  # Potential straight if values are consecutive

    def calculate_hand_strength(self):
        '''
        Calculates the strength of the player's hand based on the card values and combinations
        
        Returns:
        An integer score representing the hand's strength
        '''
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

    def take_action(self, min_bet, pot_size):
         '''
        Decides the optimal action for the player to take based on the hand's strength, the player's position, and the pot odds

        Parameters:
        min_bet: The minimum bet the player must place to stay in the game
        pot_size: The total amount of chips in the pot

        Returns:
        The optimal action for the player to take, as an Action enum
        '''
        
        # If player doesn't have enough chips for the minimum bet, they must fold
        if self.chips < min_bet:
            return Action.FOLD

        hand_strength = self.calculate_hand_strength()
        # Calculate the pot odds
        pot_odds = min_bet / pot_size if pot_size != 0 else 1

        # Based on the strength of hand and position, decide the action
        if self.position in ['Small Blind', 'Big Blind', 'UTG']:  # Early position
            if hand_strength >= 7:  # Strong hand
                return Action.RAISE
            else:
                # If pot odds are high, consider calling even with a weaker hand
                if pot_odds > 0.5:
                    return Action.CALL
                else:
                    return Action.FOLD
        elif self.position in ['UTG+1', 'UTG+2']:  # Middle position
            if hand_strength >= 6:  # Medium or strong hand
                return Action.CALL
            else:
                # If pot odds are high, consider calling even with a weaker hand
                if pot_odds > 0.5:
                    return Action.CALL
                else:
                    return Action.FOLD
        else:  # Late position
            if hand_strength > 4:  # Medium or strong hand
                return Action.CALL
            else:  # Low card
                # If pot odds are high, consider calling even with a weaker hand
                if pot_odds > 0.5:
                    return Action.CALL
                else:
                    return Action.FOLD

class PokerFlop:
     '''
        Initializes the PokerFlop class

        Parameters:
        players: A list of Player objects participating in the game
        '''
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def __init__(self, players):
          '''
        Initializes the PokerFlop class

        Parameters:
        players: A list of Player objects participating in the game
        '''
        self.players = players
        self.deck = [Card(suit, value) for suit in self.suits for value in self.values]
        self.state = {
            'rounds_played': 0,
            'current_player': None,
            'pot': 0,
            'player_states': {player.name: {'chips': player.chips, 'hand': [], 'action': None, 'position': None} for player in self.players}
        }

    def deal_cards(self):
        '''
        Deals cards to each player in the game
        '''
        for player in self.players:
            player.hand = [self.draw_card(), self.draw_card()]

    def draw_card(self):
         '''
        Draws a random card from the deck

        Returns:
        A Card object representing the drawn card
        '''
        return self.deck.pop(random.randint(0, len(self.deck) - 1))

    def play_round(self):
        '''
        Plays a round of the poker game
        '''
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
            action = player.take_action(min_bet, self.state['pot'])
            print(f"{player.name} decided to {action}")

            self.state['current_player'] = player.name
            self.state['player_states'][player.name]['hand'] = [str(card) for card in player.hand]
            self.state['player_states'][player.name]['action'] = action.name
            self.state['player_states'][player.name]['position'] = player.position

        self.state['rounds_played'] += 1

        return self.state

    def set_positions(self):
         '''
        Sets the positions for each player in the game
        '''
        # Rotate the players' positions.
        self.players = self.players[1:] + self.players[:1]
        positions = ['Small Blind', 'Big Blind', 'UTG', 'Hijack', 'Cut-off', 'Dealer']
        for player, position in zip(self.players, positions):
            player.position = position  # Assign position as a string.
    
    def get_optimal_action(self, player_name, min_bet):
        '''
        Gets the optimal action for a player

        Parameters:
        player_name: The name of the player
        min_bet: The minimum bet the player must place to stay in the game

        Returns:
        The optimal action for the player to take, as an Action enum
        '''

        player = next(player for player in self.players if player.name == player_name)
        return player.take_action(min_bet, self.state['pot'])

def player_action(player_name, hand, position, min_bet):
     '''
    Determines the optimal action for a player based on their hand and position

    Parameters:
    player_name: The name of the player
    hand: A list of Card objects representing the player's hand
    position: A string representing the player's position
    min_bet: The minimum bet the player must place to stay in the game

    Returns:
    A tuple containing the game state and the optimal action for the player
    '''
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
    '''
    Determines the optimal action for a player based on their hand and position

    Parameters:
    player_name: The name of the player
    card1_value: The value of the first card in the player's hand
    card2_value: The value of the second card in the player's hand
    are_suited: A boolean indicating whether the two cards in the player's hand are suited
    position: A string representing the player's position
    min_bet: The minimum bet the player must place to stay in the game

    Returns:
    A tuple containing the game state and the optimal action for the player
    '''
   
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
