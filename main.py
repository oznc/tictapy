import logger
import itertools

########
# funcs


def init():
    game_size = 2
    play_game = True
    players = [1, 2]
    while play_game:
        '''game = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]'''

        game = [[0 for _ in range(game_size)] for _ in range(game_size)]

        game_won = False
        game, _ = game_board(game, just_display=True)
        player_cycle = itertools.cycle(players)
        while not game_won:
            # current_player = player_cycle.next() #python2
            current_player = next(player_cycle)
            print("Current Player: {}".format(current_player))
            played = False

            while not played:
                column_player = int(input("Please enter column: "))
                row_player = int(input("Please enter row: "))
                game, played = game_board(
                    game, current_player, row_player, column_player)

            game_won, msg = win(game)

            if game_won:
                print(msg)
                print
                # again = str(raw_input("Game over. Wanna play again? (y/n) ")) #python2
                again = str(input("Game over. Wanna play again? (y/n) "))
                if again == "y":
                    print("Restarting")
                elif again == "n":
                    print("Bye")
                    play_game = False
                else:
                    print("Wrong input.")
                    play_game = False


def game_board(game_map, player=0, r=0, c=0, just_display=False):
    try:

        if not just_display and game_map[r][c] != 0:
            print("Other player already played that spot!")
            return game_map, False

        if not just_display:
            game_map[r][c] = player

        print
        # print(5*' ' + "a  b  c")
        # for count, row in enumerate(game_map):
        #    print(count, row)
        for row in game_map:
            print(row)
        return game_map, True

    except IndexError as e:
        print("Wrong input!")
        logger.log("\n Error: " + e.message)
        return game_map, False

    except Exception as e:
        print("Something went wrong, try again")
        logger.log("\n Exception: " + e.message)
        return game_map, False


def diag1(game_board):
    diag_arr = []
    for i in range(len(game_board)):
        diag_arr.append(game_board[i][i])
    # print(diag_arr)
    if list_elements_same(diag_arr):
        return True, "Player {} is the winner diagonally l-r".format(diag_arr[0])

    return False, ""


def diag2(game_board):
    diag_arr = []
    for i in range(len(game_board)):
        diag_arr.append(game_board[i][len(game_board)-i-1])
    # print(diag_arr)
    if list_elements_same(diag_arr):
        return True, "Player {} is the winner diagonally r-l".format(diag_arr[0])

    return False, ""


def vert(game_map):
    for col in range(len(game_map)):
        check = []
        for row in game_map:
            check.append(row[col])

        if list_elements_same(check):
            return True, "Player {} is the winner vertically".format(check[0])
        
        return False, ""


def horiz(game_map):
    for row in game_map:
        if list_elements_same(row):
            return True, "Player {} is the winner horizontally".format(row[0])

        return False, ""


def list_elements_same(L):
    if L.count(L[0]) == len(L) and L[0] != 0:
        return True
    else:
        return False


def win(game_map):
    is_won = False
    is_won, msg = vert(game_map)
    if not is_won:
        is_won, msg = horiz(game_map)
        if not is_won:
            is_won, msg = diag1(game_map)
            if not is_won:
                is_won, msg = diag2(game_map)
    return is_won, msg
########


init()
