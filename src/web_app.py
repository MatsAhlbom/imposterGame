from flask import Flask, render_template, request, redirect, url_for, session
import os
from dotenv import load_dotenv
from .game_handler import init_game, get_playerName, get_word

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
        "setup_index.html"
    )

@app.route("/game", methods=["GET", "POST"])
def game():
    player_index = session.get("player_index", 0)

    if request.method == "POST":
        session["player_index"] = session.get("player_index", 0) + 1
        return redirect(url_for("game"))

    return render_template(
        "game_index.html",
        player_name= get_playerName(player_index),
        word= get_word(player_index)
    )

if __name__ == "__main__":
    app.run(debug=True, port=6060)