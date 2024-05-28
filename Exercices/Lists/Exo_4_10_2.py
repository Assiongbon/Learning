"""
    Créez 4 listes hiver, printemps, ete et automne contenant les mois correspondants à ces saisons. Créez ensuite une
    liste saisons contenant les listes hiver, printemps, ete et automne. Prévoyez ce que renvoient les instructions suivantes,
    puis vérifiez-le dans l’interpréteur :
    1. saisons[2]
    2. saisons[1][0]
    3. saisons[1:2]
    4. saisons[:][1]. Comment expliquez-vous ce dernier résultat ?
"""


if __name__ == "__main__":
    hiver = ["Janvier", "Fevrier", "Mars"]
    printemps = ["Avril", "Mai", "Juin"]
    ete = ["Juillet", "Aout", "Septembre"]
    automne = ["Octobre", "Novembre", "Decembre"]
    saisons = [hiver, printemps, ete, automne]
    # 1. saisons[2]
    print("saisons[2] =", saisons[2])
    # 2. saisons[1][0]
    print("saisons[1][0] =", saisons[1][0])
    # 3. saisons[1:2]
    print("saisons[1:2] =", saisons[1:2])
    # 4. saisons[:][1]
    print("saisons[:][1] =", saisons[:][1])

