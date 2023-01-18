def find_top_right(board):
    try:
        max_x = 0
        max_y = 0
        max_val = board[0][0]
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] > max_val:
                    max_val = board[i][j]
                    max_x = i
                    max_y = j
        print("Position de l'élément le plus en haut à droite : x =", max_x, ", y =", max_y)
    except IndexError:
        print("La forme est vide.")
    except TypeError:
        print("La forme n'est pas une liste de listes.")
    except:
        print("Une erreur inattendue s'est produite.")

board = [[0, 0, 0, 0], [1, 1, 1, 1], [2, 3, 3, 1]]
find_top_right(board)
