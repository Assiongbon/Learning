liste = ["orange", "oran", "mango", "kiwi", "pineapple", "banana"]


if __name__ == "__main__":
    print("BEGIN ExerciceLists.py")
    taille = len(liste)
    print("len(liste) =", len(liste))

    for i in range(taille - 1):
        if len(liste[i]) > len(liste[i+1]):
            temp = liste[i]
            liste[i] = liste[i+1]
            liste[i+1] = temp

    for i in range(taille - 2):
        if len(liste[i]) > len(liste[i+1]):
            temp = liste[i]
            liste[i] = liste[i+1]
            liste[i+1] = temp
    
    for i in range(taille - 3):
        if len(liste[i]) > len(liste[i+1]):
            temp = liste[i]
            liste[i] = liste[i+1]
            liste[i+1] = temp

    for i in range(taille - 4):
        if len(liste[i]) > len(liste[i+1]):
            temp = liste[i]
            liste[i] = liste[i+1]
            liste[i+1] = temp
    print(liste)
