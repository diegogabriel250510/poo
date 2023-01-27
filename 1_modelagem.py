class Pessoas:
   possui_olho = True
   possui_boca = True
   raça = "ser humano"
   
   def __init__(self , nome,idade):
        self.nome = nome
        self.idade = idade
   
   def retorna_nome(self):
     return self.nome     
   
   def logar_sistema(self):
        print(f'{self.retorna_nome()} esta logando no sistema')    
   
   @classmethod
   def andar(cls):
     cls.possui_boca = False
     return None

   @staticmethod
   def e_adulto(idade):
     if idade > 18:
          return True
     return False


# p1 = Pessoas('caio sampaio', 21)
# p2 = Pessoas('marcos sampaio', 45)

print(Pessoas.e_adulto(12))

