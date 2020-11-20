# course: Object-oriented programming, year 2, semester 1
# academic year: 2020-21
# author: B. Schoen-Phelan
# date: 13-11-2020
# purpose: Lab wk8 - Word Games

# base class
class WordGames:
    """
    Class to represent the word game's base class.
    Methods and attributes that every type of word
    game should have are defined here.
    ...
    Attributes:
    -----------
        __my_words : str
        Read from user input and identifies the word
        or sentence that a user has inputted.

    Methods:
    --------
        the_words:
            Property getter method that returns
            the value of the user inputted word
            or sentence

        word_play:
            Contains logic for playing the game.
            Child classes should override this
            method in order to implement their own
            game logic.
    """
    def __init__(self):
        """
        Constructs the necessary attributes for the
        WordGame object.

        Parameters: None.
        -----------

        Instance variables:
        -------------------
            __my_words : str
                Variable that holds the user inputted word or
                sentence. Set to enforced encapsulation via
                name mangling.
        """
        self.__my_words = input("Please enter a word or sentence: ")

    @property
    def the_words(self):
        """
        Property method to return the value of the user
        inputted word or sentence.

        Parameters: None.
        -----------

        Returns:
        ________
            __my_words : str
                The value of the word or sentence that has
                been inputted by a user.
        """
        return self.__my_words

    def word_play(self):
        """
        Plays the game. The base class version of playing
        the game simply prints the value that has been
        inputted.

        Parameters: None.
        -----------

        Returns: None.
        --------
        """
        print("User input was: "+self.the_words)

class WordDuplication(WordGames): # you implement this and provide docstrings
    """
                Plays the game. This edited version modifies the functinality by duplicating
                the words
                Parameters: None.
                -----------

                Returns: duplicate word.
                --------
                """
    def word_play(self):
        for i in range(2):
            print(self.the_words)

    

class WordScramble(WordGames): # you implement this and provide docstrings
    """
            Plays the game. This edited version modifies the functinality by scrambling
            the words
            Parameters: None.
            -----------

            Returns: Scrambelled word.
            --------
            """
    def word_play(self):
        # one solution for full sentence
        sentence = self.the_words.strip().split()
        #
        # # Get the word from the sentence
        for index, word in enumerate(sentence):
            # check the length of the word > 3
            if len(word) > 3:
                # swap the indice of 2 and last element
                temp_word = list(
                    word)  # we use a list for item assignment, but could also just use another new string variable
                if (',' in temp_word) or ('.' in temp_word):
                    temp = temp_word[1]
                    temp_word[1] = temp_word[-3]
                    temp_word[-3] = temp
                else:
                    # split the word in to a list of characters and swap
                    # this swap leaves first and last in tact
                    temp = temp_word[1]
                    temp_word[1] = temp_word[-2]
                    temp_word[-2] = temp

                # Join the characters together and form the word
                swapped_word = ''.join(temp_word)
                # replace the previous word at that position with the new swapped word
                sentence[index] = swapped_word
            else:
                # Since the length of the word < 3 don't swap the word
                sentence[index] = word

        # Join all the words with a space
        the_swap = ' '.join(sentence)
        # Print word
        print(the_swap)

class MultipleInheritance(WordDuplication,WordScramble):



# prints the docstrings info
# if this class was a python module
# print(WordGames.__doc__)

# Create an instances of the classes here:
# wg = WordGames()
# wg.word_play()
#
# test = WordScramble()
# test.word_play()
#
# dup = WordDuplication()
# dup.word_play()

mul = MultipleInheritance()
mul.word_play()
