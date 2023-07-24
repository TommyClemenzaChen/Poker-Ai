# File: unit_tests.py

import unittest
from poker import Player, Card, get_action_from_input

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
        player.set_position('Early')
        self.assertEqual(player.position, 'Early')

    def test_invalid_position(self):
        player = Player('Player 1')
        with self.assertRaises(AssertionError):
            player.set_position('InvalidPosition')  # Invalid position

    def test_has_high_card(self):
        player = Player('Player 1')
        player.set_hand([Card('Hearts', '10'), Card('Spades', 'A')])  # High card
        self.assertTrue(player.has_high_card())

    def test_has_pair(self):
        player = Player('Player 1')
        player.set_hand([Card('Hearts', '10'), Card('Spades', '10')])  # Pair
        self.assertTrue(player.has_pair())

    def test_take_action(self):
        player = Player('Player 1')
        player.set_hand([Card('Hearts', '10'), Card('Spades', 'A')])  # High card
        player.set_position('Early')
        action, explanation = player.take_action(10, 100)  # min_bet = 10, pot_size = 100
        self.assertIn(action, ['FOLD', 'CALL', 'RAISE'])
        self.assertIsInstance(explanation, str)

class TestGetActionFromInput(unittest.TestCase):
    def test_get_action_from_input(self):
        player_name = 'Player 1'
        card1_value = '10'
        card2_value = 'A'
        are_suited = False
        position = 'Early'
        min_bet = 10
        game_state, optimal_action, explanation = get_action_from_input(
            player_name, card1_value, card2_value, are_suited, position, min_bet)
        self.assertIn('current_player', game_state)
        self.assertEqual(game_state['current_player'], player_name)
        self.assertIn('player_states', game_state)
        self.assertIn(player_name, game_state['player_states'])
        self.assertIn(optimal_action, ['FOLD', 'CALL', 'RAISE'])

if __name__ == '__main__':
    unittest.main(exit=False)
