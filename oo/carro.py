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