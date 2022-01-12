'''
## Tic-Tac-Toe
* The board of the Tic-Tac-Toe is implemented using dictionary in python.
* Key values are given from 1-9 in the dictionary representing 1(top-left) to 9(bottom-right), initially it's values will be empty and then after every move,
 values will be given accordingly to the player's choice.
'''
board = {
    '1':' ','2':' ','3':' ',
    '4':' ','5':' ','6':' ',
    '7':' ','8':' ','9':' '
    }

def printBoard(board):
    print(board['1'] + ' | ' + board['2'] + ' | ' + board['3'])
    print('--+---+--')
    print(board['4'] + ' | ' + board['5'] + ' | ' + board['6'])
    print('--+---+--')
    print(board['7'] + ' | ' + board['8'] + ' | ' + board['9'])

'''
Storing the keys of the board in a list for future reference.
'''
keys = [] 
for key in board:
    keys.append(key)

def playGame():
    turn = 'X'
    count = 0
    
    while True:


        printBoard(board)
        print("It's Your turn, " + turn + " move to which place?")
        pos = input()

        # Analysis:
        # Posibility of any player be it 'X' or 'O' to win. It will occur only when they have played their 3rd turn on the tic-tac-toe board atleast.
        # so based on that analysis on the 5th turn or greater there is a possibility someone won.
        # but if the board was completely filled all the 9 boxes then, It's a tie!  
       
       # Check if already filled or not?

        if board[pos] == ' ':
            board[pos] = turn
            count += 1
        else:
            print("That place is already filled.\nMove to which place?")
            continue

        if count>=5:
            if board['1'] == board['2'] == board['3'] != ' ': 
                # upper row
                printBoard(board)
                print("***************** GAME OVER!! " + turn +" WON ***********************")
                break
            elif board['4'] == board['5'] == board['6'] != ' ': 
                # middle row
                printBoard(board)
                print("***************** GAME OVER!! " + turn +" WON ***********************")
                break
            elif board['7'] == board['8'] == board['9'] != ' ': 
                # bottom low
                printBoard(board)
                print("***************** GAME OVER!! " + turn +" WON ***********************")
                break
            elif board['1'] == board['4'] == board['7'] != ' ': 
                # left column
                printBoard(board)
                print("***************** GAME OVER!! " + turn +" WON ***********************")
                break
            elif board['2'] == board['5'] == board['8'] != ' ': 
                # middle column
                printBoard(board)
                print("***************** GAME OVER!! " + turn +" WON ***********************")
                break
            elif board['3'] == board['6'] == board['9'] != ' ': 
                # right column
                printBoard(board)
                print("***************** GAME OVER!! " + turn +" WON ***********************")
                break
            elif board['1'] == board['5'] == board['9'] != ' ': 
                # diagonal 1
                printBoard(board)
                print("***************** GAME OVER!! " + turn +" WON ***********************")
                break
            elif board['7'] == board['5'] == board['3'] != ' ': 
                #diagonal 2
                printBoard(board)
                print("***************** GAME OVER!! " + turn +" WON ***********************")
                break


        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
        

        if count == 9:
            printBoard(board)
            print("**********************GAME OVER********************")
            print("******************* It's a tie!! ******************")
        
        

            print("Do you want to play again??(y/n)")
            restart = input()
            if restart == 'Y' or restart == 'y':
                for key in keys:
                    board[key] = ' '
                
                playGame()   

if __name__ == "__main__":
    playGame()
             