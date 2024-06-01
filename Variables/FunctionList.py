


def multiplier_par_2(liste: list)->None:
    # multiplier tous les elements par 2
    for index in range(len(liste)):
        liste[index] = liste[index] * 2

def multiplier_par_2_int(param: int)->None:
    # multiplier tous les elements par 2
    param = param * 2

def modifier_str(param: str)->None:
    # multiplier tous les elements par 2
    param = param + "_modifier"
    print("param =", param)

if __name__ == "__main__":
    ma_liste = [1, 2, 3, 4, 5]
    print("ma_liste =", ma_liste)
    multiplier_par_2(ma_liste)
    print("ma_liste =", ma_liste)

    n = 7
    print("n =", n)
    multiplier_par_2_int(n)
    print("n =", n)

    string = "string"
    print("string =", string)
    modifier_str(string)
    print("string =", string)




