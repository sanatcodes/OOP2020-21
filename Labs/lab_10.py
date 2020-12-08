
"""
Doc strings

Project Description: make a math game with an option to add more
options in the future

"""
#imports
from abc import ABC, abstractmethod



class base(ABC):

    @abstractmethod
    def __init__(self):
        print("welcome to the math game")

    @property
    @abstractmethod
    def user_input_property(self):
        pass

    @abstractmethod
    def play_game(self):
        pass

class FibonacciGame(base):

    def __init__(self):
        super().__init__()
        self.__input = 0

    @property
    def user_input_property(self):
        return self.__input

    @user_input_property.setter
    def user_input_property(self, value):
        self.__input = value

    def play_game(self):

        score = 0
        keep_playing = True

        while keep_playing:
            try:
                self.user_input_property = int(input("Enter 1 to play, Enter 2 to exit"))
                if self.user_input_property not in range(1, 3):
                    print("wrong input")
            except:
                print("Enter a whole number: Either 1 or 2")
                continue

            if self.user_input_property == 1:
                try:
                    terms = int(input("How many terms do you want: "))
                    if terms != 0:
                        fib = (self.calc_fibonacci(terms + 1))
                        print(fib[:-1])
                        right_or_wrong = int(input("What's the next number"))
                        if right_or_wrong == fib[-1]:
                            print("You got the correct answer")
                            score += 1
                        else:
                            print("Hard luck, the correct answer is: ", fib[-1])
                    else:
                        print("Nothing to play")
                except:
                    print("Terms must be a whole number")
            elif self.user_input_property == 2:
                print(f"you got {score} right this game!")
                keep_playing = False

    @staticmethod
    def calc_fibonacci(terms):
        if type(terms) is not int:
            raise TypeError("Fibonacci terms need to be greater than 0")

        fib_numbers = []
        if terms > 1:
            fib_numbers.extend([0, 1])
            before = fib_numbers[1]
            before_before = fib_numbers[0]

            for numbers in range(2, terms):
                #calculation of the numbers
                current = before + before_before
                fib_numbers.append(current)

                #setup numbers for next run
                before_before = before
                before = current

            return fib_numbers
        elif terms == 1:
            fib_numbers.append(0)
        elif terms <= 0:
            raise ValueError("cannot calculate fibonacci for 0 or below terms")



# init and playing
fib_game = FibonacciGame()
fib_game.play_game()

# try:
#     print(FibonacciGame.calc_fibonacci('fl '))
# except ValueError as ve:
#     print(ve)
# except TypeError as te:
#     print(te)
# except Exception as e:
#     print("Didn't expect this to happen", e)

