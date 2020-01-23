# First milestone project


Win = False
while not Win:

    # Print out some welcome text.
    print('Welcome to Tic Tac Toe!')
    print('Each user will get a turn.')

    # Take in the player's names.
    P1 = input('What is P1\'s name? ')
    P2 = input('What is P2\'s Name? ')

    # Initialize the marker.
    turn = 'X'
    print('Great. Let\'s Play.' + P1 + ' goes first.')

    # Create a dictionary to house our values and print them on the board.
    movelist = {'1':' ', '2':' ', '3':' ', '4':' ', '5':' ', '6':' ', '7':' ', '8':' ', '9':' '}

    def p_board(movelist):
        print(movelist['1'] + '|' + movelist['2'] + '|' + movelist['3'])
        print('-----')
        print(movelist['4'] + '|' + movelist['5'] + '|' + movelist['6'])
        print('-----')
        print(movelist['7'] + '|' + movelist['8'] + '|' + movelist['9'])

    p_board(movelist)

    def win_cond(board, letter):
        return ((board['1'] == letter and board['2'] == letter and board['3'] == letter) or # first row
                (board['4'] == letter and board['5'] == letter and board['6'] == letter) or # second row
                (board['7'] == letter and board['8'] == letter and board['9'] == letter) or # third row
                (board['1'] == letter and board['4'] == letter and board['7'] == letter) or # first column
                (board['2'] == letter and board['5'] == letter and board['8'] == letter) or # second column
                (board['3'] == letter and board['6'] == letter and board['9'] == letter) or # third column
                (board['1'] == letter and board['5'] == letter and board['9'] == letter) or # first diagnonal
                (board['3'] == letter and board['5'] == letter and board['7'] == letter))   # second diagonal

    # Check for a valid move

    def check_move(board, mov):
        return board[mov] != ' '

    # X always goes first. When the player has moved,
    # flip the turn switch to the other player's symbol.
    while not win_cond(movelist, turn):
        move = input('Enter the location where you\'d like to move: ')
        if check_move(movelist, move):
            print('This spot is taken!')
        elif turn == 'X':
            movelist[move] = 'X'
            turn = 'O'
        elif turn == 'O':
            movelist[move] = 'O'
            turn = 'X'
        p_board(movelist)

    # print the board
    Win = True
