# TicTacToeGame

```python
def fancyAlert(arg):
    for x in range(n):
        print()
```

# Top-Down Design of Tic-Tac-Toe Game

# Things to note:
# - The program will include all or almost all the functions
#   that are in this Top-Down Design, though a number of them
#   are not finished 

#   Feature of Top-Down Design:

# - Each function includes a description
# - input/output behavior is fully specified
# - The program runs
# - If a function is not completed, this is clearly indicated
#   with something like "STUBB!!"

# ALSO!, my game will have a class called GameRecord that will interact
# automatically with the program of the game to record player stats while
# the game is running.


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
from graphics import * # will be used in full program
#--------------------------------------------------------------------------#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# 
#--------------------------------------------------------------------------#
                 # Description: CLASS GameRecord. #
                 #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

class GameRecord:

    def __init__(self, games, player, wins, losses):
        self.games = games
        self.games = 1
        self.player = player
        self.wins = wins
        self.losses = losses

    def getGames(self):
        return self.games

    def getPlayers(self):
        return self.player

    def getWins(self):
        return self.wins

    def getLosses(self):
        return self.losses

    def __str__(self):
        Req = " The information requested is for " + self.player
        Req = Req + ", current winning streak is "
        Req = Req + self.getWins()
        Req = Req + ", with a total of " + self.games
        Req = Req + " games. \nPlayer has loss a total of "
        Req = Req + self.losses
        

        return Req
    
#--------------------------------------------------------------------------#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#--------------------------------------------------------------------------#
                # Description: Prints introduction.#
                #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

def printIntro(argument):
    for i in range(n):
        
        # n = range value
        # argument = welcoming message
# The name of this function will most likely be changed in the future.
# This function will be used to introduce the game to the user when the
# program is run, in a way that it will seem like the game is loading;
# hence the use of a for loop.

#--------------------------------------------------------------------------#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#--------------------------------------------------------------------------#
                 # Description: Draws arguments.#
                 #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

def draw(argument):

    argument.draw(window)
    
# This function is defined to draw arguments in a neat way.
# Description: This function will be useful to make the program look
# more organized whenever the function is called.
# Input: an argument (object)
# Output: Object will be drawn on the window screen

#--------------------------------------------------------------------------#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#--------------------------------------------------------------------------#
                 # Description: Removes arguments.#
                 #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

def undraw(argument):
    argument.undraw()
    
# Much like the previous function, the function 'undraw' is defined to
# remove arguments in a neat way.
# Description: This function will be useful to make the program look
# more organized whenever the function is called.
# Input: an argument (object)
# Output: Object will be removed from the window screen

#--------------------------------------------------------------------------#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# 
#--------------------------------------------------------------------------#
                 # Description: PlayerX Entities. #
                 #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

# STUBB!(fcn not finished)
def playerX():
    exampleText = Text.... Player has chosen X
    get.mouseClicks

# Input = This will be defined if user clicks on X
# Output = Window will draw exampleText 
# Description: This function will be useful to inform user of his choice.
# After playerX is defined, program will undraw text and change the text
# value into "Player X turn" so that it can further be used throughout the
# game when player X has to make a move.

# Final Input: [ playerX Clicks ] - when prompted to play
# Final Output: Object will be removed after action is taken.
# Function will include, but is not limited to: For or while loops if
#necessary, and if statements when required.

#--------------------------------------------------------------------------#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# 
#--------------------------------------------------------------------------#
                 # Description: PlayerO Entities. #
                 #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
                 
# STUBB!(fcn not finished)
def playerO():
    exampleText = Text.... Player has chosen O
    get.mouseClicks
    
# much like function above... 
# Input = This will be defined if user clicks on O
# Output = Window will draw exampleText 
# Description: This function will be useful to inform user of his choice.
# After playerX is defined, program will undraw text and change the text
# value into "Player O turn" so that it can further be used throughout the
# game when player O has to make a move.

# Final Input: [ playerO Click ] - when prompted to play
# Final Output: Object will be removed after action is taken.
# Function will include, but is not limited to: For or while loops if
#necessary, and if statements when required.

#--------------------------------------------------------------------------#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# 
#--------------------------------------------------------------------------#
                 # Description: Looping Function. #
                 #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

# STUBB! (Not finished)
def Loop(n):
# This function might be used for spaces as it might be used for something
# else!!
    for x in range(n):
        print()
# Function's purpose has not been defined yet. 
        
#--------------------------------------------------------------------------#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# 
#--------------------------------------------------------------------------#
                 #    Description: WrongClicks.   #
                 #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

# STUBB! (Not finished)
def WrongClick():
    # ....
    # Input: Erroneous click
    # Outputs:
    #       - prompt user to try again message
    #       - allow user as many tries as he pleases until the right move
    #         has been made.
    
#--------------------------------------------------------------------------#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# 
#--------------------------------------------------------------------------#
                 #      Description: ErrorMsg.    #
                 #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
                 
def ErrorMsg(argument):
    # ....
    # Input: N amount of erroneous clicks greater than 10
# This function will acknowledge the fact that a player has attempted to
# play on the wrong spot more than 10 times despite the fact of being kindly
# prompted to make a proper choice.

#--------------------------------------------------------------------------#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# 
#--------------------------------------------------------------------------#
                 #   Description: Game Results.   #
                 #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
                 
# STUBB! (Not finished)
def printResults(winPlayerX, winPlayerO):
# This function will print the winner of the game on the graph window.
# Winning row (horizontal, vertical or diagonal) will be marked with a RED line
# The option to play again, reset game, choose X or O again, or even
# play another player or computer will be given to the user.


#--------------------------------------------------------------------------#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# 
#--------------------------------------------------------------------------#
                 #   Description: Game Results.   #
                 #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
                 
def main():
    printIntro()
    draw(argument)
    undraw(argument)
    playerX()
    playerO()
    Loop(N)
    ErrorMsg(argument)
    printResults(winPlayerX, winPlayerO)
main()
# This function is basically every function of the game.
# The game can be played calling main()
# After main has finalized and the results are given... The game will
# prompt the user about playing again, if he so wishes to play again,
# the function will give the user the option to play the computer (in which
# he is then asked for the difficulty of the computer or simply vs a player.

    
