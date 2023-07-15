from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
from poker import PokerFlop, Player, get_action_from_input

app = Flask(__name__)
CORS(app)  # Enable CORS
game_state = {}

@app.route('/get_optimal_action', methods=['POST'])
def get_optimal_action_route():
    data = request.get_json()

    player_name = data['player_name']
    card1_value = data['card1_value']
    card2_value = data['card2_value']
    are_suited = data['are_suited']
    position = data['position']
    min_bet = data['min_bet']

    game_state, optimal_action = get_action_from_input(player_name, card1_value, card2_value, are_suited, position, min_bet)
    
    return jsonify({'optimal_action': optimal_action.name})

if __name__ == '__main__':
    app.run(debug=True)
