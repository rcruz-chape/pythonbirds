class Pessoa:
    olhos = 2
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'
    @staticmethod
    def metodo_estatico():
        return 42
    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

if __name__ == '__main__':
    noemi = Pessoa(nome='Noemi',idade=9)
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
    Pessoa.olhos = 3
    print(angela.__dict__)
    print(noemi.__dict__)
    print(Pessoa.olhos)
    print(angela.olhos)
    print(noemi.olhos)
    print(id(Pessoa.olhos),id(angela.olhos),id(noemi.olhos))
    print(Pessoa.metodo_estatico(),noemi.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(),noemi.nome_e_atributos_de_classe())





