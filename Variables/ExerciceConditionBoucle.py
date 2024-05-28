"""
 Objectif : supprimer tous les multiples de 2
"""


liste = [1, 2, 10, 45, 18, 15, 32, 14, 13, 10]


if __name__ == "__main__":
    print("BEGIN ExerciceConditionBoucle.py")

    # 0. Creer une nouvelle liste
    liste_resultat = []
    # 1. Parcourir la liste
    for i in liste:
    # 2. Verifier si l'element courant est multiple de 2
        if (i % 2) == 0: # le reste de la division entière est égal 0
            pass
        else:
            liste_resultat.append(i)
    # 3. Supprimer l'element si c'est un multiple
    liste = liste_resultat
    print(liste)

    print("END ExerciceConditionBoucle.py")

