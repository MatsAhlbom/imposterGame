from .player import Player, load_words
import random

AMOUNT_OF_PLAYERS = 3
players = []
word, hint = load_words("wordList.json")

for _ in range(AMOUNT_OF_PLAYERS):
    players.append(Player(word, hint))
players[random.randint(0, AMOUNT_OF_PLAYERS-1)].impostor = True

for player in players:
    player.show()