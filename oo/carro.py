"""
Você deve criar uma classe carro que deverá possuir dois atributos composto por outras duas classes:
    Deverão ser:
    1) Motor
    2) Direção
        1)O motor terá a responsabilidade de controlar a velocidade.
        Ele Oferece os seguintes atributos:
            a) Atributo de dado velocidade
            b) Método acelerar, que deverá incrementar a velocidade de uma unidade
            c) Método frear, que deverá decrementar a velocidade de duas unidades.
        2) A Direção terá responsabilidade de controlar a direção. Ela oferecerá os seguintes atributos:
            a) Valor de Direção com Valores Possíveis: Norte, Sul, Leste, Oeste
            b) Método a Girar Direita
            b) Método a Girar Esquerda
            N
        O       l
            S

"""
class carro():
    def __init__(self, direcao=1, motor=0):
        self.direcao = direcao
        self.motor = motor
    def calcular_velocidade(self):
        return self.motor.velocidade

    def acelerar(self):
        self.motor.acelerar

    def frear(self):
        self.motor.frear

    def calcular_direcao(self):
        return self.direcao.valor

    def girar_a_esquerda(self):
        self.direcao.girando_esquerda()

    def girar_a_direita(self):
        self.direcao.girando_direita()

class Direcao():
    direcoesdct = {
        1: "Norte", 2: "Leste", 3: "Sul", 4: "Oeste"}
    def __init__(self):
        self.direcao = 1
        self.valor = direcao.direcoesdct[self.direcao]

    def girando_direita(self):
        self.direcao =+ 1
        if self.direcao > 4:
            self.direcao = 1
        self.valor=self.direcoesdct[self.direcao]

    def girando_esquerda(self):
        self.direcao =- 1
        if self.direcao > 1:
            self.direcao = 1
        self.valor = self.direcoesdct[self.direcao]


class Motor():
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade -= 2
        self.velocidade = max(0,self.velocidade)















