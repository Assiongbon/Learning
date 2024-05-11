
# Class (Person)
#### attributes (nom , age)
#### methodes 

class Person :

    def __init__(self, param_nom, param_age):
        self.nom = param_nom
        self.age = param_age

    def aniversaire(self):
        self.age = self.age + 1

    def changement_de_nom(self, nom):
        self.nom = nom

    def __str__(self):
        return self.nom + " a " + str(self.age) + " ans"



aime = Person("Aime", 21)
fostin = Person("Fostin", 24)
print(aime)
aime.
aime.aniversaire()
aime.changement_de_nom("Aimé")
print(aime)
print("fostin : age =", fostin.age)
