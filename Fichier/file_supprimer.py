import os
# supprimer un fichier 

try:
    print("Suppression du fichier")
    os.remove("delete_data.txt")
except Exception as error:
    print("Probleme lors de la suppression du fichier", error)

finally:
    print("FIN")