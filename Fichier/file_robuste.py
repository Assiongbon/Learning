
def function_ouverture(file_name):
    with open(file_name, mode="r") as file:
        print("Ouverture")
        dictionaire_str = file.read()
        print((dictionaire_str))
        dictionaire = {}
        import json

        dictionaire = json.loads(dictionaire_str)

        print("eau = ", dictionaire["eau"])

    print("Fichier deja fermé")


try:
    function_ouverture("python_da2.json")
except FileNotFoundError as error:
    print("Probleme lors de l'ouverture du fichier", error)
except FileExistsError as t:
    pass

print('FIN')
