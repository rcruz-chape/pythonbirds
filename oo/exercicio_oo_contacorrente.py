from decimal import Decimal
"""
Classe Conta Corrente: Crie uma classe para implementar uma conta corrente.
A classe deve possuir os seguintes atributos: número da conta, nome do correntista e saldo.
Os métodos são os seguintes: alterarNome, depósito e saque;
No construtor, saldo é opcional, com valor default zero e os demais atributos são obrigatórios.

>>> conta = ContaCorrente(conta=12345,nome='Renato Souza')
>>> conta.alteraNome('Renato Martins Cruz Souza')
>>> print(conta.nome)
Renato Martins Cruz Souza
>>> print(conta.demonstraSaldo())
conta: 12345, Saldo = 0,00
>>> conta.deposito(500)
>>> print(conta.demonstraSaldo())
conta: 12345, Saldo = 500,00
>>> conta.saque(250.99)
>>> print(conta.demonstraSaldo())
conta: 12345, Saldo = 249,01
"""

class ContaCorrente():
    def __init__(self, nome, conta, saldo = 0):
        self.nome = nome
        self.conta = conta
        self.saldo = saldo

    def demonstraSaldo(self):
        return 'Conta:   ' + str(self.conta) + '   Saldo:   '+ str.format(self.saldo)

    def deposito(self,pfValorDeposito):
        self.saldo += pfValorDeposito
        self.saldo = Decimal(self.saldo)

    def saque(self,pfValorSaque):
        self.saldo -= pfValorSaque
        self.saldo = Decimal(self.saldo)
