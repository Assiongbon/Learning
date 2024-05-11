


file = open("data.txt", mode="r") 

print(file.readline())
file.close()

# Ouverture en mode ajout à la fin du fichier

file = open("data.txt", mode="a", encoding="utf-8")
file.write("\nEcriture à la fin du fichier")
file.close()


# Ouverture en mode ecritue dans un fichier inexistant => creation du nouveau fichier

file = open("new_data.txt", mode="w", encoding="utf-8")
file.write("\nEcriture dans le nouveau fichier")
file.close()


dictionaire = {
    "eau" : "water",
    "feu" : "fire",
    "sable" : "sand"
}

import json
file = open("python_data.json", mode="w", encoding="utf-8")
dictionaire_str = json.dumps(dictionaire)
print(dictionaire_str)
file.write(dictionaire_str)
file.close()


