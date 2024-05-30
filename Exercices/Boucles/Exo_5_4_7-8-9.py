"""
    Créez un script qui dessine un triangle comme celui-ci :
"""

if __name__ == "__main__":
    # 1. Entrer un nombre strictement positif
    lines = int(input("Entrer un nombre strictement positif : "))
    # 2. 1er cas : for
    print("triangle normal")
    for line in range(lines):
        stars = line + 1
        # afficher les etoiles
        for star in range(stars):
            print("*", end="")
        # a la ligne suivante
        print("")

    # 2. 2eme cas
    print("triangle normal")
    for line in range(lines):
        stars = line + 1
        # afficher les etoiles
        print("*"*stars)


    # 3. 3eme cas : triangle renversé
    print("triangle renversé")
    for line in range(lines):
        stars = lines - line
        # afficher les etoiles
        print("*"*stars)


    # 3. 3eme cas : triangle à gauche
    print("triangle à gauche")
    for line in range(lines):
        stars = line + 1
        spaces = lines - stars
        # afficher les espaces
        print(" "*spaces, end="")
        # afficher les etoiles
        print("*"*stars)