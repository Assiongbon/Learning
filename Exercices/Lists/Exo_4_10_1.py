"""
4.10.1 Jours de la semaine
    Constituez une liste semaine contenant les 7 jours de la semaine.
    1. À partir de cette liste, comment récupérez-vous seulement les 5 premiers jours de la semaine d’une part, et ceux du
    week-end d’autre part ? Utilisez pour cela l’indiçage.
    2. Cherchez un autre moyen pour arriver au même résultat (en utilisant un autre indiçage).
    3. Trouvez deux manières pour accéder au dernier jour de la semaine.
    4. Inversez les jours de la semaine en une commande.
"""



if __name__ == "__main__":
    week = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]
    # 1.
    working_days = week[0:5]
    print("working_days =", working_days)
    week_end = week[5:7]
    print("week_end =", week_end)
    # 2.
    working_days = week[-7:-2]
    print("working_days =", working_days)
    week_end = week[-2:-1] + [ week[-1] ]
    print("week_end =", week_end)
    # 3. 
    ##### 1ere maniere
    end_day = week[-1]
    print("end_day =", end_day)
    ##### 2eme maniere
    end_day = week[6]
    print("end_day =", end_day)
    # 4.
    week.reverse()
    print("reverse week =", week)
