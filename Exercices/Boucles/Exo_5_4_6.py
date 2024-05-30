"""
    Avec les fonctions list() et range(), créez la liste entiers contenant les nombres 
    entiers pairs de 2 à 20 inclus.
    Calculez ensuite le produit des nombres consécutifs deux à deux de entiers 
    en utilisant une boucle.
"""

if __name__ == "__main__":
    # 1. Creer la liste de nobre pairs de 2 à 20 inclus
    pairs = list(range(2, 20+1, 2))
    # 2. Parcourir la liste et calculer le produit des nombres consécutifs
    ###### 1er cas: while
    print("1er cas: while")
    index = 0
    while index < len(pairs) - 1:
        produit = pairs[index] * pairs[index+1]
        print(produit)
        index = index + 1

    ###### 2eme cas: for
    print("2eme cas: for")
    for index in range(len(pairs) - 1):
        produit = pairs[index] * pairs[index+1]
        print(produit)
