import os 
from random import choice
from time import sleep

class Hangman():
    MAX_MOVES = 6
    WORD_BANK = ("cookie", "shortcake", "cheesecake", "tiramisu",
             "donut", "cupcakes", "baklava", "cannoli", "chocotaco")

    def __init__(self):
        self.word = choice(Hangman.WORD_BANK)
        self.guessed_letters = []
        self.num_of_moves = 0
    
    def show_word(self):
        os.system("cls" if os.name == "nt" else "clear")
        board = ["_" if letter not in self.guessed_letters else letter for letter in self.word]
        for letter in board:
            print(letter, end=" ")
        print()
        print("Guessed letters : " ,end=" ")
        if self.guessed_letters:
            for letter in self.guessed_letters:
                print(letter, end=" ")
            print()
        else:
            print("You haven't guessed any letters!")
        sleep(2)
        print(f" You have {Hangman.MAX_MOVES - self.num_of_moves} moves left! Watch out...")       

    def guess_letter(self, letter):
        if len(letter) > 1:
            print("You cant do that dog, one letter at a time")
            return
        if letter in self.word:
            count = self.word.count(letter)
            print(f'you\'ve found {count} {letter}{"s" if count > 1 else ""}!')
        else:
            print(f'{letter} not in the word')
            self.num_of_moves +=1

        self.guessed_letters.append(letter)

    def check_all_letters_guessed(self):
        for letter in self.word:
            if letter not in self.guessed_letters:
                return False
        return True
    def guess_word(self, word):
        if word == self.word:
            print(f"You guessed the correct word, \"{self.word}\"!")
            return True
        else:
            print("Sorry,that's NOT the word...")
        return False
    
    def check_moves_left(self):
        if self.num_of_moves < Hangman.MAX_MOVES:
            return True
        return False
    
    def user_won(self):
        print(f"Congrats! You solved my riddle with {Hangman.MAX_MOVES - self.num_of_moves} move{'s' if self.num_of_moves > 1 else ''} left! You ROCK!")

    def user_lost(self):
        print("WOW, that hurt to watch.")

class UI():
    hangman = Hangman()

    @classmethod
    def main(cls):
        action = input("Have you played hangman before? If not or its been a while say no/n! enter to continue").upper()
        if action == "no" or action == 'n': 
            print("You got six tries bro, guess a letter if you think you know the word then hit yes when it promts you to guess the entire word!")
            sleep(7)
        else:
            pass
        while True:
            cls.hangman.show_word()
            letter = input("What letter do you want to guess? ").lower()
            cls.hangman.guess_letter(letter)
            cls.hangman.show_word()
            if cls.hangman.check_all_letters_guessed():
                cls.hangman.user_won()
                break
            action = input("Would you like to guess the whole word? yes/y or no/n ").lower()
            if action == "yes" or action == 'y':
                word = input("What is your word? ")
                if cls.hangman.guess_word(word):
                    cls.hangman.user_won()
                    break
            if not cls.hangman.check_moves_left():
                cls.hangman.user_lost()
                break

UI.main()