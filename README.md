# Poker-Ai
Poker
# Flask-Poker

Flask-Poker is a simple poker game simulation built with Python and Flask. It allows for the simulation of poker rounds between AI players, with the ability to view the current game state via a REST API.

This project is for development purposes and provides a simplified structure for building a poker game simulation.

## Prerequisites

Ensure you have the following installed on your local development machine:

- Python 3.x
- pip (Python package manager)

## Setup & Installation

1. Clone this repository to your local machine.

    ```
    git clone https://github.com/yourusername/flask-poker.git
    ```

2. Navigate to the project directory.

    ```
    cd flask-poker
    ```

3. Create a new Python virtual environment.

    ```
    python3 -m venv venv
    ```

4. Activate the virtual environment.

    ```
    source venv/bin/activate  # On Windows, use `.\venv\Scripts\activate`
    ```

5. Install the required Python packages.

    ```
    pip install -r requirements.txt
    ```

## Running the Server

To run the server, execute the following command in the terminal:
```
export FLASK_APP=app.py # On Windows, use set FLASK_APP=app.py
flask run
```
The server will start on http://localhost:5000. If the port is in use, you can start the server on a different port by specifying the `-p` option, like this:
```
flask run -p 5001
```

## API Endpoints

- **POST /new_game**: Starts a new game.
- **GET /state**: Returns the current game state.

## Game State

The game state is returned as a JSON object with the following structure:

```json
{
    "pot": 0,
    "rounds_played": 0,
    "current_player": null,
    "player_states": {
        "Player 1": {
            "chips": 0,
            "hand": [],
            "action": null
        },
        // ... more players
    }
}
