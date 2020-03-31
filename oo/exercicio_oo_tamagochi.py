import time

"""
Classe Bichinho Virtual:Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):

Atributos: Nome, Fome, Saúde e Idade b. Métodos: Alterar Nome, Fome, Saúde e Idade; Retornar Nome, Fome, Saúde e Idade 
Obs: Existe mais uma informação que devemos levar em consideração, o Humor do nosso tamagushi, 
este humor é uma combinação entre os atributos Fome e Saúde, 
ou seja, um campo calculado, então não devemos criar um atributo para armazenar esta informação 
por que ela pode ser calculada a qualquer momento.
"""


class BichinhoVirtual:
    MINFOMESAUDE = 0
    MAXFOMESAUDE = 100
    def __init__(self, nome="Renato", saude=100, fome=100, idade=0):
        self.nome = nome
        self.saude = saude
        self.fome = fome
        self.idade = idade

    def alteraNome(self,psNome):
        if psNome = '':
            print('Preciso de um nome')
        else:
            self.nome = psNome

    def retornaNome(self):
        return self.nome

    def extraiFome(self):
        self.fome -= 1
        self.fome = max(self.MINFOMESAUDE,self.fome)

    def alterarFome(self,piFome):
        self.fome += piFome
        self.fome = min(self.MAXFOMESAUDE,self.fome)

    def retornaFome(self):
        return str(self.fome)

    def extraiSaude(self):
        self.saude -= 1
        self.saude = max(self.MINFOMESAUDE,self.fome)

    def alteraSaude(self, piSaude):
        self.saude += piSaude
        self.saude = min(self.MAXFOMESAUDE,self.saude)

    def retornaSaude(self):
        return str(self.saude)

    def alteraIdade(self,piIdade):
        self.idade = max(piIdade,0)

    def retornaIdade(self):
        return str(self.nome)

def main()
main()