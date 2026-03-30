from flask import Flask, render_template, request, redirect, url_for, session
import os
from dotenv import load_dotenv
from .game_handler import init_game, get_playerName, get_word, get_random_player

load_dotenv()

app = Flask(__name__)
secret_key = os.getenv("SECRET_KEY")
app.secret_key = secret_key

@app.route("/", methods=["GET", "POST"])
def home():
    session.pop("player_index", None)
    if request.method == "POST":
        players = request.form.getlist("players[]")
        player_count = len(players)
        category = request.form.get("category")
        imposter_count = int(request.form.get("impostor_count"))

        init_game(player_count, players, category, imposter_count)

        session["player_index"] = 0
        return redirect(url_for("game"))

    return render_template(
        "setup_index_mobile.html"
    )

@app.route("/game", methods=["GET", "POST"])
def game():
    player_index = session.get("player_index", 0)

    if request.method == "POST":
        session["player_index"] = session.get("player_index", 0) + 1
        return redirect(url_for("game"))

    try:
        next_player_name = get_playerName(player_index)
        next_word = get_word(player_index)
    except IndexError:
        return redirect(url_for("start"))

    return render_template(
        "game_index_mobile.html",
        player_name= next_player_name,
        word= next_word
    )


@app.route("/start", methods=["GET", "POST"])
def start():
    if request.method == "POST":
        return redirect(url_for("home"))

    return render_template(
        "start_index_mobile.html",
        first_player= get_random_player().name
    )

if __name__ == "__main__":
    app.run(debug=True, port=6060)