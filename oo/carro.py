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
        Exemplo
        >>>Motor=Motor()
        >>>Motor.Velocidade
        >>>0
        >>>Motor.acelerar
        >>>1
        >>>Motor.acelerar
        >>>2
        >>>Motor.acelerar
        >>>3
        >>>Motor.frear
        >>>1
        >>>Motor.frear
        >>>0
        >>>direcao=Direcao()
        >>>direcao.valor
        >>>'Norte'
        >>>direcao.girando_direita
        >>>'Leste'
        >>>direcao.girando_direita
        >>>'Sul'
        >>>direcao.girando_direita
        >>>'Oeste'
        >>>direcao.girando_direita
        >>>'Norte'
        >>>direcao.girando_esquerda
        >>>'Oeste'
        >>>direcao.girando_esquerda
        >>>'Sul'
        >>>direcao.girando_esquerda
        >>>'Leste'
        >>>direcao.girando_esquerda
        >>>'Norte'
        >>>carro=Carro(direcao,moto)
        >>>carro=Carro.calcular_velocidade()
        0
        >>>carro=Carro.acelerar()
        >>>carro=Carro.calcular_velocidade()
        1
        >>>carro=Carro.frear()
        >>>carro=Carro.calcular_velocidade()
        0
        >>>carro=Carro.calcular_direcao()
        'Norte
        >>>carro=Carro.girar_a_esquerda()
        >>>carro=Carro.calcular_direcao()
        'Oeste
        >>>carro=Carro.girar_a_esquerda()
        >>>carro=Carro.calcular_direcao()
        'Sul
        >>>carro=Carro.girar_a_esquerda()
        >>>carro=Carro.calcular_direcao()
        'Sul
        >>>carro=Carro.girar_direita()
        >>>carro=Carro.calcular_direcao()
        'Oeste
"""
class Motor():
    def __init__(self, velocidade = 0):
        self.velocidade = velocidade

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade -= 2
        if self.velocidade < 0:
            self.velocidade = 0

class Direcao():
    direcoes={1:"Norte",2:"Leste",3:"Sul",4:"Oeste"}

    def __init__(self, direcao=1):
        self.direcao = direcao

    def girando_direita(self):
        self.direcao += 1
        if self.direcao > 4:
            self.direcao = 1
        return direcao.direcoes[self.direcao]

    def girando_esquerda(self):
        self.direcao -= 1
        if self.direcao < 1:
            self.direcao = 4
        global direcoes
        return direcao.direcoes[self.direcao]

class Carro():
    def __init__(self,motor = Motor(),direcao = Direcao()):
        self.motor = motor
        self.direcao = direcao

    @classmethod
    def calcular_velocidade(cls):
        motor = Motor()
        print(motor.velocidade)
        return motor.velocidade


    def acelerar(self):
        motor = Motor()
        motor.acelerar()

    def frear(self):
        motor = Motor()
        motor.frear()
    @classmethod
    def calcula_direcao(cls):
        direcao = Direcao()
        print(direcao.direcoes[Direcao.direcao])
        return direcao.direcoes[Direcao.direcao]

    def girar_esquerda(self):
        direcao = Direcao()
        direcao.girando_esquerda()

    def girar_direita(self):
        direcao = Direcao()
        direcao.girando_direita()
if __name__ == '__main__':
    # Testando motor
    motor = Motor()
    print(motor.velocidade)
    motor.acelerar()
    print(motor.velocidade)
    motor.acelerar()
    print(motor.velocidade)
    motor.acelerar()
    print(motor.velocidade)
    motor.frear()
    print(motor.velocidade)
    motor.frear()
    print(motor.velocidade)
    direcao=Direcao()
    print(direcao.direcoes[direcao.direcao])
    direcao.girando_direita()
    print(direcao.direcoes[direcao.direcao])
    direcao.girando_direita()
    print(direcao.direcoes[direcao.direcao])
    direcao.girando_direita()
    print(direcao.direcoes[direcao.direcao])
    direcao.girando_direita()
    print(direcao.direcoes[direcao.direcao])
    direcao.girando_esquerda()
    print(direcao.direcoes[direcao.direcao])
    direcao.girando_esquerda()
    print(direcao.direcoes[direcao.direcao])
    direcao.girando_esquerda()
    print(direcao.direcoes[direcao.direcao])
    direcao.girando_esquerda()
    direcao.direcoes[direcao.direcao]
    carro=Carro()
    carro.calcular_velocidade()
    carro.acelerar()
    carro.calcular_velocidade()
    carro.acelerar()
    carro.calcular_velocidade()
    carro.acelerar()
    carro.calcular_velocidade()
    carro.frear()
    carro.calcular_velocidade()
    carro.frear()
    carro.calcular_velocidade()
    carro.calcula_direcao()
    carro.girar_direita()
    carro.calcula_direcao()
    carro.girar_direita()
    carro.calcula_direcao()
    carro.girar_direita()
    carro.calcula_direcao()
    carro.girar_direita()
    carro.calcula_direcao()
    carro.girar_esquerda()
    carro.calcula_direcao()
    carro.girar_esquerda()
    carro.calcula_direcao()
    carro.girar_esquerda()
    carro.calcula_direcao()
    carro.girar_esquerda()
    carro.calcula_direcao()













