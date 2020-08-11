from random import random
import sys


def load_words():
    with open("./words_alpha.txt") as words:
        return words.read().split()


def good_random(min, max):
    return round(random() * (max - min)) + min


def get_input():
    guess = input("What's your guess?: ")
    if len(guess) > 0:
        guess = guess[0]
    else:
        print("Please input a letter")
        get_input()
    if guess.isalpha():
        return guess.lower()
    else:
        print("Please input a letter.")
        get_input()


class Word():
    word = list()
    to_print = list()

    def __init__(self):
        words = load_words()
        self.word = words[good_random(0, len(words) - 1)]
        for i in range(len(self.word)):
            self.to_print.append("_")

    def guess(self, hangman):
        if "".join(self.word) == "".join(self.to_print):
            print("YOU WON!")
            sys.exit()
        if hangman.i > 6:
            print("GAME OVER!")
            print("The word was {}".format(self.word))
            sys.exit()
        guess = get_input()
        if "".join(guess) not in "".join(self.word):
            hangman.next().draw()
        else:
            self.mark_answer(guess)
            hangman.draw()
        self.guess(hangman)

    def mark_answer(self, char):
        i = 0
        for character in self.word:
            if character == char:
                self.to_print[i] = char
            i += 1


class Hangman():
    def __init__(self):
        self.i = 0
        self.draw()

    def draw(self):
        print("".join(word.word))
        print("".join(word.to_print))
        with open("./{}.txt".format(self.i)) as art:
            print(art.read())

    def next(self):
        if self.i < 6:
            self.i += 1
            return self
        else:
            print("GAME OVER!")
            sys.exit()


word = Word()
hangman = Hangman()

word.guess(hangman)
