"""
    Soit impairs la liste de nombres [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]. Écrivez un programme qui, à partir
    de la liste impairs, construit une liste pairs dans laquelle tous les éléments de impairs sont incrémentés de 1.
"""


if __name__ == "__main__":
    impairs = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
    pairs = []
    # Construit la liste pairs dans laquelle tous les éléments de impairs sont incrémentés de 1
    #### 1er cas: for
    for impair in impairs:
        pairs.append(impair+1)
    print("pairs =",pairs)
    pairs.clear()
    #### 2eme cas while
    index = 0
    while index < len(impairs):
        impair = impairs[index]
        pairs.append(impair+1)
        index = index + 1
    print("pairs =",pairs)
