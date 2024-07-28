from flask import Flask, jsonify, request, send_from_directory, render_template
from flask_socketio import SocketIO, emit, join_room, leave_room
from loteria import generate_card, cards, check_win
import os

app = Flask(__name__, static_folder='../frontend', template_folder='../frontend')
socketio = SocketIO(app)

players = {}
games = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory(app.static_folder, path)

@app.route('/start_game', methods=['POST'])
def start_game():
    game_id = str(len(games) + 1)
    games[game_id] = {
        "players": [],
        "called_cards": []
    }
    print(f"Game started with ID: {game_id}")  # Add logging
    return jsonify({"game_id": game_id})

@app.route('/active_games', methods=['GET'])
def active_games():
    active_game_ids = list(games.keys())
    return jsonify({"active_games": active_game_ids})

@app.route('/join_game', methods=['POST'])
def join_game():
    data = request.json
    print('Received join_game request with data:', data)  # Add logging
    if 'game_id' not in data:
        print('Error: game_id not found in request data')
        return jsonify({"error": "game_id not provided"}), 400
    player_name = data['player_name']
    game_id = data['game_id']
    print(f"Received join game request from player: {player_name} for game: {game_id}")

    try:
        card = generate_card()
        print(f"Generated card for player {player_name}: {card}")

        if game_id in games and len(games[game_id]["players"]) < 10:
            player_id = str(len(players) + 1)
            players[player_id] = {
                "name": player_name,
                "game_id": game_id,
                "card": card
            }
            games[game_id]["players"].append(player_id)
            return jsonify({"player_id": player_id, "card": card})
        else:
            return jsonify({"error": "Game not found or full"}), 400
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": str(e)}), 500

@socketio.on('join')
def on_join(data):
    player_id = data['player_id']
    game_id = players[player_id]['game_id']
    join_room(game_id)
    emit('player_joined', {'player_id': player_id, 'card': players[player_id]['card']}, room=game_id)

@app.route('/call_card', methods=['POST'])
def call_card():
    data = request.json
    game_id = data.get('game_id')
    print(f"Calling card for game_id: {game_id}")  # Add logging
    if game_id and game_id in games:
        if len(cards) == 0:
            return jsonify({"error": "No more cards to call"}), 400
        card = cards.pop()
        games[game_id]["called_cards"].append(card)
        socketio.emit('card_called', {'called_card': card}, room=game_id)
        
        # Check for win conditions
        for player_id in games[game_id]['players']:
            player = players[player_id]
            print(f"Checking win for player {player['name']} with card: {player['card']} and called cards: {games[game_id]['called_cards']}")  # Add logging
            if check_win(player['card'], games[game_id]['called_cards']):
                print(f"Player {player['name']} has won the game!")  # Add logging
                socketio.emit('player_won', {'player_name': player['name'], 'player_id': player_id}, room=game_id)
                break
        
        return jsonify({"called_card": card})
    else:
        return jsonify({"error": "Game not found"}), 400

@app.route('/get_game_state', methods=['GET'])
def get_game_state():
    game_id = request.args.get('game_id')
    if game_id in games:
        return jsonify(games[game_id])
    else:
        return jsonify({"error": "Game not found"}), 400

@app.route('/static/images/cards/<filename>')
def get_card_image(filename):
    return send_from_directory(os.path.join(app.static_folder, 'images/cards'), filename)

@app.route('/static/images/boards/<filename>')
def get_board_image(filename):
    return send_from_directory(os.path.join(app.static_folder, 'images/boards'), filename)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)

