from english_words import english_words_lower_alpha_set
import random

turns = 5

class WordleGame:

    def __init__(self, word_length):
        self.word_length = int(word_length)
        self.correct_letters = []
        self.incorrect_letters = []
        self.prior_guesses = []
        # display a hang man style string for entering the correct letters
        self.hang_man = ['_' for i in range(0,self.word_length)]


    def select_word(self):

        # get all words of the right length
        words = list(english_words_lower_alpha_set)
        self.eligible_words = [i for i in words if len(i) == self.word_length]

        # select random word
        rand_index = random.randrange(0,len(self.eligible_words),1)
        selected_word = self.eligible_words[rand_index]

        return selected_word

    
    def get_guess(self):

        guess = input(f'\nGuess a word that is {self.word_length} characters long: ')
        return guess.lower()


    def _is_valid_guess(self, guess):

        is_valid_guess = False

         # make sure the word is the right length and exists in the dictionary
        if len(guess) != self.word_length:
            print('Word length is invalid. Guess again...\n')
        elif guess not in self.eligible_words:
            print('Word is not in dictionary. Guess again...\n')
        else:
            is_valid_guess = True

        return is_valid_guess

      
    def _is_correct_guess(self, guess, target_word):

        is_correct_guess = False
        
        if guess == target_word:
            print(f"You win!! The correct word is {target_word}")
            self.hang_man = guess
            is_correct_guess = True
        else:
            for idx, letter in enumerate(guess):
                # if the letter is correct, save it to the correct letters list
                if letter in target_word:
                    self.correct_letters.append(letter)
                    # if the letter is in the right place, swap the _ in hang_man for the letter
                    if letter == target_word[idx]:
                        self.hang_man[idx] = letter
                else:
                    self.incorrect_letters.append(letter)

        return is_correct_guess


    def process_guess(self, guess, target_word):

        # check for a valid guess, and loop until a good one is provided
        is_valid_guess = self._is_valid_guess(guess)

        while not is_valid_guess:
            guess = self.get_guess()
            is_valid_guess = self._is_valid_guess(guess)

        # check if word matches, and get correct/incorrect letters
        is_correct_guess = self._is_correct_guess(guess, target_word)

        self.prior_guesses.append(guess)

        unique_correct = sorted(set(self.correct_letters))
        unique_incorrect = sorted(set(self.incorrect_letters))

        print(f'Correct letters: {(", ").join(unique_correct)}')
        print(f'Incorrect letters: {(", ").join(unique_incorrect)}')
        print(("").join(self.hang_man))
        for i in self.prior_guesses:
            print(i)

        return is_correct_guess


def main():
    game_length = input('Select the word length: ')

    game = WordleGame(word_length = game_length)
    target_word = game.select_word()
    is_correct_guess = False

    turn_count = 0
    while turn_count < turns and not is_correct_guess:
        guess = game.get_guess()
        is_correct_guess = game.process_guess(guess=guess, target_word=target_word)
        turn_count += 1
        print(f'\nTurns remaining: {turns - turn_count}')

    print(f'The word was: {target_word}')

if __name__ == '__main__':
    main()
