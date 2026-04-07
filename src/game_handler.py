from .player import Player, load_words
import random

players = []
categoryToList = {"Personer": "wordList.json", "Brainrot": "wordList_brainrot.json", "Sport": "wordList_sport.json"}

def init_game(player_count: int, playerNames: list, category: str, imposter_count: int):
    # #remove old session
    players.clear()
    
    #load in word list
    word, hint = load_words(categoryToList[category])

    #create the playes
    for i in range(player_count):
        players.append(Player(playerNames[i], word, hint))

    #assign imposters
    chosen_imposters = random.sample(players, imposter_count)
    for player in chosen_imposters:
        player.impostor = True

def test_run():
    for player in players:
        player.show()

def get_playerName(player_index):
    return players[player_index].name

def get_word(player_index):
    return players[player_index].show()

def get_random_player():
    return random.choice(players)