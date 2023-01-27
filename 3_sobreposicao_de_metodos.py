class Pessoa():

    
    def __init__(self,nome, cpf):
        self.nome = nome
        self.cpf = cpf

class cliente(Pessoa):
    
    
    def __init__(self, id_cliente, nome, cpf):
        super().__init__()
        self.id_cliente = id_cliente




c1 = cliente(2, "caio sampaio", "45454454666")

print(c1.id_cliente)
print(c1.nome)
print(c1.cpf)