class Pessoa:
    olhos = 2
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá, meu nome é {self.nome}'
    @staticmethod
    def metodo_estatico():
        return 42
    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

class Homem(Pessoa):
    def cumprimentar(self):
        cumprimentar_da_classe = super().cumprimentar()
        return f'{cumprimentar_da_classe}' + '  Aperto de mão.'

class Mutante(Pessoa):
    olhos = 3

if __name__ == '__main__':
    noemi = Homem(nome='Daniel',idade=9)
    angela = Pessoa(noemi,nome='Angela',idade=39)
    print(Pessoa.cumprimentar(angela))
    print(id(angela))
    print(angela.cumprimentar())
    print(angela.nome)
    print(angela.idade)
    for filho in angela.filhos:
        print([filho.nome,filho.idade])
    angela.sobrenome='Borges'
    del angela.filhos
    noemi.olhos = 1
    del noemi.olhos
    print(angela.__dict__)
    print(noemi.__dict__)
    print(Pessoa.olhos)
    print(angela.olhos)
    print(noemi.olhos)
    print(id(Pessoa.olhos),id(angela.olhos),id(noemi.olhos))
    print(Pessoa.metodo_estatico(),noemi.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(),noemi.nome_e_atributos_de_classe())
    pessoa = Pessoa(nome='Anonimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(noemi, Pessoa))
    print(isinstance(noemi, Homem))
    print(noemi.olhos)
    print(noemi.cumprimentar())



