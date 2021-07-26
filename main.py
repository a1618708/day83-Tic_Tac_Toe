import random

board = "   |   |    \n___________ \n   |   |    \n___________ \n   |   |    \n"
board_choose_position = " 1 | 2 | 3  \n___________ \n 4 | 5 | 6  \n___________ \n 7 | 8 | 9  \n"
number_to_computer=[1,2,3,4,5,6,7,8,9]
board_index_number = [0, 1, 5, 9, 27, 31, 35, 53, 57, 61]
End = False

def user_choose(mark,number_lst):
    global board
    global board_choose_position
    Complete_choose = False
    while not Complete_choose:
        number = int(input("Please choose position shows in number: "))
        if board[board_index_number[number]] != " ":
            print("The place has been taken by computer")
        else:
            s = list(board)
            s[board_index_number[number]] = mark
            board = "".join(s)
            j = list(board_choose_position)
            j[board_index_number[number]] = mark
            board_choose_position = "".join(j)
            number_lst.remove(number)
            Complete_choose = True


def computer_choose(mark, number_lst):
    global board
    global board_choose_position
    computer_number = random.choice(number_lst)
    s = list(board)
    s[board_index_number[computer_number]] = mark
    board = "".join(s)
    j = list(board_choose_position)
    j[board_index_number[computer_number]] = mark
    board_choose_position = "".join(j)
    number_lst.remove(computer_number)

def game_over(player):
    global board
    if board[board_index_number[1]] !=" " and board[board_index_number[1]]==board[board_index_number[2]]==board[board_index_number[3]]:
        return True,player==board[board_index_number[1]]
    elif board[board_index_number[4]] !=" " and board[board_index_number[4]]==board[board_index_number[5]]==board[board_index_number[6]]:
        return True,board[board_index_number[4]]
    elif board[board_index_number[7]] !=" " and board[board_index_number[7]]==board[board_index_number[8]]==board[board_index_number[9]]:
        return True,player==board[board_index_number[7]]
    elif board[board_index_number[1]] !=" " and board[board_index_number[1]]==board[board_index_number[4]]==board[board_index_number[7]]:
        return True,player==board[board_index_number[1]]
    elif board[board_index_number[2]] !=" " and board[board_index_number[2]]==board[board_index_number[5]]==board[board_index_number[8]]:
        return True,player==board[board_index_number[2]]
    elif board[board_index_number[3]] !=" " and board[board_index_number[3]]==board[board_index_number[6]]==board[board_index_number[9]]:
        return True,player==board[board_index_number[3]]
    elif board[board_index_number[1]] !=" " and board[board_index_number[1]]==board[board_index_number[5]]==board[board_index_number[9]]:
        return True,player==board[board_index_number[1]]
    elif board[board_index_number[3]] !=" " and board[board_index_number[3]]==board[board_index_number[5]]==board[board_index_number[7]]:
        return True,player==board[board_index_number[3]]
    else:
        return False, False

def win_check(over,winner):
    global End
    if over:
        print(board)
        if winner:
            print("You Win!")
        else:
            print("You Lose!")
        End = True
        return True
    elif number_to_computer == []:
        print(board)
        print("Tie!")
        End = True
        return True
    else:
        return False




player = input("Please choose one : O for player1, X for player2: ").upper()
while not End:
    if player == "O":
        print(board_choose_position)
        user_choose("O", number_to_computer)
        if win_check(game_over(player)[0], game_over(player)[1]):
            continue
        computer_choose("X", number_to_computer)
    else:
        player = "X"
        computer_choose("O", number_to_computer)
        if win_check(game_over(player)[0], game_over(player)[1]):
            continue
        print(board_choose_position)
        user_choose("X", number_to_computer)

    if win_check(game_over(player)[0], game_over(player)[1]):
        continue





