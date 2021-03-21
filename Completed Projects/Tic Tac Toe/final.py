import os

board = {'7': ' ' , '8': ' ' , '9': ' ' ,
         '4': ' ' , '5': ' ' , '6': ' ' ,
         '1': ' ' , '2': ' ' , '3': ' ' }

def printBoard():
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])


#TAKE USER INPUT

turn = 0

def ensureNonZero(input_number):
#     global input_number
    
    condition_met = False
    
    while condition_met == False:
        
        if len(input_number) == 0:
            input_number = input("Please input a non-zero entry: ")

        else:
            condition_met = True
            
    return input_number
            
#UPDATE DICTIONARY
def updateBoard():
    global turn, input_number, letter
    repeat = True
    
#     if turn%2 == 0:
#         letter = 'X'
#     else:
#         letter = 'O'
    #Ensuring that repitition of numbers is not allowed
    while repeat == True:
            if board[input_number] != ' ':
                print("'\n', Please select a square that isn't already filled")
                print("Please Input where you would want to put ", letter, " : ", '\n')
                input_number = input()
            else:
                repeat = False
                
    if turn%2 == 0:
        letter = 'X'
        board[input_number] = 'X'
        turn += 1
        
    else:
#         repeat = False
        letter = 'O'
        board[input_number] = 'O'
        turn += 1
    printBoard()

#CHECK FOR WINNER

def checkWinner():
    global letter, winner
    winner = None
        
    if (board['7'] == board['5'] == board['3'] != ' ') or (board['1'] == board['5'] == board['9'] != ' '): # diagonal
            print('\n', letter, " is the winner")
            print("****************************GAME OVER*******************************")
            winner = True
            os.system("pause")
#             print("Condition 1")

    if (board['1'] == board['2'] == board['3'] != ' ') or (board['4'] == board['5'] == board['6'] != ' ') or (board['7'] == board['8'] == board['9'] != ' '): #rows
            print('\n', letter, " is the winner")
            print("****************************GAME OVER*******************************")
            winner = True
            os.system("pause")
#             print("Condition 2")

    if (board['3'] == board['4'] == board['5'] != ' ') or (board['1'] == board['5'] == board['9'] != ' '): # diagonal
            print('\n', letter, " is the winner")
            print("****************************GAME OVER*******************************")
            winner = True
            os.system("pause")
#             print("Condition 3")

    if (board['1'] == board['4'] == board['7'] != ' ') or (board['2'] == board['5'] == board['8'] != ' ') or (board['3'] == board['6'] == board['9'] != ' '): # diagonal
            print('\n', letter, " is the winner")
            print("****************************GAME OVER*******************************")
            winner = True
            os.system("pause")
            
    
#             print("Condition 4")
            
#         for n in range(1,10, 3):

#             if (board[str(n)] and board[str(n+1)] and board[str(n+2)]) == letter:
#                 print(letter, " is the winner")
#                 winner = True
#                 print("Condition 2")
        
#         for n in range(1,4):
#             if (board[str(n)] and board[str(n+3)] and board[str(n+6)]) == letter:
#                 print(letter, " is the winner")
#                 winner = True
#                 print("Condition 3")


board = {'7': ' ' , '8': ' ' , '9': ' ' ,
     '4': ' ' , '5': ' ' , '6': ' ' ,
     '1': ' ' , '2': ' ' , '3': ' ' }

printBoard()
print("The above is the empty playing board. To place your mark, enter a number in the range of 1-9. The mark (X/O) will be placed in accordance to its position in the number pad\n")

turn = 0
winner = False

for i in range(1,10):
    if winner == True:
        break

    if turn%2 == 0:
        letter = 'X'
    else:
        letter = 'O'

    string = "Please Input where you would want to put "+ letter+ " : "
    input_number= input(string)
    input_number = ensureNonZero(input_number)
    updateBoard()
    checkWinner()
