"""
Classe Quadrado: Crie uma classe que modele um quadrado:

Atributos: Tamanho do lado
Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;

>>> quadrado = Quadrado()
>>> print(quadrado.retornaValorlado())
4
>>> print(quadrado.calculaArea())
16
>>> quadrado.mudaValorlado(5)
>>> print(quadrado.retornaValorlado())
5
>>> print(quadrado.calculaArea())
25

"""
class Quadrado():
    def __init__(self):
        self.lado = 4

    def retornaValorlado(self):
        return self.lado

    def calculaArea(self):
        return self.lado ** 2

    def mudaValorlado(self,ladonovo):
        self.lado = ladonovo

