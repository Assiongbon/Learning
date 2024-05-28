"""
    Affichez la table de multiplication par 9 en 
    une seule commande avec les instructions range() et list().
"""


if __name__ == "__main__":
    table = list(range(0, (9*9+1), 9))
    print("table =", table)

