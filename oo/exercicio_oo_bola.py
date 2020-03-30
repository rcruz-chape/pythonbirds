"""
Classe Bola: Crie uma classe que modele uma bola:

Atributos: Cor, circunferência, material
Métodos: trocaCor e mostraCor
>>> cor = Cor()
>>> print(cor.mostraCor())
>>> Branco
>>> cor.trocaCor("Vermelho")
>>> print(cor.mostraCor())
>>> Vermelho

"""
class Cor():
    def __init__(self):
        self.cor = 'Branco'
        self.circunfeencai = 1.65
        self.material = 'Capotao'

    def trocaCor(self,psCorTrocada):
        self.cor = psCorTrocada

    def mostraCor(self):
        return self.cor
