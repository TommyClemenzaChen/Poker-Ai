import random
from enum import Enum
from flask import abort 
'''
Action enum, represents 2 distinct actions. There is no CALL action in the preflop round of Poker. 
'''
class Action(Enum):
    FOLD = 0
    RAISE = 1

'''
Card class, encapsulates Card functionality
'''
class Card:

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"

class Player:

    def __init__(self, name, chips=1000):
        '''
        Initialize a player with a name and chips
        '''
        self.name = name
        self.hand = []
        self.chips = chips
        self.position = None
        self.values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.premier_values = ['A'] # consider these as premier cards
        self.high_values = ['K', 'J', 'Q']  # consider these as high value cards
        self.medium_values = ['8', '9', '10']  # consider these as medium value cards
        self.low_values = ['5', '6', '7']  # consider these as low value cards
        self.very_low_values = ['2', '3', '4']  # consider these as very low value cards

    def set_hand(self, hand):
        '''
        Set hand for player
        Parameters:
        hand (List): list of cards
        '''
        self.hand = hand

    def set_position(self, position):
        '''
        Set position for player
        Parameters: 
        position: position of player

        '''
        self.position = position

    def count_values(self):
        '''
        Count the number of cards with each value in the hand
        Returns: 
        (dict): Dictionary with keys as values and values as counts
        '''
        values = [card.value for card in self.hand]
        return {value: values.count(value) for value in values}
    def has_premier_card(self):
         """
         This function checks if a player has a premier card in their hand.


         Returns:
         boolean: Whether a premier card is present in the player's hand.
        """
        return any(card.value in self.premier_values for card in self.hand)
    
    def has_high_card(self):
        """
         This function checks if a player has a high card in their hand.


         Returns:
         boolean: Whether a high card is present in the player's hand.
        """
        return any(card.value in self.high_values for card in self.hand)

    def has_medium_card(self):
         """
         This function checks if a player has a medium card in their hand.

         Returns:
         boolean: Whether a medium card is present in the player's hand.
        """
        return any(card.value in self.medium_values for card in self.hand)

    def has_low_card(self):
         """
         This function checks if a player has a low card in their hand.


         Returns:
         boolean: Whether a low card is present in the player's hand.
        """
        return any(card.value in self.low_values for card in self.hand)
    
    def has_very_low_card(self):
         """
         This function checks if a player has a very low card in their hand.


         Returns:
         boolean: Whether a very low card is present in the player's hand.
        """
        return any(card.value in self.very_low_values for card in self.hand)

    def has_pair(self):
         """
         This function checks if a player has a pair in their hand.


         Returns:
         boolean: Whether a pair is present in the player's hand.
        """
        values = [card.value for card in self.hand]
        return len(set(values)) == 1  # Pair has two same value cards

    def is_suited(self):
         """
         This function checks if a player's hand is suited. A hand is suited if all cards have the same suit.


         Returns:
         boolean: Whether a player's hand is suited.
        """
        suits = [card.suit for card in self.hand]
        return len(set(suits)) == 1  # Suited if all suits are the same

    def has_potential_straight(self):
        values = [self.values.index(card.value) for card in self.hand]
        return max(values) - min(values) == 1  # Potential straight if values are consecutive
    
    def has_double_high_card(self):
        if ((self.hand[0].value in self.high_values or self.hand[0].value in self.premier_values) and (self.hand[1].value in self.high_values or self.hand[1].value in self.premier_values)):
            return True
        return False

    def calculate_hand_strength(self):
         """
         This function computes the hand strength of a particular hand. The hand strength is a number between 1 and 10, with 10 being the highest. The hand strength is computed as follows:
            - If the player has a pair, the hand strength is 10. If the pair is a premier pair, the hand strength is 10. If the pair is a high pair, the hand strength is 9. If the pair is a medium pair, the hand strength is 8. If the pair is a low pair, the hand strength is 7. If the pair is a very low pair, the hand strength is 6.
            - If the player has two high cards that are suited, the hand strength is 7. If the player has two high cards that are off-suited, the hand strength is 5. If the player has two medium cards that are suited, the hand strength is 5. If the player has two medium cards that are off-suited, the hand strength is 3. If the player has a high card and a medium card that are suited, the hand strength is 5. If the player has a high card and a medium card that are off-suited, the hand strength is 3. If the player has a high card and a low card that are suited, the hand strength is 4. If the player has a high card and a low card that are off-suited, the hand strength is 2. If the player has two low cards that are suited, the hand strength is 3. If the player has two low cards that are off-suited, the hand strength is 1.

         Returns:
         (int) The evaluated hand strength of the player's hand.
        """
        hand_strength = 0
        if self.has_pair():
            pair_value = self.hand[0].value  # Since it's a pair, we can just take the value of the first card
            if pair_value in self.premier_values:
                hand_strength = 10
            elif pair_value in self.high_values:
                hand_strength = 9  # High pair
            elif pair_value in self.medium_values:
                hand_strength = 8  # Medium pair
            elif pair_value in self.low_values:
                hand_strength = 7  # Low pair
            else:
                hand_strength = 6 # Very low pair

        elif self.has_double_high_card():
            hand_strength = 7

        elif self.is_suited():
            if self.has_premier_card():
                hand_strength = 8
                if(self.has_low_card()):
                    hand_strength = 7 # Suited very low card
                elif(self.has_very_low_card()):
                    hand_strength = 6 # Suited very low card
            elif self.has_high_card():
                hand_strength = 7  # Suited high card
                if(self.has_low_card()):
                    hand_strength = 6 # Suited very low card
                elif(self.has_very_low_card()):
                    hand_strength = 5 # Suited very low card
            
            elif self.has_medium_card():
                hand_strength = 5  # Suited medium card
                if(self.has_low_card()):
                    hand_strength = 4 # Suited very low card
                elif(self.has_very_low_card()):
                    hand_strength = 3 # Suited very low card
                
            elif self.has_potential_straight():
                if self.has_premier_card():
                    hand_strength = 8
                elif self.has_high_card():
                    hand_strength = 7  # Suited high card
                elif self.has_medium_card():
                    hand_strength = 6 # Suited very low card
                elif self.has_low_card():
                    hand_strength = 4  # Suited medium card
                elif self.has_very_low_card():
                    if self.has_low_card():
                        hand_strength = 4  # Suited medium card
                    else:
                        hand_strength = 3  # Suited medium card
                else:
                    hand_strength = 3  # Suited low card
            
            else:
                hand_strength = 3  # Suited low card
                
        elif self.has_potential_straight():
            if self.has_premier_card():
                hand_strength = 8
            elif self.has_high_card():
                hand_strength = 7  # Potential high straight
            elif self.has_medium_card():
                hand_strength = 4  # Potential medium straight
            else:
                hand_strength = 2  # Potential low straight

        else: # off-suited high card starting hands
            if self.has_premier_card():
                hand_strength = 7
                if(self.has_medium_card()):
                    hand_strength = 6 # Has very low card
                elif(self.has_low_card()):
                    hand_strength = 3 # Has very low card
                elif(self.has_very_low_card()):
                    hand_strength = 2 # Has very low card
            elif self.has_high_card():
                hand_strength = 5  # High card
                if(self.has_medium_card()):
                    hand_strength = 4 # Has very low card
                elif(self.has_low_card()):
                    hand_strength = 3 # Has very low card
                elif(self.has_very_low_card()):
                    hand_strength = 2 # Has very low card
            elif self.has_medium_card():
                hand_strength = 3  # Medium card
            else:
                hand_strength = 1  # Low card

        return hand_strength

    def take_action(self, min_bet, pot_size):
         """
         This function returns the optimal action for a player based on their hand strength, position, and pot odds.
        Parameters:
        (int) min_bet: The minimum bet to stay in the game.
        (int) pot_size: The size of the pot.

         Returns:
         (Action, str): A tuple of (Action, explanation) where Action is an Action enum corresponding to the optimal action and explanation is a string explaining the action.
        """
        # If player doesn't have enough chips for the minimum bet, they must fold
        if self.chips < min_bet:
            return Action.FOLD, "Not enough chips for the minimum bet, must fold."

        hand_strength = self.calculate_hand_strength()
        # Calculate the pot odds
        pot_odds = min_bet / pot_size if pot_size != 0 else 1

        # Based on the strength of hand and position, decide the action
        
        if self.position in ['UTG','Hijack']:  # Early position
            if hand_strength >= 7:  # Strong hand
                return Action.RAISE, "In early position with a strong hand, it's a good strategy to raise."
            elif pot_odds > 0.5:  # If pot odds are high
                return Action.FOLD, "Even though in early position, the pot odds are not favorable, so it's better to fold."
            else:
                return Action.FOLD, "In early position with a weak hand, it's a good strategy to fold."
        elif self.position in ['Cut-off', 'BTN']:  # Middle position
            if hand_strength >= 6:  # Medium or strong hand
                return Action.RAISE, "In middle position with a medium or strong hand, it's a good strategy to raise."
            elif pot_odds > 0.5:  # If pot odds are high
                return Action.FOLD, "Even though in middle position, the pot odds are not favorable, so it's better to fold."
            else:
                return Action.FOLD, "In middle position with a weak hand, it's a good strategy to fold."
        else:  # Late position
            if hand_strength >= 4:  # Medium or strong hand
                return Action.RAISE, "In late position with a medium or strong hand, it's a good strategy to raise."
            elif pot_odds > 0.5:  # If pot odds are high
                return Action.FOLD, "Even though in late position, the pot odds are not favorable, so it's better to fold."
            else:  # Low card
                return Action.FOLD, "In late position with a low card, it's a good strategy to fold."

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
         """
         This function deals cards to a player. Each player is dealt two cards.
 
        """
        for player in self.players:
            player.hand = [self.draw_card(), self.draw_card()]

    def draw_card(self):
         """
         This function draws a random card from the deck.

         Returns:
            (Card): A random card from the deck.
        """
        return self.deck.pop(random.randint(0, len(self.deck) - 1))

    def play_round(self):
         """
         This function plays a round of poker. A round consists of the following:
            - The player in the small blind position must post the small blind.
            - The player in the big blind position must post the big blind.
            - Players decide their action.
            - The round ends when all players have taken an action.


         Returns:
            (dict): A dictionary containing the state of the game after the round has been played.
        """
        self.deck = [Card(suit, value) for suit in self.suits for value in self.values]
        self.deal_cards()
        self.set_positions()

        # pod = SB + BB + bet_size
        min_bet = 2*big_blind_bet  # This is the big blind
        small_blind_bet = 5  # This is the small blind
        big_blind_bet = 2*small_blind_bet
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
            action, explanation = player.take_action(min_bet, self.state['pot'])
            print(f"{player.name} decided to {action} because {explanation}")

            self.state['current_player'] = player.name
            self.state['player_states'][player.name]['hand'] = [str(card) for card in player.hand]
            self.state['player_states'][player.name]['action'] = action.name
            self.state['player_states'][player.name]['position'] = player.position

        self.state['rounds_played'] += 1

        return self.state

    def set_positions(self):
         """
         This function assigns positions to players. The positions are as follows:
            - Small Blind
            - Big Blind
            - UTG
            - Hijack
            - Cut-off
            - BTN         
        """
        # Rotate the players' positions.
        self.players = self.players[1:] + self.players[:1]
        positions = ['Small Blind', 'Big Blind', 'UTG', 'Hijack', 'Cut-off', 'BTN']
        for player, position in zip(self.players, positions):
            player.position = position  # Assign position as a string.

    def get_optimal_action(self, player_name, min_bet):
         """
         This function returns the optimal action for a player based on their identifier, and the minumum bet. It is effectively a wrapper around the take_action() function in the Player class. 
        Parameters:
        (str) player_name: The name of the player.
        (int) min_bet: The minimum bet to stay in the game.
        Returns:
         (Action, str): A tuple of (Action, explanation) where Action is an Action enum corresponding to the optimal action and explanation is a string explaining the action.
        """
        player = next(player for player in self.players if player.name == player_name)
        return player.take_action(min_bet, self.state['pot'])

def player_action(player_name, hand, position, min_bet):
     """
         This function returns the optimal action for a player based on their hand, identifier, and the minumum bet. It is effectively a wrapper around the get_optimal_action() function in the PokerFlop class. 
        Parameters:
        (str) player_name: The name of the player.
        (int) hand: The hand of the player.
        (int) position: The position of the player.
        (int) min_bet: The minimum bet to stay in the game.
        Returns:
         (dict, Action, str): A tuple of (dict, Action, explanation) where Action is an Action enum corresponding to the optimal action and explanation is a string explaining the action. The first value in the returned tuple is a dictionary encapsulating the game state. 
        """
    player = Player(player_name)
    player.set_hand(hand)  # Set player's hand. Now `hand` is a list of `Card` objects
    player.set_position(position)  # Set player's position

    game = PokerFlop([player])  # Create a game with just the one player

    optimal_action, explanation = game.get_optimal_action(player_name, min_bet)  # Get optimal action

    game_state = game.state
    game_state['current_player'] = player_name
    game_state['player_states'][player_name]['hand'] = [str(card) for card in player.hand]
    game_state['player_states'][player_name]['position'] = position
    game_state['player_states'][player_name]['action'] = optimal_action.name

    return game_state, optimal_action, explanation

def get_action_from_input(player_name, card1_value, card2_value, are_suited, position, min_bet):
     """
         This function returns the game state, optimal action, and explanation for a player based on their hand, cards, determination of whether the hand is suited, position, identifier, and the minumum bet. It is effectively a wrapper around the player_action() function in the PokerFlop class. 
        Parameters:
        (str) player_name: The name of the player.
        (int) card1_value: The value of the first card.
        (int) card2_value: The value of the second card.
        (bool) are_suited: Whether the cards are suited.
        (int) position: The position of the player.
        (int) min_bet: The minimum bet to stay in the game.
        Returns:
         (dict, Action, str): A tuple of (dict, Action, explanation) where Action is an Action enum corresponding to the optimal action and explanation is a string explaining the action. The first value in the returned tuple is a dictionary encapsulating the game state. 
        """
    
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
    game_state, optimal_action, explanation = player_action(player_name, [card1, card2], position, min_bet)

    return game_state, optimal_action, explanation
