import random
import json

def load_words(wordListPath):
    with open(wordListPath, "r", encoding="utf-8") as f:
        word_list = json.load(f)

    word, hint = random.choice(list(word_list.items()))

    return (word, hint)

class Player():
    def __init__(self, name, word, hint):
        self.impostor = False
        self.name = name
        self.word = word
        self.hint = hint

    def show_hint(self):
        hint = f"Impostor: {self.hint}"
        return hint

    def show_word(self):
        word = f"{self.word}"
        return word

    def show(self):
        if self.impostor:
            return self.show_hint()
        return self.show_word()