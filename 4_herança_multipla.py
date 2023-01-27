class Animal:
    def andar(self):
        print("estou andando como um animal")
    
    def correr(self):
        print("estou correndo")

    def pular(self):
        print('estou pulando')
    
class Felino():
    def felino(self):
        print("eu sou um felino")


class Gato(Felino, Animal):
    def miar(self):
        print("estou andando como um gato")

class Cachorro(Animal):
    def latir(self):
        print("estou latindo")



y = Gato()
y.andar()