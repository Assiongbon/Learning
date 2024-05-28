"""
    Soit la liste ["vache", "souris", "levure", "bacterie"]. 
    Affichez l’ensemble des éléments de cette liste (un élément par ligne) 
    de trois façons différentes (deux méthodes avec for et une avec while).
"""

if __name__ == "__main__":
    liste = ["vache", "souris", "levure", "bacterie"]
    # 1ere maniere: for
    print("1ere maniere: for")
    for item in liste:
        print(item)
    # 2eme maniere: for
    print("2eme maniere: for")
    for index in range(len(liste)):
        print(liste[index])
    # 3eme maniere: while
    print("3eme maniere: while")
    index = 0
    taille = len(liste)
    while index < taille:
        print(liste[index])
        index = index + 1