import math
from math import sqrt as racine_carre

PI = 3.14
[x, y, z ] = [ "Orange", "Banana", "Cherry" ]

def entree() -> float:
    local_var = 5
    print(PI)
    while True:
        # recuperer l'entrée de l'utilisateur
        """
            ceci est un commentaire
            sur plusieurs lignes
        """
        nombre = input("Entrez un nombre réel: ")
        # faire la conversion en nombre réel
        try:
            nombre = float(nombre)
            # retourner la valeur réelle
            return nombre
        except:
            print("La valeur saisie est incorrecte!")


nombre = entree()
nombrE = 0
print("La racine carrée de", nombre, "est", math.sqrt(nombre))
print(f"La racine carrée de {nombre} est {racine_carre(nombre)}")

print(PI)