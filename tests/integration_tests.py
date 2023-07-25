# Run with: python -m unittest tests.integration_tests
# This file contains integration tests to ensure functionality of the server.
# These are integration tests, not unit tests. They are meant to test the functionality of the program as a whole,
# not individual components or the accuracy of the program.

import concurrent.futures
import requests
import time
import unittest
from flask_testing import TestCase
from flask import Flask
import json

from server import app

'''
Server integration tests to verify that the server routing works as expected
'''

class ServerTest(TestCase):
    def create_app(self):
        return app
    
    def setUp(self):
        # Code to setup before each test
        print(f'\nRunning test: {self._testMethodName}...')

    def tearDown(self):
        # Code to cleanup after each test
        print('Test complete.')
        time.sleep(0.2)

    def test_all_possible_hands(self):
        # Define the set of all possible card values
        card_values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

        # Define the set of all possible positions
        positions = ['Small Blind', 'Big Blind', 'UTG', 'Hijack', 'Cut-off', 'BTN']

        # Define the min bet
        min_bets = range(1, 6)

        # Iterate over all possible pairs of card values, both suited and unsuited
        for are_suited in [False, True]:
            for i in range(len(card_values)):
                for j in range(i + 1, len(card_values)):
                    # Iterate over all possible positions
                    for position in positions:
                        # Iterate over all possible minimum bets
                        for min_bet in min_bets:
                            # Define a test case
                            test_case = {
                                'player_name': 'Player 1',
                                'card1_value': card_values[i],
                                'card2_value': card_values[j],
                                'are_suited': are_suited,
                                'position': position,
                                'min_bet': min_bet
                            }

                            # Send a request to the server
                            response = self.client.post('/get_optimal_action', data=json.dumps(test_case), content_type='application/json')

                            # Check that the response has the correct status code
                            self.assertEqual(response.status_code, 200)

                            # Load the response data
                            data = json.loads(response.data)

                            # Check that the response data contains the expected fields
                            self.assertIn('optimal_action', data)

                            # Check that the optimal action is one of the possible actions
                            self.assertIn(data['optimal_action'], ['FOLD', 'CALL', 'RAISE'])
    
    def test_empty_request_data(self):
        response = self.client.post('/get_optimal_action', data=json.dumps({}), content_type='application/json')
        self.assertEqual(response.status_code, 400)  # Replace 400 with the expected status code

    def test_incomplete_request_data(self):
        test_case = {'player_name': 'Player 1'}  # Incomplete data
        response = self.client.post('/get_optimal_action', data=json.dumps(test_case), content_type='application/json')
        self.assertEqual(response.status_code, 400)  # Replace 400 with the expected status code

    def test_invalid_request_data(self):
        test_case = {
            'player_name': 123,  # Invalid data: player_name is not a string
            'card1_value': '5',
            'card2_value': 'J',
            'are_suited': True,
            'position': 'UTG',
            'min_bet': 1
        }
        response = self.client.post('/get_optimal_action', data=json.dumps(test_case), content_type='application/json')
        self.assertEqual(response.status_code, 400)  # Replace 400 with the expected status code
if __name__ == '__main__':
    unittest.main(exit=False)
