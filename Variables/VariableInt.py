"""
    %  ==> reste de la division entiere
    /  ==> operateur division avec virgule
    // ==> operateur division entiere

    and   : et
    or    : ou
    not   : l'inverse
    
    3 =  11
    2 =  10

    == : egal
    != : different
    >
    <
    >=
    <=

"""

nombre = 5

#nombre = nombre + 4  # nombre += 4
nombre += 4

print(nombre)

if __name__ == "__main__":
    print("BEGIN")
    print(type(nombre))
    puissance_3 = nombre ** 3
    reste = nombre % 3
    quotient = nombre // 3
    print(puissance_3, "reste =",reste, "quotient =", quotient)

    if True and True:
        print("Les deux conditions sont vraies")

    nombre = 10
    comparaison = (nombre != 11) or True
    print("comparaison =", comparaison)
    if nombre != 10:
        print("Oui,", nombre, "est different de 10")
    
    if nombre is 11:
        print("nombre is 10")
    else:
        print("nombre is not 10")
    nombre = None
    if nombre is None:
        print("oui")


