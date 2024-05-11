import math
from math import sqrt as racine_carre
def entree() -> float:
    while True:
        # recuperer l'entrée de l'utilisateur
        nombre = input("Entrez un nombre réel: ")
        # faire la conversion en nombre réel
        try:
            nombre = float(nombre)
            # retourner la valeur réelle
            return nombre
        except:
            print("La valeur saisie est incorrecte!")


nombre = entree()

print("La racine carrée de", nombre, "est", math.sqrt(nombre))
print(f"La racine carrée de {nombre} est {racine_carre(nombre)}")

