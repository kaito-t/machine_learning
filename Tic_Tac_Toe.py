#1~9の整数以外が入力された際に、入力を弾く処理を行います。

# -----Global Variables -----


#最初はboardを作ります
# Game board
board = ["-","-","-",
         "-","-","-",
         "-","-","-", ]

#ここまででは何も表示されないです。

#If game is still going
game_still_going = True

#Who won? Or tie?
winner = None

#Whos turn is it
current_player = "X"

#Display_board
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

#play a game of tic tac toe
def play_game():

    #初期の局面を表示します
    display_board()

    #while the game is still going
    while game_still_going:

        #handle a single turn of arvitary player
        handle_turn(current_player)

        #check if the game has ended
        check_if_game_over()

        #flip to the other player
        flip_player()

    #The game has ended
    if winner == "X" or winner =="0":
        print(winner + "won.")
    elif winner == None:
        print("Tie.")


#Handle a single turn of an arbitary player
def handle_turn(player):

#-------------------------------------------
print(player + "'s turn.")
    position = input("Choose a position from 1-9: ")

valid = False
while not valid:

    if position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        position = input("invalid input. Choose a position from 1-9: ")

        position = int(position) - 1

    if board[position] =="-":
        valid = True
    else:
        print("You can go there. Go again.")

#-------------------------------------------

    board[position] = player
    display_board()

def check_if_game_over():
    check_for_winner()
    check_if_tie()

def check_for_winner():

    #Set up global variables
    global winner

    #check rows
    row_winner = check_rows()
    #check columns
    column_winner = check_columns()
    #check diagnols
    diagnal_winner = check_diagnals()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = columns_winner
    elif diagnal_winner:
        winner = diagnal_winner
    else:
        winner = None
    return


def check_rows():
    #set up global variables
    global game_still_going
    #check if any of the rows have all the same value
    row_1 = board[0] == board[1] == board[2] !="-" #←-は考慮しない
    row_2 = board[3] == board[4] == board[5] !="-"
    row_3 = board[6] == board[7] == board[8] !="-"
    #If any row does have a match, flag tha there is a win
    if row_1 or row_2 or row_3:
        game_still_going = False

    #Return the winner(XorO)
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return

def check_columns():
    global game_still_going
    #check if any of the rows have all the same value
    column_1 = board[0] == board[3] == board[6] !="-" #←-は考慮しない
    column_2 = board[1] == board[4] == board[7] !="-"
    column_3 = board[2] == board[5] == board[8] !="-"
    #If any columns does have a match, flag tha there is a win
    if column_1 or column_2 or column_3:
        game_still_going = False

    #Return the winner(XorO)
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return

def check_diagnals():
    global game_still_going
    #check if any of the rows have all the same value
    diagnals_1 = board[0] == board[4] == board[8] !="-" #←-は考慮しない
    diagnals_2 = board[6] == board[4] == board[2] !="-"
    #If any columns does have a match, flag tha there is a win
    if diagnals_1 or diagnals_2:
        game_still_going = False

    #Return the winner(XorO)
    if diagnals_1:
        return board[0]
    elif diagnals_2:
        return board[6]
    return

def check_if_tie():
#-----------------------------------
    global game_still_going
    if "-" not in board:
        game_still_going = False
#-----------------------------------
    return

def flip_player():
    #global variables we need
    global current_player
    # if the current player was x, then change it to O
    if current_player == "X":
        current_player ="O":
    # if the current player was O, then change it to X
    elif current_player == "O":
        current_player = "X"
    return

play_game()
