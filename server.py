from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
from poker import PokerFlop, Player, get_action_from_input

app = Flask(__name__)
CORS(app)  # Enable CORS(Cross Origin Requests)
game_state = {} 

@app.route('/get_optimal_action', methods=['POST']) # Invoked on POST request to this route
def get_optimal_action_route():
    '''
    Returns optimal action given data from frontend

    '''
    data = request.get_json() # Frontend values are encapsulated in 'data'

    player_name = data['player_name'] # Player name
    card1_value = data['card1_value'] # First Card Value
    card2_value = data['card2_value'] # Second card value
    are_suited = data['are_suited'] 
    position = data['position'] # Position
    min_bet = data['min_bet'] # Minimum bet(dynamic value)

    game_state, optimal_action, explanation = get_action_from_input(player_name, card1_value, card2_value, are_suited, position, min_bet) # Retrieve optimal action, provided input

    return jsonify({'optimal_action': optimal_action.name, 'explanation': explanation}) # Return optimal action as JSON


if __name__ == '__main__': # Run Flask app
    app.run(debug=True)
