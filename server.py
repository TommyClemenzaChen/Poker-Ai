from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
from poker import PokerGame, Player

app = Flask(__name__)
CORS(app)  # Enable CORS
game_state = {}

@app.route('/new_game', methods=['POST'])
def new_game():
    players = [Player('Player 1', 2000), Player('Player 2', 1500), Player('Player 3', 1500), 
               Player('Player 4', 1500), Player('Player 5', 1500), Player('Player 6', 1500)]
    global game_state
    game = PokerGame(players)
    game_state = game.play_game(1)  
    return make_response(jsonify(game_state), 201)  # Created

@app.route('/state', methods=['GET'])
def state():
    if game_state:
        return jsonify(game_state)
    else:
        return make_response(jsonify({"error": "Game not started"}), 404)  # Not Found

@app.route('/play_round', methods=['PUT'])
def play_round():
    global game_state
    if game_state:
        game_state = game.play_game(1)
        return make_response(jsonify(game_state), 200)  # OK
    else:
        return make_response(jsonify({"error": "Game not started"}), 404)  # Not Found

if __name__ == "__main__":
    app.run(debug=True)
