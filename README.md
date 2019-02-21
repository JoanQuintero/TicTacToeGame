# TicTacToeGame #

### Top-Down Design of Tic-Tac-Toe Game

<ul>
    <li>Things to note:</li>
    <ul>
        <li>The program will include all or almost all the functions that are in this Top-Down Design, though a number of them are not finished.</li>
        <li>The module used for this Game is graphics.py,</li> 
    </ul>
</ul>

Click here --> [Graphics](http://mcsp.wartburg.edu/zelle/python/graphics.py "Get Graphics!") to get the module.

```python
from graphics import *  # Importing everything from the module graphics
``` 

### Feature of Top-Down Design:

<ul>
    <li>The program runs</li>
    <li>Each function includes a description</li>
    <li>Input/Output behavior is fully specified</li>
    <li>If a function is not completed, this is clearly indicated with the word **"STUBB!!"**</li>
    <li>Finally, the game will have a class called <em>GameRecord</em> that will interact automatically with the program of the game to record player stats while the game is running.</li>
</u>

--------------------------------------------------------------------------
--------------------------------------------------------------------------
--------------------------------------------------------------------------
--------------------------------------------------------------------------
### Overview: CLASS <em>GameRecord</em> 
>> This is just a body style of how the body of the coding will look                 
```python
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
```
--------------------------------------------------------------------------
--------------------------------------------------------------------------
--------------------------------------------------------------------------
--------------------------------------------------------------------------

### Concept: Printing introduction 

```python
def printIntro(argument):
    for i in range(n):
        
        # n = range value
        # argument = welcoming message
```

The name of this function will most likely be changed in the future.
This function will be used to introduce the game to the user when the
program is run, in a way that it will seem like the game is loading;
hence the use of a for loop.

--------------------------------------------------------------------------
--------------------------------------------------------------------------
### Concept: Drawing arguments

```python
def draw(argument):

    argument.draw(window)
```    
This function is defined to draw arguments in a neat way.
Description: This function will be useful to make the program look
more organized whenever the function is called.
Input: an argument (object)
Output: Object will be drawn on the window screen

--------------------------------------------------------------------------
--------------------------------------------------------------------------
### Concept: Removing arguments
            
```python
def undraw(argument):
    argument.undraw()
```    
Much like the previous function, the function 'undraw' is defined to
remove arguments in a neat way.
Description: This function will be useful to make the program look
more organized whenever the function is called.
Input: an argument (object)
Output: Object will be removed from the window screen

--------------------------------------------------------------------------
--------------------------------------------------------------------------
### Concept: <em>Player X</em> Entities

```python
# STUBB!(fcn not finished)
def playerX():
    exampleText = Text.... Player has chosen X
    get.mouseClicks
```
Input = This will be defined if user clicks on X
Output = Window will draw exampleText 
Description: This function will be useful to inform user of his choice.
After playerX is defined, program will undraw text and change the text
value into "Player X turn" so that it can further be used throughout the
game when player X has to make a move.

Final Input: [ playerX Clicks ] - when prompted to play
Final Output: Object will be removed after action is taken.
Function will include, but is not limited to: For or while loops if
#necessary, and if statements when required.

--------------------------------------------------------------------------
--------------------------------------------------------------------------
### Concept: <em>Player O</em> Entities 

```python                 
# STUBB!(fcn not finished)
def playerO():
    exampleText = Text.... Player has chosen O
    get.mouseClicks
```    
much like function above... 
Input = This will be defined if user clicks on O
Output = Window will draw exampleText 
Description: This function will be useful to inform user of his choice.
After playerX is defined, program will undraw text and change the text
value into "Player O turn" so that it can further be used throughout the
game when player O has to make a move.

Final Input: [ playerO Click ] - when prompted to play
Final Output: Object will be removed after action is taken.
Function will include, but is not limited to: For or while loops if
#necessary, and if statements when required.

--------------------------------------------------------------------------
--------------------------------------------------------------------------
### Concept: Looping Function

```python
# STUBB! (Not finished)
def Loop(n):
    for x in range(n):
        print()
```        
Function's purpose has not been defined yet. 
This function might be used for spaces as it might be used for something else!!
        
--------------------------------------------------------------------------
--------------------------------------------------------------------------
### Concept: WrongClicks   

```python
# STUBB! (Not finished)
def WrongClick():
``` 
Input: Erroneous click  
Outputs: prompt user to try again message allow user as many tries as he pleases until the right move has been made.
    
--------------------------------------------------------------------------
--------------------------------------------------------------------------
### Concept: Error handling    

```python                 
def ErrorMsg(argument):
    # ....
    # Input: N amount of erroneous clicks greater than 10
``` 
This function will acknowledge the fact that a player has attempted to play on the wrong spot more than 10 times despite the fact of being kindly prompted to make a proper choice.

--------------------------------------------------------------------------
--------------------------------------------------------------------------
### Concept: Game Results 

```python                 
# STUBB! (Not finished)
def printResults(winPlayerX, winPlayerO):
``` 
This function will print the winner of the game on the graph window.
Winning row (horizontal, vertical or diagonal) will be marked with a RED line
The option to play again, reset game, choose X or O again, or even play another player or computer will be given to the user.


--------------------------------------------------------------------------
--------------------------------------------------------------------------
### Concept: Main   

```python                
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
``` 
>> This function is basically every function of the game.

The game can be played calling main()
<ul>
    <li>After main has finalized and the results are given, The game will:</li>
        <ul>
            <li>Prompt the user about playing again, if he so wishes to,
the function will give the user the option to play the computer (in which
                he is then asked for the difficulty of playing vs the computer or simply vs a player.</li>
    </ul>
</ul>

    
