"""
    Voici les notes d’un étudiant [14, 9, 6, 8, 12]. 
    Calculez la moyenne de ces notes. Utilisez l’écriture formatée pour
    afficher la valeur de la moyenne avec deux décimales.
"""


if __name__ == "__main__":
    notes = [14, 9, 6, 8, 12]
    # Calcul de la moyenne
    moyenne = None
    somme = 0
    ##### 1er cas : for
    for note in notes:
        somme = somme + note
    print("somme =", somme)
    moyenne = somme / len(notes)
    print("moyenne =", moyenne)
    ##### 2eme cas : sum
    somme = sum(notes)
    print("somme =", somme)
    moyenne = somme / len(notes)
    print("moyenne =", moyenne)
