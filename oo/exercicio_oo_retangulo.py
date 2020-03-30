"""
Classe Retangulo: Crie uma classe que modele um retangulo:

Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local.
Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.


"""
class Retangulo():
    def __init__(self):
        self.largura = 3
        self.comprimento = 4

    def mudaValorlado(self,pFlargura,pFcomprimento):
        self.largura = pFlargura
        self.comprimento = pFcomprimento

    def retornaValorlado(self):
        return 'Largura: '  + str(self.largura) + '\n' + 'Comprimento:   ' + str(self.comprimento)

    def calculaArea(self):
        return self.largura * self.comprimento

    def calculaPerimetro(self):
        return (self.largura * 2) + (self.comprimento * 2)

desejacontinuar = 'O'
retangulo = Retangulo()
while desejacontinuar.upper() != 'N':
    largura = float(input("Favor Informar a Largura do Retangulo: "))
    comprimento = float(input("Favor Informar o Comprimento do Retangulo: "))
    retangulo.mudaValorlado(largura,comprimento)
    print(retangulo.retornaValorlado())
    print("Quantidade de Pisos: " + str(retangulo.calculaArea()))
    print ("Rodapés Necessários: " + str(retangulo.calculaPerimetro()))
    desejacontinuar = input("Deseja Continuar?(S - Sim/N - Não) - ")
    while desejacontinuar.upper() not in ('S','N'):
        desejacontinuar = input("Deseja Continuar?(S - Sim/N - Não) Favor Digitar S ou N  -  ")

