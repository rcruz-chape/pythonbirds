import time
import multiprocessing
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
        if psNome == '':
            print('Preciso de um nome')
        else:
            self.nome = psNome

    def retornaNome(self):
        return self.nome

    def extraiFome(self):
        self.fome -= 10
        self.fome = max(self.MINFOMESAUDE,self.fome)

    def alterarFome(self,piFome):
        self.fome += piFome
        self.fome = min(self.MAXFOMESAUDE,self.fome)

    def retornaFome(self):
        return str(self.fome)

    def extraiSaude(self):
        self.saude -= 10
        self.saude = max(self.MINFOMESAUDE,self.saude)

    def alteraSaude(self, piSaude):
        self.saude += piSaude
        self.saude = min(self.MAXFOMESAUDE,self.saude)

    def retornaSaude(self):
        return str(self.saude)

    def alteraIdade(self,piIdade):
        self.idade = max(piIdade,0)

    def retornaIdade(self):
        return str(self.idade)

    def retornaHumor(self):
        return ((self.fome * 30)+(self.saude * 50)+2000)/100

    def retornaEstadoHumor(self,piHumor):
        vReturn = ''
        vReturn = 'Estou '
        if piHumor > 90:
            vReturn += 'muito feliz.'
        elif 69 < piHumor < 91:
            vReturn += 'feliz.'
        elif 49 < piHumor < 70:
            vReturn += 'apreensivo.'
        elif 29 < piHumor < 50:
            vReturn += 'muito triste.'
        else:
            vReturn +=  'depressivo.'
        return vReturn

    def cronometroFomeSaude(self):
        viEndtime = time.time() + 10
        while time.time() < viEndtime:
            self.extraiFome()
            if self.fome < 1:
                self.alterarFome(int(input("Estou com fome, preciso ser alimentado.\n Se eu não for alimentado, a saúde"
                                           " será impactada\nDigitar Agora:  ")))
                if self.fome < 1:
                    self.fome = self.MAXFOMESAUDE
                    self.extraiSaude()

            if time.time() >= viEndtime:
                if self.saude > 0:
                    viEndTime =time.time()+10

def main():
    vdFomeSaude = {1:10,2:20,3:30,4:40,5:50}
    viAcao = 0
    vsAcao = ''
    viIdade = -1
    vsNome = ""
    vsIdade = ""
    viHumor = 0
    viVivo = 1
    viEndTime = 0
    print('Olá...Seja Bem Vindo ao Jogo do Tomagochi...')
    vsNome = input("Qual será o meu nome?  ")
    while viIdade < 0:
        vsIdade = input("Quantos anos eu tenho?   ")
        if vsIdade.isnumeric():
            viIdade = int(vsIdade)
            if viIdade < 0:
                print("A Idade inválida, favor dizer a minha idade de maneira correta")
        else:
            print("A Idade informada não é númerica, favor dizer a minha idade de maneira correta")
        time.sleep(1)
    vcTamagochi = BichinhoVirtual(nome=vsNome,idade=viIdade)
    viHumor = vcTamagochi.retornaHumor()
    print('Olá!\n Eu sou ' + vcTamagochi.retornaNome() + '.\nTenho '+ vcTamagochi.retornaIdade() + ' anos\n'
          + vcTamagochi.retornaEstadoHumor(viHumor))
    time.sleep(5)
    viEndTime = time.time() + 10
    while viVivo == 1:
     #   vLock = multiprocessing.Lock()
     #   vLock.acquire()
     #   p = multiprocessing.Process(target=vcTamagochi.cronometroFomeSaude())
     #   p.start()
        if viEndTime < time.time():
            viEndTime = time.time() + 10
            vcTamagochi.extraiFome()
            if vcTamagochi.fome < vcTamagochi.MINFOMESAUDE + 10:
                viFome = int(input("Estou com Fome, preciso comer.\n Se eu passar fome, impactará a minha saúde\n"
                                   "O que vou comer?\n 1 - Batata-Frita\n 2 - Maçã\n 3 - Sanduíche\n 4 - Arroz, "
                                   "Feijão, Bife, Salada\n 5 - Churrasco\n 6 - Nada"))
                if viFome == 6:
                    vcTamagochi.extraiSaude()
                    if vcTamagochi.saude == 0:
                        viVivo == 0
                else:
                    vcTamagochi.alterarFome(viFome)


        if viVivo == 1:
            vsAcao = input("O que eu faço?\n 1 - Mudo Nome \n 2 - Mudo de Idade \n 3 - Me Alimento \n 4 - Tomo Remédio \n "
                           "5 - Consumir\n 6 - Estou Doente\n 7 - Finalizo a Minha Vida    "
                           )

            if vsAcao.isnumeric():
                viAcao = int(vsAcao)
            if viAcao == 1:
                vcTamagochi.alteraNome(input("Qual será o meu novo Nome?   "))
            elif viAcao == 2:
                vcTamagochi.alteraIdade(int(input("Qual será a minha Idade?   ")))
            elif viAcao == 3:
                viAlimento = int(input("O que eu vou comer?\n 1 - Batata-Frita\n 2 - Maçã\n 3 - Sanduíche\n 4 - Arroz, "
                                       "Feijão, Bife, Salada\n 5 - Churrasco\n"))
                for i in vdFomeSaude:
                    if i == viAlimento:
                        vcTamagochi.alterarFome(vdFomeSaude[i])
            elif viAcao == 4:
                viRemedio = int(input("O que Doutor vai fazer?\n 1 - Receitar Anti-Inflamatório\n 2 - Receitar Descanso "
                                      " 3 - Receitar AntiBiótico\n 4 - Internar no Quarto \n 5 - UTI\n"))
                for i in vdFomeSaude:
                    if i == viRemedio:
                        vcTamagochi.alteraSaude(vdFomeSaude[i])
            elif viAcao == 5:
                vcTamagochi.extraiFome()
                if vcTamagochi.fome == vcTamagochi.MAXFOMESAUDE:
                    vcTamagochi.extraiSaude()
                    vcTamagochi.alterarFome()
            elif viAcao == 6:
                vcTamagochi.extraiSaude()
            elif viAcao == 7:
                vsTemCerteza = input("Tem Certeza?\n S - Sim\n N - Não    ")
                if vsTemCerteza.upper() == 'S':
                    vcTamagochi.alterarFome((vcTamagochi.fome*(-1)))
                    vcTamagochi.alteraSaude((vcTamagochi.saude*(-1)))
                    viVivo = 0

            viHumor = vcTamagochi.retornaHumor()
            print('Olá!\n Eu sou ' + vcTamagochi.retornaNome() + '.\nTenho ' + vcTamagochi.retornaIdade() + ' anos\n'
                  + vcTamagochi.retornaEstadoHumor(viHumor))
            time.sleep(5)
        if viVivo == 0:
            print('Adeus mundo cruel. Aqui Jaz o Bichinho Virtual ' + vcTamagochi.retornaNome() + ' aos '
                  + vcTamagochi.retornaIdade()  + 'anos.')
     #   vLock.release()

main()