board = [' ', ' ', ' ',
         ' ', ' ', ' ',
         ' ', ' ', ' ']

CurrentPlayer = 'X'
game_running = True

def PrintBoard(board):
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('---------')
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('---------')
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])

def player_input(board):
    while True:
        PrintBoard(board)

        input_position = input("Choose a position (1-9): ")

        if input_position.isdigit():
            position = int(input_position) - 1

            if position >= 0 and position <= 8:

                if board[position] == ' ':
                    board[position] = CurrentPlayer
                    break 
                else:
                    print('Taken na Boss')

            else:
                print('Number 1-9 nga lang!')

        else:
            print('Number 1-9 lang pwede boss')
            

while game_running:

    player_input(board)

    
    if (board[0] == board[1] == board[2] != ' ' or
        board[3] == board[4] == board[5] != ' ' or
        board[6] == board[7] == board[8] != ' ' or
        board[0] == board[3] == board[6] != ' ' or
        board[1] == board[4] == board[7] != ' ' or
        board[2] == board[5] == board[8] != ' ' or
        board[0] == board[4] == board[8] != ' ' or
        board[2] == board[4] == board[6] != ' '):
        PrintBoard(board)
        print("The winner is", CurrentPlayer)
        game_running = False
        continue

    
    if ' ' not in board:
        PrintBoard(board)
        print("Tabla boss!")
        game_running = False
        continue

    
    if CurrentPlayer == 'X':
        CurrentPlayer = 'O'
    else:
        CurrentPlayer = 'X'
