



liste = [2, 3, 2, 5, 7, 11, 13, 11, 12.522, "dtdt"]
if __name__ == "__main__":
    print("BEGIN VariableLists.py")
    print(type(liste))
    print("len(liste) =", len(liste))
    print("liste =", liste)

    # Lire un element
    print("liste[0] =", liste[0])
    print("index of liste[0] =", liste.index(2))

    # Modifier un element
    liste[0] -= 1
    print("liste =", liste)

    # Inserer un element
    liste.insert(2, 33)
    print("liste =", liste)
    liste.append(55)  # inserer à la fin de la liste
    print("liste =", liste)

    # Supprimer un element
    del liste[0]
    print("liste =", liste)
    liste.remove(2)
    print("liste =", liste)
    print(liste.pop())
    print("liste =", liste)
    liste.clear() # tout supprimer
    print("liste =", liste)


    # J
    liste = [2, 3, 2, 5, 7, 11, 13, 11] + [58, 1005, 9, "hdhhdh"] + [525, 5458]
    #liste.sort(reverse=True)
    print("liste =", liste)














