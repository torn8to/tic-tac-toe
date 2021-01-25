import cv2 as cv
import numpy as np
import PIL as pil

class TicTacToeBoard:
    def __init__(self,againstComputer:bool):
        self.count = 1
        self.board = np.zeros((3,3), np.uint8)
        self.player1marker = 1
        self.player2marker = 2
        self.against_computer:bool = againstComputer
        self.player_is_first:bool = True

    def resetBoard(self):
        self.board = np.zeros((3,3), np.uint8)


    '''
    checks either player conforms to a win condition
    '''
    '''
    Methods for enabling and disabling playing against an AI  opponent
    implemented for futur reference
    '''
    def enable_ai(self):
        self.againstComputer = True;


    def disable_ai(self):
        self.against_computer = False;
    '''
    checks and returns whisch player marker has achieved a win condition
    '''


    def check_for_win(self):
        for x in self.board:
            if x == [1,1,1]:
                return self.player1marker
        for i in range(0,3):
            if self.board[1][i] == 1 and  self.board[2][i] == 1 and  self.board[3][i] == 1:
                return self.player1marker
        if self.board[2][2] == 1 and ((self.board[1][1] == 1 and self.board[3][3] == 1)or(self.board[1][3] == 1 and self.board[3][1] ==1)):
            return self.player1Marker
        for x in self.board:
            if x == [2,2,2]:
                return self.player2marker
        for i in range(0,3):
            if self.board[1][i] == 1 and  self.board[2][i] == 1 and  self.board[3][i] == 1:
                return self.player2marker
        if self.board[2][2] == 2 and ((self.board[1][1] == 2 and self.board[3][3] == 2)or(self.board[1][3] == 2 and self.board[3][1] ==2)):
            return self.player2Marker
        return 3

    '''
    returns true if there is a winner
    '''
    def is_winner(self):
        check = check_for_win()
        return check == self.player1Marker and check == self.player2marker

    '''
    returns true or flase on whether or no the placement entered has already been filled
    '''

    def coordinate_overlap(self, coordinateX, coordinateY):
        comp = self.board[coordinateY][coordinateX]
        return comp == self.player1marker or comp == self.player2marker



    def playerPlays(self, isplayer1:bool,coordinateX, coordinateY):

        if isplayer1:
            playerMarker = self.player1marker
        else:
            playerMarker = self.player2marker

        self.board[coordinateY][coordinateX] = playerMarker


    def printBoard(self):
        print(self.board)


    def play_through_text_input(self):
        IsPlaying = True
        isPlayer1 = True
        count == 0
        while IsPlaying:
            s = ''
            if isPlayer1:
                s = 'player 1'
            else:
                s = 'player 2'

            print(self.board)
            print("coordinates are 0,0 (top left) and coordinates are 2,2 bottom right")
            x = int(input(s+ 'enter your x coordinate'))
            y = int(input(s+ 'enter your y coordinate'))

            if x >2 and y > 2 or self.coordinate_overlap(x,y):
                input_is_valid = False
                while not input_is_valid:
                    print("please enterin a valid input 0-2 and in non filled coordinates")
                    x = int(input(s+ 'enter your x coordinate'))
                    y = int(input(s+ 'enter your y coordinate'))
                    input_is_valid = x >2 and y > 2 or self.coordinate_overlap(x,y)

            self.playerPlays(isPlayer1,x,y)
            count = count+1;

            if self.check_for_win() == 1 or self.check_for_win() == 2:
                print("player "+ self.check_for_win()+ "wins")
                IsPlaying = False
            elif count == 8:
                print("the game was a draw would you like to play again")


            if not isPlaying:
                i = str(input("would you like to play again Y/N"))
                if i == "Y"or i == "y":
                    self.resetBoard()
                    isPlaying = True


'''
end of TicTacToeBoard class
'''





'''
global variables
'''
tic_tac_toe_board = TicTacToeBoard(False) # ai starts off as disabled
running = True;
bar_color = (168,14,12) # bgr values for the tic tac toe board
'''variables for drawing tic tac _toe board'''
top_pad = 80
left_pad = 80
bar_length = 330
bar_width = 15
tic_tac_dimension = int((bar_length - bar_width*2)/3)
x_img = np.array(cv.imread('./Assets/X.png'))
o_img = np.array(cv.imread('./Assets/O.png'))
img = np.full((512,512,3),255,np.uint8)
'''
a function for interpereting the mouse inpyuts to get the right locations
'''

def interact(event,x,y,flags,param):
    '''variables for figuring out which location the box is interacting   '''
    xx,yy = -1,-1
    in_region = False
    #if event == cv.EVENT_LBUTTONDOWN:
    if True:
        for i in range(1,4):
            if left_pad + (i-1)*tic_tac_dimension +bar_width*(i-1) < x and x <= left_pad + (i* tic_tac_dimension)+ bar_width* (i-1):
                xx = i
            if left_pad + (i-1)*tic_tac_dimension +bar_width*(i-1) < y and y <= left_pad + (i* tic_tac_dimension)+ bar_width* (i-1):
                yy = i
    print(str(in_region) + ":("+str(xx)+","+str(yy)+")")




'''
End of interact function
'''

'''
this function ismeant to switch the value of a boolean so that it is usable
'''
def switch(*args):
    running = not running

'''
function that enables the gui to reset the board
'''
def reset_the_board(*args):
    tic_tac_toe_board.resetBoard()
    print("the succ")

def

if __name__ == '__main__':
    '''start and end coordinates for the left vertical bar'''
    left_vert_init_x = int(left_pad+tic_tac_dimension)
    left_vert_init_y = int(top_pad)
    left_vert_final_x =int(left_pad + tic_tac_dimension + 15)
    left_vert_final_y =int(top_pad + bar_length)
    '''start and end coordinates for the right vertical bar'''
    right_vert_init_x = int(left_pad+2*tic_tac_dimension+bar_width)
    right_vert_init_y = int(top_pad)
    right_vert_final_x =int( left_pad+2*tic_tac_dimension+2*bar_width)
    right_vert_final_y = int(top_pad + bar_length)
    '''start and end coordinates for the top horizontal bar'''
    top_hor_init_x  = int(left_pad)
    top_hor_init_y = int(top_pad+tic_tac_dimension)
    top_hor_final_x = int(left_pad+bar_length)
    top_hor_final_y = int(top_pad+tic_tac_dimension+bar_width)
    '''start and endcoordinates for the bottom horizontal bar'''
    bottom_hor_init_x = int(left_pad)
    bottom_hor_init_y = int(top_pad + 2*tic_tac_dimension+bar_width)
    bottom_hor_final_x =int( left_pad+bar_length)
    bottom_hor_final_y = int( top_pad+2*tic_tac_dimension+2*bar_width)

    ''' creating the display image array'''



    cv.namedWindow('image')
    cv.createButton("Exit Game", switch,'image',cv.QT_PUSH_BUTTON,1) # when this button is hit it breaks the for loop
    cv.createButton("Reset Board",reset_the_board,'image',cv.QT_PUSH_BUTTON,0) # resets the board
    cv.setMouseCallback('image', interact)

    '''drawing the bars of the the tic-tac-toe gameBoard'''
    # drawing the left vertical bar
    cv.rectangle(img,(left_vert_init_x,left_vert_init_y),(left_vert_final_x,left_vert_final_y),bar_color,-1)
    # drawing the right vertical bar
    cv.rectangle(img,(right_vert_init_x,right_vert_init_y),(right_vert_final_x,right_vert_final_y), bar_color, -1)
    # drawing the top horizontal bar
    cv.rectangle(img,(top_hor_init_x,top_hor_init_y),(top_hor_final_x,top_hor_final_y), bar_color, -1)
    # drawing the bottom horizontal bar
    cv.rectangle(img,(bottom_hor_init_x,bottom_hor_init_y),(bottom_hor_final_x,bottom_hor_final_y),bar_color, -1)

    

    while running:
        cv.imshow('image',img)
        k = cv.waitKey(20) & 0xFF
        if k == 27:
            break

    cv.destroyAllWindows()
