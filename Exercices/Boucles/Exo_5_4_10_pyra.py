"""
    Créez un script qui dessine un triangle comme celui-ci :
"""

if __name__ == "__main__":
    # 1. Entrer un nombre strictement positif
    lines = int(input("Entrer un nombre strictement positif : "))
    for line in range(lines):
        stars = 2*line + 1
        spaces = lines - (line + 1)
        # afficher les espaces
        print(" "*spaces, end="")
        # afficher les etoiles
        print("*"*stars)

"""
n -> r
r = (n - 1)*2 + 1
1 -> 1
2 -> 3
3 -> 5
4 -> 7


"""