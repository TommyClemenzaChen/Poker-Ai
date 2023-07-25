# File: unit_tests.py

import unittest
from poker import Player, Action, Card, get_action_from_input

class TestCard(unittest.TestCase):
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

class TestPlayer(unittest.TestCase):
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

    def test_has_pair(self):
        player = Player('Player 1')
        player.set_hand([Card('Hearts', '10'), Card('Spades', '10')])  # Pair
        self.assertTrue(player.has_pair())

    def test_take_action(self):
        player = Player('Test Player')
        player.set_hand([Card('Hearts', 'A'), Card('Diamonds', 'K')])  # Set a valid hand
        action, _ = player.take_action(50, 100)  # Take action with a min_bet of 50 and pot_size of 100
        self.assertIn(action.name, [action.name for action in Action])  # Compare action names


class TestGetActionFromInput(unittest.TestCase):
    def test_get_action_from_input(self):
        game_state, optimal_action, explanation = get_action_from_input('Player 1', '5', '6', True, 'Small Blind', 50)
        self.assertIn(optimal_action.name, [action.name for action in Action])
if __name__ == '__main__':
    unittest.main(exit=False)
