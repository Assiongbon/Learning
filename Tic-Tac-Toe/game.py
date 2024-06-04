import os

# @PLAYER
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
    COORDINATE_A2 : (0, 1),
    COORDINATE_A3 : (0, 2),
    COORDINATE_B1 : (1, 0),
    COORDINATE_B2 : (1, 1),
    COORDINATE_B3 : (1, 2),
    COORDINATE_C1 : (2, 0),
    COORDINATE_C2 : (2, 1),
    COORDINATE_C3 : (2, 2),
}

game_data = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]

def display_game()->None:
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
    pass



def get_player_input(player:str)->str:
    """
        @param player : @PLAYER
        @return coordinate: @COORDINATE
        TODO: 
        - Demander le joueur "player" d'entrer les coordonnées (les minuscules et majuscules sont acceptables")
        - Validater les coordonées
        - Redemander les coordonnées si elles sont incorrectes
        - Retourner les coordonnées si elles sont correctes sous le format @COORDINATE
    """
    pass


def set_player_in_game_data(game_data:list, player:str, coordinate:str)->None:
    """
        @param game_data : list of list
        @param player : @PLAYER
        @paramm coordinate: @COORDINATE
        TODO:
            - Ajouter le 'player' dans le 'game_data' aux coordonées 'coordinate' en utilisant le 
                dictionnaire TRANSLATOR
    """
    pass


def game_over(game_data:list):
    """
        @param game_data : list of list
        @return 
            - False : le jeu continue
            - None : le jeu est terminé avec match nul
            - player : le jeu est terminé avec le gagnant 'player' @PLAYER
    """
    pass


if __name__ == "__main__":
    os.system("cls")