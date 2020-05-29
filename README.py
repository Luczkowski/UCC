# UCC

import json

class Dictionary:

    def __init__(self, words=None):
        #self.words_dictionary = {}
        self.open_dictionary_file()
        if words:
            self.words_dictionary = words

    def add_word(self, orginal_word, translated_word):
        #self.open_dictionary_file()
        if orginal_word in self.words_dictionary:
            print (f"Słowo '{orginal_word}' znajduje się w słowniku")
            ans = input("Czy chcesz je zaktualizować?")
            if ans.lower()[0] != "t" or ans.lower()[0] == "y":
                return "Kończymy więc"
        self.words_dictionary[orginal_word] = translated_word
        self.update_dictionary_file()
        #return self.words_dictionary

    def get_word(self, orginal_word):
        #self.open_dictionary_file()
        if orginal_word not in self.words_dictionary:
            print(f"Słowo '{orginal_word}' nie znajduje się w słowniku")
            ans = input("Czy chcesz je dodać do słownika?")
            if ans.lower()[0] == "t" or ans.lower()[0] == "y":
                word = input("Podaj tłumaczenie:")
                self.add_word(orginal_word, word)
        else:
            return self.words_dictionary[orginal_word]

    def delete_word(self, orginal_word):
        #self.open_dictionary_file()
        if orginal_word not in self.words_dictionary:
            return f"Słowo '{orginal_word}' nie znajduje się w słowniku"
        else:
            del self.words_dictionary[orginal_word]
        self.update_dictionary_file()
        #return self.words_dictionary

    def translate(self, sentence):
        new_words = []
        for i in sentence.split(" "):
            if i in self.words_dictionary:
                new_words.append(self.words_dictionary[i])
            else:
                new_words.append(len(i) * "X")
        return " ".join(new_words)

    def open_dictionary_file(self):
        try:
            file = open("dictionary.json", encoding="utf-8")
        except FileNotFoundError:
            file = open("dictionary.json", "w", encoding="utf-8")
            content = "{}"
            file.write(content)
        else:
            content = file.read()
        finally:
            file.close()
        self.words_dictionary = json.loads(content)

    def update_dictionary_file(self):
        dictionary_json = json.dumps(self.words_dictionary)
        file = open("dictionary.json", mode="w", encoding="utf-8")
        file.write(dictionary_json)
        file.close()

d1 = Dictionary()
d2 = Dictionary()
