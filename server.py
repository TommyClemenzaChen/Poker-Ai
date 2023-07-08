from flask import Flask, request, jsonify
from poker import PokerGame, Player

app = Flask(__name__)
game_state = {}

@app.route('/new_game', methods=['POST'])
def new_game():
    players = [Player('Player 1', 2000), Player('Player 2', 1500), Player('Player 3', 1500), Player('Player 4', 1500), Player('Player 5', 1500), Player('Player 6', 1500)]
    global game_state
    game = PokerGame(players)
    game_state = game.play_game(1)  # Assuming play_game() returns a game state now
    return 'Game started!'

@app.route('/state', methods=['GET'])
def state():
    return jsonify(game_state)

@app.route('/play_round', methods=['PUT'])
def play_round():
    global game_state
    game_state = game.play_game(1)
    return 'Round played!'

if __name__ == "__main__":
    app.run(debug=True)