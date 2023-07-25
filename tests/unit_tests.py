# File: unit_tests.py
# This file contains unit tests to ensure functionality of the Player and Card classes, along with
# the get_action_from_input function.
# These are unit tests, not integration tests. They are meant to test the functionality of individual
# components of the program, not the program as a whole.


import argparse
import unittest
import time
from poker import Player, Action, Card, get_action_from_input


'''
Unit tests for Card class, asserting that a card is created with the correct suit and value
'''
class TestCard(unittest.TestCase):
    def setUp(self):
        print(f'\nRunning test: {self._testMethodName}...')
    
    def tearDown(self):
        print('Test complete.')
        time.sleep(0.2)

    def test_card_creation(self):
        card = Card('Hearts', '10')
        self.assertEqual(card.suit, 'Hearts')
        self.assertEqual(card.value, '10')

    def test_invalid_card_suit(self):
        with self.assertRaises(AssertionError):
            Card('InvalidSuit', '10')  # Invalid suit

    def test_invalid_card_value(self):
        with self.assertRaises(AssertionError):
            Card('Hearts', 'InvalidValue')  # Invalid value

'''
Unit tests for Player class, asserting that a player is created with the correct name, chips, hand, and position
Additionally, asserts the player's hand is classified correctly by assertion and functionality tests

'''
class TestPlayer(unittest.TestCase):
    def setUp(self):
        print(f'\nRunning test: {self._testMethodName}...')
    
    def tearDown(self):
        print('Test complete.')
        time.sleep(0.2)
    
    def test_player_creation(self):
        player = Player('Player 1')
        self.assertEqual(player.name, 'Player 1')
        self.assertEqual(player.chips, 1000)
        self.assertEqual(player.hand, [])
        self.assertIsNone(player.position)

    def test_invalid_player_name(self):
        with self.assertRaises(AssertionError):
            Player(123)  # Non-string name
        with self.assertRaises(AssertionError):
            Player('')  # Empty name

    def test_set_hand(self):
        player = Player('Player 1')
        hand = [Card('Hearts', '10'), Card('Spades', 'A')]
        player.set_hand(hand)
        self.assertEqual(player.hand, hand)

    def test_set_position(self):
        player = Player('Player 1')
        player.set_position('UTG')
        self.assertEqual(player.position, 'UTG')

    def test_invalid_position(self):
        player = Player('Player 1')
        with self.assertRaises(AssertionError):
            player.set_position('InvalidPosition')  # Invalid position

    def test_has_high_card(self):
        player = Player('Player 1')
        player.set_hand([Card('Hearts', 'J'), Card('Spades', 'A')])  # High card
        self.assertTrue(player.has_high_card())

    def test_has_medium_card(self):
        player = Player('Player 1')
        player.set_hand([Card('Hearts', '10'), Card('Spades', 'A')])
        self.assertTrue(player.has_medium_card())
    
    def test_has_low_card(self):
        player = Player('Player 1')
        player.set_hand([Card('Hearts', '5'), Card('Spades', 'A')])
        self.assertTrue(player.has_low_card())
    
    def test_has_very_low_card(self):
        player = Player('Player 1')
        player.set_hand([Card('Hearts', '2'), Card('Spades', 'A')])
        self.assertTrue(player.has_very_low_card())

    def test_has_premier_card(self):
        player = Player('Player 1')
        player.set_hand([Card('Hearts', 'A'), Card('Spades', 'A')])
        self.assertTrue(player.has_premier_card())
    
    def test_is_suited(self):
        player = Player('Player 1')
        player.set_hand([Card('Hearts', '10'), Card('Hearts', 'A')])
        self.assertTrue(player.is_suited())
    
    def test_has_potential_straight(self):
        player = Player('Player 1')
        player.set_hand([Card('Hearts', '10'), Card('Spades', 'J')])
        self.assertTrue(player.has_potential_straight())
    
    def test_has_double_high_card(self):
        player = Player('Player 1')
        player.set_hand([Card('Hearts', 'J'), Card('Spades', 'J')])
        self.assertTrue(player.has_double_high_card())

    def test_has_pair(self):
        player = Player('Player 1')
        player.set_hand([Card('Hearts', '10'), Card('Spades', '10')])  
        self.assertTrue(player.has_pair())

    '''
    Functionality tests for Player class, to test if the hand_strength and take_action methods are working
    '''

    def test_calculate_hand_strength(self):
        player = Player('Test Player')
        player.set_hand([Card('Hearts', 'A'), Card('Diamonds', 'K')])  
        self.assertIsInstance(player.calculate_hand_strength(), int)

    def test_take_action(self):
        player = Player('Test Player')
        player.set_hand([Card('Hearts', 'A'), Card('Diamonds', 'K')])  
        action, _ = player.take_action(50, 100)  
        self.assertIn(action.name, [action.name for action in Action])  

'''
Unit tests for get_action_from_input function, asserting that the function returns an action
'''

class TestGetActionFromInput(unittest.TestCase):
    def setUp(self):
        print(f'\nRunning test: {self._testMethodName}...')
    
    def tearDown(self):
        print('Test complete.')
        time.sleep(0.2)

    def test_player_action(self):
        game_state, optimal_action, explanation = get_action_from_input('Player 1', '5', '6', True, 'Small Blind', 50)
        self.assertIn(optimal_action.name, [action.name for action in Action])
        self.assertIsInstance(explanation, str)
        self.assertIsInstance(game_state, dict)

    def test_get_action_from_input(self):
        game_state, optimal_action, explanation = get_action_from_input('Player 1', '5', '6', True, 'Small Blind', 50)
        self.assertIn(optimal_action.name, [action.name for action in Action])
        self.assertIsInstance(explanation, str)
        self.assertIsInstance(game_state, dict)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run unit tests for the poker project.')
    parser.add_argument('--test', type=str, help='Specify the test to run')
    args = parser.parse_args()

    if args.test:
        suite = unittest.TestSuite()
        suite.addTest(unittest.makeSuite(globals()[args.test]))
        unittest.TextTestRunner().run(suite)
    else:
        unittest.main()
