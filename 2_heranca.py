class Pessoa():

    def andar(self):
        print("estou andando")

    def falar(self):
        print("estou falando")

class cliente(Pessoa):
    def comprar(self):
        print("estou comprando")

class Vendedor(Pessoa):
    def vender(self):
        print("estou vedendo")
