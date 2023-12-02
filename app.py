from flask import Flask, request, render_template, jsonify
from uuid import uuid4

from flask_debugtoolbar import DebugToolbarExtension

from boggle import BoggleGame

app = Flask(__name__)
app.config["SECRET_KEY"] = "this-is-secret"

# The boggle games created, keyed by game id

debug = DebugToolbarExtension(app)

debug = True



games = {}


@app.get("/")
def homepage():
    """Show board."""

    return render_template("index.html")


@app.post("/api/new-game")
def new_game():
    """Start a new game and return JSON: {game_id, board}."""

    # get a unique string id for the board we're creating
    game_id = str(uuid4())
    game = BoggleGame()
    games[game_id] = game

    return jsonify({"gameId": game_id, "board": game.board})

@app.post("/api/score-word")
def score_word():
    """Checks that the given word is playable and on the board
    Returns a json string with a result validating whether it's
    on the board"""

    print("/api/score-word", request.json)
    response = request.json
    word = response["word"]
    game_id = response["gameId"]
    game = games[game_id]

    if game.is_word_in_word_list(word):
        if game.check_word_on_board(word):
            result = "ok"
        else:
            result = "not-on-board"
    else:
        result = "not-word"

    #Get a word from JSON data
    #Get game id from JSON data
    #Take that word chec kif word is in word list with fn above
    #If it is in word_list, check if that word is on the board
    #Whatever this returns- we return as a json response


    return jsonify({"result": result})