"""
    Répondez à la question suivante en une seule commande.
    Combien y a-t-il de nombres pairs dans l’intervalle [2, 10000] inclus ?
"""


if __name__ == "__main__":
    nombre_pairs = len(list(range(2, 10_000+1, 2)))
    print("nombre_pairs =", nombre_pairs)
