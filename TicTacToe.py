# COMMENTS:

# OPERATION (60/80):
# - Nice operation
# - On a draw game it does not alert the user
# - Play against computer operation does not work
# - Sometimes takes a lot of clicks (say on the "X") for the program to respond
# - If I click illegally on an occupied space it does not do anything,
#   but it switches to next player turn
# - By "amount of games left" you mean number of moves left.  For illegal
#   clicks it still goes down.

# CODE (20/40)
# - You have some initial use of functions and a class is used; that's good
# - But there long sequences of conditionals that can be handled quickly
#   using functions

# ******************************


#                Tic Tac Toe


#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#


from graphics import *
from math import *
import time



def StartGame():
    # STUBB!! - not finished
    class Button:


        def __init__(self, win, name, pt1, pt2):
            self.pt1x = pt1[0]
            self.pt1y = pt1[1]
            self.pt2x = pt2[0]
            self.pt2y = pt2[1]

            self.R = Rectangle(Point(pt1[0], pt1[1]), Point(pt2[0], pt2[1]))
            self.R.setOutline('cornflowerblue')
            self.R.setFill('silver')
            self.R.draw(win)

            self.T = Text(self.R.getCenter(), name)
            self.T.draw(win)

            self.activate()
                
        def filled(self, pt):

            x = pt.getX()
            y = pt.getY()

            insideBox = self.pt1x <= x <= self.pt2x and self.pt1y <= y <= self.pt2y

            if self.activated and insideBox:
                return True

            else:
                return False

        # make this dark grey
        def activate(self):
            self.activated = True

        # make this light gray
        def deactivate(self):
            self.activated = False

        def deactivation(self):
            self.activated = False
            self.R.setWidth(1)
            self.T.setFill('Red')
            self.R.setOutline('yellow')
            self.R.setFill('green')


    def undraw(NameWhatToRemove):
        NameWhatToRemove.undraw()

    def incSize(NameToSize, Size):
        NameToSize.setSize(Size)


    Setup = GraphWin("Game Setup", 400, 400)
    Setup.setCoords(0, 0, 100, 100)
    Setup.setBackground('cornflowerblue')

    PlayerVSPlayer = Button(Setup, "Player vs Player", (10,60), (40,80))
    PlayerVSComputer = Button(Setup, "Player vs Computer", (50, 60), (80, 80))

    Choice = 0
    
    while Choice != 1:
        Choop = Setup.getMouse()
        x = Choop.getX()
        y = Choop.getY()
        pair = [(x, y)]

        if (x > 10 and x < 40) and (y > 60 and y < 80):
            Choice = 1
            PlayerVSPlayer.deactivation()

           
            win = GraphWin("Tic-Tac-Toe: Player vs Player", 700, 500)
            win.setCoords(0, 0, 100, 100)
            win.setBackground('cornflowerblue')
                


            #-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

            Top1 = Button(win, "", (20,60), (40,80))
            Top2 = Button(win, "", (40,60), (60,80))
            Top3 = Button(win, "", (60,60), (80,80))
            Mid1 = Button(win, "", (20,40), (40,60))
            Mid2 = Button(win, "", (40,40), (60,60))
            Mid3 = Button(win, "", (60,40), (80,60))
            Bot1 = Button(win, "", (20,20), (40,40))
            Bot2 = Button(win, "", (40,20), (60,40))
            Bot3 = Button(win, "", (60,20), (80,40))

            HorizontalLine1 = Oval(Point(20, 40), Point(80, 40))
            HorizontalLine2 = Oval(Point(20, 60), Point(80, 60))
            VerticalLine1 = Oval(Point(40, 80), Point(40, 20))
            VerticalLine2 = Oval(Point(60, 80), Point(60, 20))   

            GameGridLines = [HorizontalLine1, HorizontalLine2, VerticalLine1, VerticalLine2]

            [x.setOutline('White') for x in GameGridLines]
            [x.setWidth(3) for x in GameGridLines]

            #-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
                

            Click1 = Text(Point(50, 85), "Click Anywhere To Start")
            incSize(Click1, 16)
            Click1.setFill('white')

            Click2 = Text(Point(50, 85), "Click Anywhere To Start")
            incSize(Click2, 15)
            Click2.setFill('black')

            Click1.draw(win)
            Click2.draw(win)

            #Drawing All Defined Objects
            [x.draw(win) for x in GameGridLines]

            win.getMouse()

            undraw(Click1)
            undraw(Click2)

            ChoosePosition = Text(Point(20, 7), "Choose X or O: ")
            ChoosePosition.setSize(15)
            ChoosePosition.setFill('Black')
            ButtonX = Rectangle(Point(35, 5), Point(45, 10))
            ButtonO = Rectangle(Point(55, 5), Point(65, 10))
            ButtonX.setFill('grey')
            ButtonO.setFill('grey')
            # O Choice
            CircleChoice = Circle(Point(60, 7.5), 1.6)
            # X Choice
            Line1 = Line(Point(39,6), Point(41, 9))
            Line2 = Line(Point(39, 9), Point(41, 6))


            GamePositionChoices = [ButtonX, ButtonO, CircleChoice, Line1, Line2]
            [x.setWidth(3) for x in GamePositionChoices]

            GamePosition = [ChoosePosition, ButtonX, ButtonO, CircleChoice, Line1, Line2]
            [x.draw(win) for x in GamePosition]

            def XGame(x1, y1):
                t = Text(Point(x1, y1), " X ")
                incSize(t, 35)
                t.setFill('white')
                t.draw(win)

            def OGame(x2, y2):
                te = Text(Point(x2, y2), " O ")
                incSize(te, 35)
                te.setFill('white')
                te.draw(win)
               
            PlayerChooses = 0

            while PlayerChooses != 1:
                User = win.getMouse()
                x = User.getX()
                y = User.getY()
                if (x > 40 and x < 50) and (y > 5 and y < 10):
                    [undraw(ChoiceBox) for ChoiceBox in GamePosition]
                    currentPlayer = "Player X"
                    PlayerChooses = 1
                        
                if (x > 55 and x < 65) and (y > 5 and y < 10):
                    [undraw(ChoiceBox) for ChoiceBox in GamePosition]
                    currentPlayer = "Player O"
                    PlayerChooses = 1

            GamesToPlay = 9
                
            t1 = 0
            t2 = 0
            t3 = 0
            m1 = 0
            m2 = 0
            m3 = 0
            b1 = 0
            b2 = 0
            b3 = 0
                
            VictoriousX = Text(Point(30, 7), " X WINS! ")
            incSize(VictoriousX, 36)

            VictoriousO = Text(Point(30, 7), " O WINS! ")
            incSize(VictoriousO, 36)

            DrawGame = Text(Point(30, 7), " IT'S A DRAW! ")
            incSize(DrawGame, 36)


# COMMENT: Don't want to define a function in another function.

            def WinLine(name):
                for i in range(10):
                    name.setOutline('White')
                    name.setOutline('Red')
                    name.draw(win)
                    undraw(name)
                    VictoriousX.draw(win)
                    undraw(VictoriousX)

            Amt = Text(Point(70, 5), 'Amount of games left: ')
            num = Text(Point(90,5), '9')
            incSize(Amt, 15)
            incSize(num, 15)

            Amt.draw(win)
            num.draw(win)
    
            while 0 < GamesToPlay:
                time.sleep(0.2)
                Turn = Text(Point(50, 90), currentPlayer + ' Turn')
                incSize(Turn, 20)
                Turn.setFill('yellow')
                Turn.draw(win) 
                pt = win.getMouse()
                x = round(pt.getX())
                y = round(pt.getY())
                Turn.undraw()

        #       TextGamesLeft = Text(20, 10), "Games Left: ", GamesToPlay)
        ### PUT GAMES TO PLAY INSIDE GRAPH WIN
        #       Draw(TextGamesLeft)




# COMMENT: Below is a lot of repeated code.  You should use functions
# to make the code shorter and clearer.
                    
                print("Amount of games left", GamesToPlay)
                    
                if currentPlayer == "Player X" and ((20 <= x <= 80) and (20 <= y <= 80)):
                    n = eval(num.getText())
                    n = n - 1
                    num.setText(str(n))
                    
                    if Top1.filled(pt) and ((20 < x < 40) and (60 < y < 80)):
                        XGame(30,70)
                        Top1.deactivate()
                        GamesToPlay -= 1
                        t1 = 1
                            
                    if Top2.filled(pt) and ((40 < x < 60) and (60 < y < 80)):
                        XGame(50,70)
                        Top2.deactivate()
                        GamesToPlay -= 1
                        t2 = 1
                            
                    if Top3.filled(pt) and ((60 < x < 80) and (60 < y < 80)):
                        XGame(70,70)
                        Top3.deactivate()
                        GamesToPlay -= 1
                        t3 = 1
                            
                    if Mid1.filled(pt) and ((20 < x < 40) and (40 < y < 60)):
                        XGame(30,50)
                        Mid1.deactivate()
                        GamesToPlay -= 1
                        m1 = 1
                            
                    if Mid2.filled(pt) and ((40 < x < 60) and (40 < y < 60)):
                        XGame(50,50)
                        Mid2.deactivate()
                        GamesToPlay -= 1
                        m2 = 1
                            
                    if Mid3.filled(pt) and ((60 < x < 80) and (40 < y < 60)):
                        XGame(70,50)
                        Mid3.deactivate()
                        GamesToPlay -= 1
                        m3 = 1
                            
                    if Bot1.filled(pt) and ((20 < x < 40) and (20 < y < 40)):
                        XGame(30,30)
                        Bot1.deactivate()
                        GamesToPlay -= 1
                        b1 = 1
                            
                    if Bot2.filled(pt) and ((40 < x < 60) and (20 < y < 40)):
                        XGame(50,30)
                        Bot2.deactivate()
                        GamesToPlay -= 1
                        b2 = 1
                            
                    if Bot3.filled(pt) and ((60 < x < 80) and (20 < y < 40)):
                        XGame(70,30)
                        Bot3.deactivate()
                        GamesToPlay -= 1
                        b3 = 1
                        
                    currentPlayer = "Player O"
                      
                elif currentPlayer == "Player O" and ((20 <= x <= 80) and (20 <= y <= 80)):
                    n = eval(num.getText())
                    n = n - 1
                    num.setText(str(n))
                    
                    if Top1.filled(pt) and ((20 < x < 40) and (60 < y < 80)):
                        OGame(30,70)
                        Top1.deactivate()
                        GamesToPlay -= 1
                        t1 = 2

                    if Top2.filled(pt) and ((40 < x < 60) and (60 < y < 80)):
                        OGame(50,70)
                        Top2.deactivate()
                        GamesToPlay -= 1
                        t2 = 2
                            
                    if Top3.filled(pt) and ((60 < x < 80) and (60 < y < 80)):
                        OGame(70,70)
                        Top3.deactivate()
                        GamesToPlay -= 1
                        t3 = 2
                            
                    if Mid1.filled(pt) and ((20 < x < 40) and (40 < y < 60)):
                        OGame(30,50)
                        Mid1.deactivate()
                        GamesToPlay -= 1
                        m1 = 2
                            
                    if Mid2.filled(pt) and ((40 < x < 60) and (40 < y < 60)):
                        OGame(50,50)
                        Mid2.deactivate()
                        GamesToPlay -= 1
                        m2 = 2
                            
                    if Mid3.filled(pt) and ((60 < x < 80) and (40 < y < 60)):
                        OGame(70,50)
                        Mid3.deactivate()
                        GamesToPlay -= 1
                        m3 = 2
                            
                    if Bot1.filled(pt) and ((20 < x < 40) and (20 < y < 40)):
                        OGame(30,30)
                        Bot1.deactivate()
                        GamesToPlay -= 1
                        b1 = 2
                            
                    if Bot2.filled(pt) and ((40 < x < 60) and (20 < y < 40)):
                        OGame(50,30)
                        Bot2.deactivate()
                        GamesToPlay -= 1
                        b2 = 2
                            
                    if Bot3.filled(pt) and ((60 < x < 80) and (20 < y < 40)):
                        OGame(70,30)
                        Bot3.deactivate()
                        GamesToPlay -= 1
                        b3 = 2

                    currentPlayer = "Player X"

            ############ THIS IS WHERE I START CHECKING WINNING ROWS

# COMMENT: The repeated code in checking for winning condition
# can be made much shorter.  For repeated code usefunction.
                    
                if (GamesToPlay == 0 or GamesToPlay != 0):
                        
                    if t1 == 1 and t2 == 1 and t3 == 1:
                        GamesToPlay = 0
                        WinningRow = Line(Point(30, 70), Point(70, 70))
                        WinningRow.setWidth(8)

                        WinLine(WinningRow)

                    if t1 == 1 and m1 == 1 and b1 == 1:
                        GamesToPlay = 0
                        WinningRow = Line(Point(30, 70), Point(30, 30))
                        WinningRow.setWidth(8)

                        WinLine(WinningRow)

                    if t1 == 1 and m2 == 1 and b3 == 1:
                        GamesToPlay = 0
                        WinningRow = Line(Point(30, 70), Point(70, 30))
                        WinningRow.setWidth(8)

                        WinLine(WinningRow)

                    if t2 == 1 and m2 == 1 and b2 == 1:
                        GamesToPlay = 0
                        WinningRow = Line(Point(50, 70), Point(50, 30))
                        WinningRow.setWidth(8)

                        WinLine(WinningRow)
                                    
                    if t3 == 1 and m3 == 1 and b3 == 1:
                        GamesToPlay = 0
                        WinningRow = Line(Point(70, 70), Point(70, 30))
                        WinningRow.setWidth(8)

                        WinLine(WinningRow)

                    if t3 == 1 and m2 == 1 and b1 == 1:
                        GamesToPlay = 0
                        WinningRow = Line(Point(70, 70), Point(30, 30))
                        WinningRow.setWidth(8)

                        WinLine(WinningRow)

                    if m1 == 1 and m2 == 1 and m3 == 1:
                        GamesToPlay = 0
                        WinningRow = Line(Point(30, 50), Point(70, 50))
                        WinningRow.setWidth(8)

                        WinLine(WinningRow)

                    if b1 == 1 and b2 == 1 and b3 == 1:
                        GamesToPlay = 0
                        WinningRow = Line(Point(30, 30), Point(70, 30))
                        WinningRow.setWidth(8)

                        WinLine(WinningRow)
                                
            ###################        

                    if t1 == 2 and t2 == 2 and t3 == 2:
                        GamesToPlay = 0
                        WinningRow = Line(Point(30, 70), Point(70, 70))
                        WinningRow.setWidth(8)

                        WinLine(WinningRow)

                    if t1 == 2 and m1 == 2 and b1 == 2:
                        GamesToPlay = 0
                        WinningRow = Line(Point(30, 70), Point(30, 30))
                        WinningRow.setWidth(8)

                        WinLine(WinningRow)

                    if t1 == 2 and m2 == 2 and b3 == 2:
                        GamesToPlay = 0
                        WinningRow = Line(Point(30, 70), Point(70, 30))
                        WinningRow.setWidth(8)

                        WinLine(WinningRow)

                    if t2 == 2 and m2 == 2 and b2 == 2:
                        GamesToPlay = 0
                        WinningRow = Line(Point(50, 70), Point(50, 30))
                        WinningRow.setWidth(8)

                        WinLine(WinningRow)
                                    
                    if t3 == 2 and m3 == 2 and b3 == 2:
                        GamesToPlay = 0
                        WinningRow = Line(Point(70, 70), Point(70, 30))
                        WinningRow.setWidth(8)

                        WinLine(WinningRow)

                    if t3 == 2 and m2 == 2 and b1 == 2:
                        GamesToPlay = 0
                        WinningRow = Line(Point(70, 70), Point(30, 30))
                        WinningRow.setWidth(8)

                        WinLine(WinningRow)

                    if m1 == 2 and m2 == 2 and m3 == 2:
                        GamesToPlay = 0
                        WinningRow = Line(Point(30, 50), Point(70, 50))
                        WinningRow.setWidth(8)

                        WinLine(WinningRow)

                    if b1 == 2 and b2 == 2 and b3 == 2:
                        GamesToPlay = 0
                        WinningRow = Line(Point(30, 30), Point(70, 30))
                        WinningRow.setWidth(8)
                        WinLine(WinningRow)

            if GamesToPlay == 0:

                for i in range(50):
                    DrawGame.setFill('White')
                    DrawGame.setFill('Red')
                    DrawGame.draw(win)
                    undraw(DrawGame)
                        
            [undraw(x) for x in GameGridLines]
            NewScreen = Rectangle(Point(0,0), Point(100, 100))
            #NewScreen.draw(win)
            NewScreen.setFill('cornflowerblue')
            Restart = Button(win, "PLAY AGAIN", (30,7), (60,15))      

            Ss = win.getMouse()
            x1x = Ss.getX()
            y1x = Ss.getY()

            if ((30 <= x1x <= 60) and (7 <= y1x <= 15)):
                win.close()
                Setup.close()
                time.sleep(0.5)
                StartGame()

 
StartGame()
