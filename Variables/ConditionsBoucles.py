


if __name__ == "__main__":
    print("BEGIN ConditionsBoucles.py")
    n = int(input("Entrez un nombre : "))
    if n < 0:
        n = -n
    
    collection = range(-6, n, 2)
    for element in collection:
        
        if element == 0:
            continue

        if element == 4:
            break

        print(element)
    # sortie de la boucle
    

    liste = [2, 3, 5, 7, 11, 13, 17, 2]
    print("Liste = [2, 3, 5, 7, 11, 13, 17]")
    for item in liste:
        print(item)
    
    for index in range(len(liste)):
        liste[index] = liste[index] + 1
    
    print(liste)
    
    print("END ConditionsBoucles.py")

    if True:
        pass

    print("pass")
    i = 10
    while not (i == 0):
        print("i =", i)
        i -= 1 