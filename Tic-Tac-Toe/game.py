import os

# @PLAYER
PLAYER_NONE = " "
PLAYER_O = "O"
PLAYER_X = "X"

# @COORDINATE
COORDINATE_A1 = "A1"
COORDINATE_A2 = "A2"
COORDINATE_A3 = "A3"
COORDINATE_B1 = "B1"
COORDINATE_B2 = "B2"
COORDINATE_B3 = "B3"
COORDINATE_C1 = "C1"
COORDINATE_C2 = "C2"
COORDINATE_C3 = "C3"

# @TRANSLATOR
TRANSLATOR = {
    COORDINATE_A1 : (0, 0),
    COORDINATE_A2 : (1, 0),
    COORDINATE_A3 : (2, 0),
    COORDINATE_B1 : (0, 1),
    COORDINATE_B2 : (1, 1),
    COORDINATE_B3 : (2, 1),
    COORDINATE_C1 : (0, 2),
    COORDINATE_C2 : (1, 2),
    COORDINATE_C3 : (2, 2),
}

game_data = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]

def display_game(game_data:list)->None:
    """
                A   B   C
               _ _ _ _ _ _
            1 | X | O | X |
              |_ _|_ _|_ _|
            2 | O | X | O |
              |_ _|_ _|_ _|
            3 | O | O | X |
              |_ _|_ _|_ _|
        TODO:
            - Afficher la carte du jeu comme ci-dessus en utilisant la variable 'game_data'
    """
    print("    A   B   C")
    print("   _ _ _ _ _ _")
    index = 1
    for line in game_data:
        print(f"{index} | {line[0]} | {line[1]} | {line[2]} |")
        print("  |_ _|_ _|_ _|")
        index = index + 1



def get_player_input(game_data:list, player:str)->str:
    """
        @param game_data : @PLAYER
        @param player : @PLAYER
        @return coordinate: @COORDINATE
        TODO: 
        - Demander le joueur "player" d'entrer les coordonnées (les minuscules et majuscules sont acceptables")
        - Validater les coordonées
        - Redemander les coordonnées si elles sont incorrectes
        - Retourner les coordonnées si elles sont correctes sous le format @COORDINATE
    """
    while True:
        #  Demander le joueur "player" d'entrer les coordonnées (les minuscules et majuscules sont acceptables")
        player_input = input(f"Au tour de '{player}' de jouer: ")
        # Convertir en majuscule
        player_input = player_input.upper()
        # Validater les coordonées
        indexes = TRANSLATOR.get(player_input, None)
        if indexes != None:
            # Verifier la case dans les données du jeu
            i = indexes[0]
            j = indexes[1]
            if game_data[i][j] == PLAYER_NONE:
                break
    return player_input


def set_player_in_game_data(game_data:list, player:str, coordinate:str)->None:
    """
        @param game_data : list of list
        @param player : @PLAYER
        @paramm coordinate: @COORDINATE
        TODO:
            - Ajouter le 'player' dans le 'game_data' aux coordonées 'coordinate' en utilisant le 
                dictionnaire TRANSLATOR
    """
    indexes = TRANSLATOR.get(coordinate, None)
    i = indexes[0]
    j = indexes[1]
    game_data[i][j] = player

def game_winner(game_data:list)->str:
    """
        @param game_data : list of list
        @return 
            - None : pas de gagnant
            - player : le jeu est terminé avec le gagnant 'player' @PLAYER
    """
    # Horizontalement
    for line in range(3):
        if game_data[line][0] == game_data[line][1] and \
           game_data[line][0] == game_data[line][2] and \
           game_data[line][0] != PLAYER_NONE :
            return game_data[line][0]
    # Verticalement
    for column in range(3):
        if game_data[0][column] == game_data[1][column] and \
           game_data[0][column] == game_data[2][column] and \
           game_data[0][column] != PLAYER_NONE :
            return game_data[0][column]
    # Diagonalement
    if  game_data[0][0] == game_data[1][1] and \
        game_data[0][0] == game_data[2][2] and \
        game_data[1][1] != PLAYER_NONE :
        return game_data[1][1]
    if  game_data[0][2] == game_data[1][1] and \
        game_data[0][2] == game_data[2][0] and \
        game_data[1][1] != PLAYER_NONE :
        return game_data[1][1]
    return None

def game_over(game_data:list):
    """
        @param game_data : list of list
        @return 
            - False : le jeu continue
            - None : le jeu est terminé avec match nul
            - player : le jeu est terminé avec le gagnant 'player' @PLAYER
    """
    # Verification d'un gagnant
    winner = game_winner(game_data)
    if winner is not None:
        return winner
    
    # Verification de match nul
    match_nul = None # match nul
    for case_list in game_data:
        for case in case_list:
            if case is PLAYER_NONE:
                match_nul = False

    return match_nul

if __name__ == "__main__":
    player = PLAYER_X
    winner = None
    while True:
        os.system("cls")
        display_game(game_data)
        coordinate_player = get_player_input(game_data, player)
        set_player_in_game_data(game_data, player, coordinate_player)
        # Verification d'un gagnant
        winner = game_over(game_data)
        if winner is not False: # game over
            break
        # Changement de player
        if player == PLAYER_X:
            player = PLAYER_O
        elif player == PLAYER_O:
            player = PLAYER_X
    os.system("cls")
    display_game(game_data)
    if winner is None :
        print("Match nul")
    else:
        print(f"Le gagnant est {winner}")