import random
import json

def load_words(wordListPath):
    with open(wordListPath, "r") as f:
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
        print(f"{self.name}: {self.hint}")
        return

    def show_word(self):
        print(f"{self.name}: {self.word}")
        return

    def show(self):
        if self.impostor:
            self.show_hint()
            return self.hint
        
        self.show_word()
        return self.word