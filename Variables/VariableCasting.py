

nombre = 3.14

# 10
nombreString = "105"

if __name__ == "__main__":
    print("BEGIN VariableCasting.py")
    nombre_entier = int(nombre)
    print(nombre_entier, type(nombre_entier))
    nombre_reel = float(nombreString)
    print(nombre_reel, type(nombre_reel))
    nombre_entier = int(nombre_reel)
    print(nombre_entier, type(nombre_entier))
    

