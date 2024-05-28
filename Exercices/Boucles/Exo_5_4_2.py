"""
    Constituez une liste semaine contenant les 7 jours de la semaine.
    Écrivez une série d’instructions affichant les jours de la semaine 
    (en utilisant une boucle for), ainsi qu’une autre série
    d’instructions affichant les jours du week-end (en utilisant une boucle while).
"""


if __name__ == "__main__":
    week = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]
    # Afficher les jours de la semaine en utilisant une boucle for (Lundi au Vendredi)
    print("Afficher les jours du week-end en utilisant une boucle while")
    for day in week[:5]:
        print(day)
    # Afficher les jours du week-end en utilisant une boucle while
    print("Afficher les jours du week-end en utilisant une boucle while")
    index = 5
    while index < len(week):
        print(week[index])
        index = index + 1