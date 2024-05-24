
my_dict = {
    "eau": 12,
    "vin": 10
}


if __name__ == "__main__":
    print("BEGIN VariableDict.py")
    print(type(my_dict))
    print("len(my_dict) =", len(my_dict))
    print("my_dict =", my_dict)

    # Lire un element
    print("my_dict['vin'] =", my_dict["vin"])
    print("my_dict.get('eau', None) =", my_dict.get("eau", None))

    # Lire les clés
    print("my_dict.keys() =", my_dict.keys(), type(my_dict.keys()))

    # Modifier un element
    my_dict["eau"] = 100
    my_dict.update({"alcool": 50})
    print("my_dict =", my_dict)

    # Supprimer un element
    del my_dict["eau"]
    print("my_dict =", my_dict)
    print(my_dict.pop("vin"))
    print("my_dict =", my_dict)
    my_dict = {
        "eau": 12,
        "vin": 10
    }
    my_dict.clear() # tout supprimer
    my_dict = {
        "eau": 12,
        "vin": 10,
        "aliments": {
            "boeuf": 0.5,
            "poulet": 2
        },
        "liste": [1, 2, 3, 4]
    }

    my_dict2 = my_dict.copy()
    my_dict2.update({"jus" : 15})
    print(my_dict2)
    print(my_dict)
    my_dict["aliments"]["poulet"] = 4
    print(my_dict)
    print(my_dict["liste"][-1])



