"""
Classe Pessoa: Crie uma classe que modele uma pessoa:

Atributos: nome, idade, peso e altura
Métodos: Envelhercer, engordar, emagrecer, crescer.
A média de crescimento das crianças no primeiro ano de vida é de 25cm, já no segundo é de 12cm. No terceiro ano,
a média cai para 7 e, a partir dos quatro, a média é de 7. Após dos dez, o crescimento desacelera.
Mas, durante essa época, pode chegar a ser de 5. Terminando com 20 anos.

>>> pessoa.Pessoa()
>>> print(pessoa.caracteristica())
Nome: Renato Martins Cruz Souza
Idade: 0 ano
Peso: 3 kg
Altura: 48 cm
>>>pessoa.enVelhecer(10)
>>> print(pessoa.caracteristica())
Nome: Renato Martins Cruz Souza
Idade: 10 anos
Peso: 3 kg
Altura: 154 cm
>>>pessoa.engordar(29)
>>> print(pessoa.caracteristica())
Nome: Renato Martins Cruz Souza
Idade: 10 anos
Peso: 32 kg
Altura: 147 cm
>>>pessoa.enVelhercer(10)
>>> print(pessoa.caracteristica())
Nome: Renato Martins Cruz Souza
Idade: 20 anos
Peso: 32 kg
Altura: 197 cm
>>>pessoa.engordar(69)
>>> print(pessoa.caracteristica())
Nome: Renato Martins Cruz Souza
Idade: 20 anos
Peso: 101 kg
Altura: 197 cm
>>>pessoa.enVelhercer(20)
>>> print(pessoa.caracteristica())
Nome: Renato Martins Cruz Souza
Idade: 40 anos
Peso: 101 kg
Altura: 197 cm
>>>pessoa.crescer(10)
>>> print(pessoa.caracteristica())
Nome: Renato Martins Cruz Souza
Idade: 40 anos
Peso: 101 kg
Altura: 207 cm
>>>pessoa.engordar(60)
>>> print(pessoa.caracteristica())
Nome: Renato Martins Cruz Souza
Idade: 40 anos
Peso: 161 kg
Altura: 207 cm
>>>pessoa.emagrecer(81)
>>> print(pessoa.caracteristica())
Nome: Renato Martins Cruz Souza
Idade: 40 anos
Peso: 80 kg
Altura: 207 cm
A média de crescimento das crianças no primeiro ano de vida é de 25cm, já no segundo é de 12cm. No terceiro ano,
a média cai para 7 e, a partir dos quatro, a média é de 7. Após dos dez, o crescimento desacelera.
Mas, durante essa época, pode chegar a ser de 5. Terminando com 20 anos.
"""

class Pessoa():
    vDmediacrescimento = {1:25,2:12,3:7,4:7,5:7,6:7,7:7,8:7,9:7,10:5,11:5,12:5,13:5,14:5,15:5,16:5,17:5,18:5,19:5,20:5}
    def __init__(self):
        self.nome = "Renato Martins Cruz Souza"
        self.idade = 0
        self.peso = 3
        self.altura = 48

    def crescer(self,piAlturaNew):
        self.altura += piAlturaNew

    def emagrecer(self,piPesoNew):
        self.peso -= piPesoNew
        self.peso = max(0,self.peso)

    def engordar(self, piPesoNew):
        self.peso += piPesoNew

    def envelhecer(self,piIdadeNew):
        bTesteIdade = true
        if self.idade > 20:
            bTesteIdade = false
        if bTesteIdade:
            vidade = self.idade + piIdadeNew
            vidadeinicial = self.idade
            for vidadeinicial in vidade:
                self.crescer(self.vDmediacrescimento[vidadeinicial])
        self.idade =+ piIdadeNew



    def caracteristica(self):
        return 'Nome: ' + self.nome + '\n' +
               'Idade: ' + str(self.idade) ' anos \n' +
               'Peso: ' + str(self.peso) ' Kg \n' +
               'Altura: ' + str(self.altura) ' cm '



