import time
"""
Classe TV: Faça um programa que simule um televisor criando-o como um objeto.
O usuário deve ser capaz de informar o número do canal e aumentar ou diminuir o volume.
Certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas válidas.

"""
class Televisao:
    vdCanaisHabilitados = {2:"Cultura",4:"SBT",5:"Globo",7:"Record",9:"RedeTV",11:"Gazeta",13:"Bandeirantes",
                         21:"Canal 21"}
    VOLUMEMAX = 100
    VOLUMEMIN = 0

    def __init__(self,canal,volume):
        self.canal = canal
        self.volume = volume
        self.canalValor = Televisao.vdCanaisHabilitados[self.canal]

    def disPlay(self):
        return 'Canal:  ' + self.canalValor + '\n' +  'Volume: ' + str(self.volume)

    def aumentaVolume(self):
        self.volume += 1
        self.volume = min(self.volume,100)

    def diminuirVolume(self):
        self.volume += 1
        self.volume = max(0,self.volume)


    def alterarVolDireto(self,piVolume):
        if not self.VOLUMEMIN < piVolume < self.VOLUMEMAX:
            print('Volume informado errado:  ')
        else:
            self.volume = piVolume


    def mudarCanal(self, canal):
        if canal not in Televisao.vdCanaisHabilitados:
            print("Canal: " + str(canal) + " Não habilitado")
        else:
            self.canal = canal
            self.canalValor = Televisao.vdCanaisHabilitados[self.canal]

    def mudarCanalUp(self):
        vbAchou = 0
        viCanal = self.canal
        while vbAchou == 0:
            viCanal += 1
            if viCanal > max(self.vdCanaisHabilitados):
                viCanal = min(self.vdCanaisHabilitados)
            if viCanal in self.vdCanaisHabilitados:
                self.canal = viCanal
                vbAchou = 1
        self.canalValor = self.vdCanaisHabilitados[self.canal]

    def mudarCanalDown(self):
        vbAchou = 0
        viCanal = self.canal
        while vbAchou == 0:
            viCanal -= 1
            if viCanal < min(self.vdCanaisHabilitados):
                viCanal = max(self.vdCanaisHabilitados)
            if viCanal in self.vdCanaisHabilitados:
                vbAchou = 1
                self.canal = viCanal
        self.canalValor = self.vdCanaisHabilitados[self.canal]

def main():
    tv = Televisao(canal=5,volume=20)
    viDesligaTV = 0
    viAcao = 0
    vlvalida = [1,2,3,4,5,6,7,8]
    vnAcao = ''

    while viDesligaTV == 0:
        print("Escolha de Ações: ")
        print("Favor Digitar 1 para Visualizar Canal e Volume:")
        print("Favor Digitar 2 para Informar um Canal:")
        print("Favor Digitar 3 para Pular um Canal:")
        print("Favor Digitar 4 para Voltar um Canal:")
        print("Favor Digitar 5 para aumentar o volume em um ponto:")
        print("Favor Digitar 6 para diminuir o volume em um ponto:")
        print("Favor Digitar 7 para alterar o volume diretamente")
        print("Favor Digitar 8 para desligar a TV")
        vnAcao = input('Favor informar um número:    ')
        if not vnAcao.isnumeric():
            print('Erro!\n O Caracter ' + vnAcao + ' não é um caracter númerico, favor informar um caracter'
                                       + ' correto.')
        else:
            viAcao = int(vnAcao)
            if viAcao not in vlvalida:
                print('Erro!\n Função Inexistente')
            else:
                if viAcao == 1:
                    print(tv.disPlay())
                elif viAcao == 2:
                    tv.mudarCanal(int(input("Favor Informar um Canal: ")))
                elif viAcao == 3:
                    tv.mudarCanalUp()
                elif viAcao == 4:
                    tv.mudarCanalDown()
                elif viAcao == 5:
                    tv.aumentaVolume()
                elif viAcao == 6:
                    tv.diminuirVolume()
                elif viAcao == 7:
                    tv.alterarVolDireto(int(input("Favor Informar o novo Volume:  ")))
                elif viAcao == 8:
                    viDesligaTV = 1
                    print("Desligando")
                time.sleep(3)

main()










