import random
import json

def load_words(wordListPath):
    with open(wordListPath, "r") as f:
        word_list = json.load(f)

    word, hint = random.choice(list(word_list.items()))

    return (word, hint)

class Player():
    def __init__(self, word, hint):
        self.impostor = False
        self.word = word
        self.hint = hint

    def show_hint(self):
        print(self.hint)
        return

    def show_word(self):
        print(self.word)
        return

    def show(self):
        if self.impostor:
            self.show_hint()
            return
        
        self.show_word()
        return