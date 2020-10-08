import random
import os
import time
def assets():
    global numeros, naipes, valores, jogando, turno, mao_jogador, mao_bot, soma, soma_bot, opcao, a, x  
    numeros = ("A","2","3","4","5","6","7","8","9","10","J","Q","K")
    naipes = ("espadas", "paus", "copas", "ouros")
    valores = {"A":11,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"1":10,"J":10,"Q":10,"K":10}
    turno = 1
    mao_jogador = []
    mao_bot = []
    soma = 0
    soma_bot = 0
    opcao = None
    a = None
    x = None
jogando = True
fichas = 15
start = True
class Carta():
    def __init__(self,numero,naipe):
        self.numero = numero
        self.naipe = naipe
    
    def __str__(self):
        return self.numero+ " de "+ self.naipe

class Deck():
    def __init__(self):
        self.deck = []
        for naipe in naipes:
            for numero in numeros:
                card = Carta(numero,naipe)
                self.deck.append(str(card))
    
    def __str__(self):
        deck_completo = ''
        for card in self.deck:
            deck_completo +="\n"+ card.__str__()
        return deck_completo

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()

class Jogador(Deck):
    def __init__(self):
        super().__init__()
        global mao_jogador, soma
        self.mao_jogador = mao_jogador
        self.soma = soma

    def soma_jogador(self):
        global valores, turno, total_jogador
        card = self.mao_jogador
        self.soma += valores[card[-1][0]]
        total_jogador = self.soma
        if self.soma > 21:
            turno = 2
            print (f"Você estourou, tendo o valor de {self.soma}")
            input ("Digite algo para continuar. ")
            os.system('cls')
        elif self.soma < 21:
            print (f"Somando um valor de {self.soma}.")
        elif self.soma == 21:
            turno = 2
            print ("Parabéns você conseguiu somar 21!")
            input ("Digite algo para continuar. ")
            os.system('cls')
        

    def cartas_jogador(self):
        global mao_jogador
        self.mao_jogador.append(super().deal())
        self.cartas_atuais = ", ".join(mao_jogador)
        print (f"Suas cartas são: {self.cartas_atuais}")
        if self.mao_jogador[-1][0] == "A":
            self.ajustar_as()

    def ajustar_as(self):
        self.ajustar = None
        while type(self.ajustar) != int:
            while self.ajustar not in [1,11]:
                try:
                    self.ajustar = int(input(f"Você pegou um A, você quer que ele passe a valer 1 ou 11? \nLembrando que sua soma anterior era de {self.soma}: "))
                except ValueError:
                    print ("Isso não é uma opção")
        valores["A"] = self.ajustar

class Bot(Deck):
    def __init__(self):
        global mao_bot, soma_bot
        super().__init__()
        self.mao_bot = mao_bot
        self.soma_bot = soma_bot

    def cartas_bot(self):
        global mao_bot
        self.mao_bot.append(super().deal())
        self.cartas_atuais_bot = ", ".join(mao_bot)
        print (f"As cartas do bot são: {self.cartas_atuais_bot}")

    def somar_bot(self):
        global valores, turno, bot_total
        card_bot = self.mao_bot
        self.soma_bot += valores[card_bot[-1][0]]
        bot_total = self.soma_bot
        if self.soma_bot > 21:
            turno = 3
            print (f"O bot estourou, tendo o valor de {self.soma_bot}")
            input ("Digite algo para continuar. ")
            os.system('cls')
        elif self.soma_bot < 21:
            print (f"Somando um valor de {self.soma_bot}.")
        elif self.soma_bot == 21:
            turno = 3
            print ("O bot conseguiu somar 21!")
            input ("Digite algo para continuar. ")
            os.system('cls')
def jogo():
    global turno, opcao, x, fichas, start
    os.system('cls')
    deck_teste = Jogador()
    deck_bot = Bot()
    deck_teste.shuffle()
    if start == True:
        print ("Bem vindo ao jogo Blackjack, mais conhecido como Vinte e um.\nSeu objetivo neste jogo é pegar cartas e somar seus\nvalores o mais próximo de 21 do que o computador.")
        print ("Porém tome cuidado para não passar de 21 pois, caso isso acontecer você perderá o jogo.")
        print ("Você começa o jogo com 15 fichas, que você deve apostar no início de cada jogo.")
        print ("Se você ganhar, você ganha mais fichas, se perder você perde as que você apostou.")
        print ("Tente alcançar o maior número de fichas!")
        input("Vamos começar? (Digite algo para continuar) ")
        time.sleep(1)
        start = False
        os.system('cls') 
    while turno == 1:
        if x == None:
            while not type(x) == int:
                try:
                     x = int(input(f"Digite quantas fichas você irá apostar nessa rodada, você já tem {fichas}: "))
                except ValueError:
                    print ('Isso não é uma opção!')
        deck_teste.cartas_jogador()
        deck_teste.soma_jogador()
        opcao = None
        if turno == 2:
            break
        while not type(opcao) == int:
            try:
                opcao = int(input("Digite 1 para pegar mais uma carta ou 2 para encerrar sua vez: "))
                break
            except ValueError:
                print ('Isso não é uma opção!')
        if opcao == 2:
            turno = 2
            os.system ('cls')
            break
        time.sleep(1)
        os.system('cls')
    while turno == 2:
        if turno == 3:
            break
        deck_bot.shuffle()
        deck_bot.cartas_bot()
        deck_bot.somar_bot()
        time.sleep(1.5)
    while turno == 3:
        global a, jogando
        if total_jogador > bot_total:
            if total_jogador <= 21:
                print ("Parabéns você venceu e ganhou mais fichas!")
                fichas = round(fichas + (x * 0.7))
            elif total_jogador > 21 and bot_total <= 21:
                print ("Que pena não foi dessa vez! o bot venceu você nesta rodada!") 
                fichas = round(fichas - x)
        elif total_jogador < bot_total:
            if bot_total > 21 and total_jogador <= 21:
                print ("Parabéns você venceu e ganhou mais fichas!")
                fichas = round(fichas + (x * 0.7))
            elif bot_total <= 21:
                print ("Que pena não foi dessa vez! o bot venceu você nesta rodada!")
                fichas = round(fichas - x) 
        elif total_jogador == bot_total and total_jogador <= 21 and bot_total <= 21:
            print ("Esta rodada empatou! Dessa vez você não perde nem ganha nenhuma ficha!")
        else:
            print ("Parece que os dois estouraram então foi empate mas você ainda sim perde algumas fichas!")
            fichas = round(fichas - (x * 0.3))
        print (total_jogador, bot_total)
        x = None
        if fichas <= 0:
            print ("Você ficou sem fichas! Tente denovo outra vez!")
            quit()
        while not type(a) == int:
            try:
                a = int(input("Digite 1 para jogar novamente ou 2 para encerrar: "))
                break
            except ValueError:
                print ('Isso não é uma opção!')
            else:
                if a not in [1,2]:
                    a = None
        if a == 1:
            turno = 0
            break
        elif a == 2:
            jogando = False
            break
       
while jogando:
    assets()
    jogo()