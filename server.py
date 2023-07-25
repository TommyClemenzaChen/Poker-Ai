from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
from poker import PokerFlop, Player, get_action_from_input

app = Flask(__name__)
CORS(app)  # Enable CORS(Cross Origin Requests)
game_state = {} # Game state as dictionary

@app.route('/get_optimal_action', methods=['POST']) # Invoked on POST request to this route
def get_optimal_action_route():
    '''
    Returns optimal action given data from frontend
    (json): A JSON representation of the Optimal action and associated explanation
    '''
    data = request.get_json() # Frontend values are encapsulated in 'data'

    try:
        player_name = data['player_name'] # Player name
        if not isinstance(player_name, str):
            raise ValueError("player_name must be a string")
        card1_value = data['card1_value'] # First Card Value
        card2_value = data['card2_value'] # Second Card Value
        are_suited = data['are_suited'] # Are the cards suited
        position = data['position'] # Position
        min_bet = data['min_bet'] # Minimum Bet

        game_state, optimal_action, explanation = get_action_from_input(player_name, card1_value, card2_value, are_suited, position, min_bet) # Retrieve optimal action, provided input
    except KeyError:
        return jsonify({'error': 'Bad Request'}), 400
    except ValueError:
        return jsonify({'error': 'Bad Request'}), 400
    except Exception as e:
        return jsonify({'error': 'Internal Server Error'}), 500
    
    return jsonify({'optimal_action': optimal_action.name, 'explanation': explanation}) # Return optimal action as JSON


if __name__ == '__main__': # Run Flask app
    app.run(debug=True)
