import cv2 as cv
import numpy as np
import time

class TicTacToeBoard:
    def __init__(self,againstComputer:bool):
        self.turn_count = 1
        self.board = np.zeros((3,3), np.uint8)
        self.player1marker = 1
        self.player2marker = 2
        self.against_computer:bool = againstComputer
        self.player_is_first:bool = True
        self.isPlayer1 = True

    def resetBoard(self):
        self.board = np.zeros((3,3), np.uint8)

    def next_turn(self):
        self.isPlayer1 = not self.isPlayer1

    def get_player_1_marker(self):
        return self.player1marker

    def get_player_2_marker(self):
        return self.player2marker

    def get_board(self):
        return self.board

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



    def playerPlays(self, coordinateX, coordinateY):

        if self.isPlayer1:
            playerMarker = self.player1marker
        else:
            playerMarker = self.player2marker
        if not self.coordinate_overlap(coordinateX,coordinateY):
            self.board[coordinateY][coordinateX] = playerMarker
            self.next_turn()




    def printBoard(self):
        print(self.board)


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
a function for interpereting the mouse inputs to get the right locations
'''

def interact(event,x,y,flags,param):
    '''variables for figuring out which location the box is interacting   '''
    xx,yy = -1,-1
    in_region = False
    if event == cv.EVENT_LBUTTONDOWN:
        for i in range(1,4):
            if left_pad + (i-1)*tic_tac_dimension +bar_width*(i-1) < x and x <= left_pad + (i* tic_tac_dimension)+ bar_width* (i-1):
                xx = i-1
            if left_pad + (i-1)*tic_tac_dimension +bar_width*(i-1) < y and y <= left_pad + (i* tic_tac_dimension)+ bar_width* (i-1):
                yy = i-1
            if xx != -1 and yy != -1:
                tic_tac_toe_board.playerPlays(xx,yy)
                tic_tac_toe_board.printBoard()
                place_markers()
                break;

    print("yo")




'''
End of interact function
'''

'''
this function ismeant to switch the value of a boolean so that it is usable
'''
def switch(*args):
    cv.destroyAllWindows()

'''
function that enables the gui to reset the board
'''
def reset_the_board(*args):
    tic_tac_toe_board.resetBoard()
    reset_the_viewer()
    print("the succ")

'''
this is to reset the board to the whit background and the tic tac toe board
'''
def replace_section(primary_section,new_addition, starting_x, starting_y):
    primary_section[starting_x:starting_x+80,starting_y:starting_y+80] = new_addition
    return primary_section
'''
writes pushes all of the relevant markers to the screen
'''
def place_markers():
    board = tic_tac_toe_board.get_board()
    player1 = tic_tac_toe_board.get_player_1_marker()
    player2 = tic_tac_toe_board.get_player_2_marker()
    for i in range(0,3):
        for j in range(0,3):
            if board[i][j] == player2:
                replace_section(img,x_img,left_pad + (i*(tic_tac_dimension+bar_width)), top_pad+ j*(tic_tac_dimension+bar_width))
            if board[i][j] == player1:
                replace_section(img,o_img,left_pad + (i*(tic_tac_dimension+bar_width)), top_pad+ j*(tic_tac_dimension+bar_width))

'''
resets the viewer to the tictac toe board with a white background
'''
def reset_the_viewer():
    # resets img to an allwhite background
    img = np.full((512,512,3),255,np.uint8)
    # drawing the left vertical bar
    cv.rectangle(img,(left_vert_init_x,left_vert_init_y),(left_vert_final_x,left_vert_final_y),bar_color,-1)
    # drawing the right vertical bar
    cv.rectangle(img,(right_vert_init_x,right_vert_init_y),(right_vert_final_x,right_vert_final_y), bar_color, -1)
    # drawing the top horizontal bar
    cv.rectangle(img,(top_hor_init_x,top_hor_init_y),(top_hor_final_x,top_hor_final_y), bar_color, -1)
    # drawing the bottom horizontal bar
    cv.rectangle(img,(bottom_hor_init_x,bottom_hor_init_y),(bottom_hor_final_x,bottom_hor_final_y),bar_color, -1)



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
    cv.createButton("Exit Game", switch,'image',cv.QT_PUSH_BUTTON,1) # when this button is hit it breaks the loop
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
