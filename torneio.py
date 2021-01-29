import random as r
from os import system, name 
import time

def clear(): 
  
    if name == 'nt': 
        _ = system('cls') 
  
    else: 
        _ = system('clear') 

lutas = ["Judô","Karatê","Jiu-Jitsu"]

torneios = []

lutadorescadastrados = []

faixas = ["branca","cinza","amarela","laranja","verde","roxa","azul","marrom","vermelha","preta","livre"]

def classificarForça(força,odio,experiencia):
    return (força+odio*2+experiencia)/4

def trocarposição(lista,index1,index2):
    aux = lista[index2]
    lista[index2] = lista[index1]
    lista[index1] = aux

class Lutador:
    vitorias = 0
    derrotas = 0
    experiencia = 0
    inimigosderrotados = []
    def __init__(self, nome, idade, peso, força, faixa, artemarcial,odio):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.força = força
        self.faixa = faixa
        self.artemarcial=artemarcial
        self.odio = odio
    def adicionarVitoria(self):
        self.vitorias += 1
        self.experiencia += 5
    def adicionarDerrota(self):
        self.derrotas += 1
        self.experiencia += 10
    def checarInimigo(self,inimigo):
        for i in self.inimigosderrotados:
            if inimigo == self.inimigosderrotados[i]:
                return True
        return False


class Torneio:
    lutadoresinscritos = []
    ordemranking=[]
    faixas = []
    def __init__(self,nome,lutatorneio,pesomaximo,pesominimo,faixa):
        self.nome = nome
        self.lutatorneio = lutatorneio
        self.pesomaximo = pesomaximo
        self.pesominimo = pesominimo
        self.faixas.append(faixa)
    def inscreverLutador(self,lutador):
        self.lutadoresinscritos.append(lutador)
    def colocarFaixas(self,maisfaixa):
        self.faixas.append(maisfaixa)
    def ordenarRanking(self):
        for i in range(0,len(self.lutadoresinscritos)):
            self.ordemranking.append(self.lutadoresinscritos[i])
        for i in range(0,len(self.ordemranking)-1):
            for i in range(0,len(self.ordemranking)-1):
                if self.ordemranking[i+1].vitorias>self.ordemranking[i].vitorias:
                    trocarposição(self.ordemranking,i,i+1)
                elif self.ordemranking[i+1].vitorias==self.ordemranking[i] and self.ordemranking[i+1].derrotas<self.ordemranking[i].derrotas:
                    trocarposição(self.ordemranking,i,i+1)
                elif self.ordemranking[i+1].vitorias==self.ordemranking[i] and self.ordemranking[i+1].derrotas==self.ordemranking[i].derrotas and self.ordemranking[i+1].checarInimigo(self.ordemranking[i].nome)==True and self.ordemranking[i].checarInimigo(self.ordemranking[i+1].nome)==False:
                    trocarposição(self.ordemranking,i,i+1)
            


    

#menu principal
escolhaValida = False
torneioinvalido=False
jogo=True
jogo1=True
jogo2=True
jogo3=True
jogo4=True
jogo5=True
jogo6=True
jogo7=True
jogo8=True
jogo9=True
jogo10=True
jogo11=True

while jogo==True:
    clear()
    jogo1=True
    jogo2=True
    jogo3=True
    jogo4=True
    jogo5=True
    jogo6=True
    jogo7=True
    jogo8=True
    jogo9=True
    jogo10=True
    jogo11=True
    print("\n########## OLÁ CAMPEÃO ##########\n")
    print("Seja bem-vindo ao MENU PRINCIPAL do nosso sistema!")
    print("Aqui você pode criar torneio de artes marciais personalizados e seus próprios lutadores com atributos definidos por você!!")
    print("Escolha uma das opções abaixo para começar a se divertir:\n")
    print("1 - MENU DE TORNEIO\n Crie torneios, realize suas lutas e muito mais!\n\n")
    print("2 - MENU DE LUTADOR\n Crie e cadastre lutadores e veja detalhes de cada um!\n\n")
    print("3 - CRIAR TORNEIO ALEATÓRIO\n Crie um torneio completamente aleatório, com lutadores criados aleatoriamente!\n\n")
    print("4 - SAIR DO SISTEMA\n\n")
    escolhaValida=False
    while escolhaValida==False:
        try:
            escolhamenu = int(input("Digite o identificador numérico da opção que você deseja: "))
            if 0<escolhamenu<=4:
                escolhaValida=True
            else:
                print("Entre com um valor numérico, correspondente ao que deseja acessar no menu, sendo este 1, 2, 3 ou 4!!")
        except:
            print("Entre com um valor numérico, correspondente ao que deseja acessar no menu, sendo este 1, 2, 3 ou 4!!")

    clear()
    escolhaValida=False
    #menu de torneio
    if escolhamenu==1:
        while jogo1 == True:
            jogo1=True
            jogo2=True
            jogo3=True
            jogo4=True
            jogo5=True
            jogo6=True
            jogo7=True
            jogo8=True
            jogo9=True
            jogo10=True
            jogo11=True
            escolhaValida=False
            print("Seja bem-vindo ao MENU DE TORNEIO do nosso sistema!")
            print("Aqui você pode:\n")
            print("1 - Criar torneios de luta!\n\n")
            print("2 - Inscrever lutadores já cadastrados no sistema no torneio de sua escolha!\n\n")
            print("3 - Ver torneios existentes!\n\n")
            print("4 - Ver ranking do torneio de sua escolha!\n\n")
            print("5 - Ver lutadores inscritos em um torneio de sua escolha!!\n\n")
            print("6 - Realizar luta entre dois lutadores de sua escolha!\n\n")
            print("7 - Retornar ao menu principal!\n\n")
            while escolhaValida==False:
                try:
                    escolhamenu = int(input("Digite o identificador numérico da opção que você deseja: "))
                    if 0<escolhamenu<=7:
                        escolhaValida=True
                    else:
                        print("Entre com um valor numérico, correspondente ao que deseja acessar no menu, sendo este 1, 2, 3, 4, 5, 6 ou 7!!")
                except:
                    print("Entre com um valor numérico, correspondente ao que deseja acessar no menu, sendo este 1, 2, 3, 4, 5, 6 ou 7!!")
            clear()
            escolhaValida=False
            #criar torneio
            if escolhamenu==1:
                while jogo2==True:
                    torneioinvalido=False
                    print("Temos torneios de: \n")
                    print("1 - JUDÔ\n")
                    print("2 - KARATÊ\n")
                    print("3 - JIU-JITSU\n")
                    while escolhaValida==False:
                        try:
                            escolhamenu = int(input("Digite o identificador numérico da opção que você deseja: "))
                            if 0<escolhamenu<=3:
                                escolhaValida=True
                            else:
                                print("Entre com um valor numérico, correspondente ao que deseja acessar no menu, sendo este 1, 2 ou 3!!")
                        except:
                            print("Entre com um valor numérico, correspondente ao que deseja acessar no menu, sendo este 1, 2 ou 3!!")
                    escolhaValida=False
                    if escolhamenu==1:
                        luta = lutas[0]
                    elif escolhamenu==2:
                        luta = lutas[1]
                    else:
                        luta = lutas[2]

                    clear()
                    
                    while escolhaValida==False:
                        torneioinvalido=False
                        nome = input("\nEscolha um nome para o torneio:\n")
                        for i in range (0,len(torneios)):
                            if nome == torneios[i].nome:
                                print("Nome de torneio já existe! Por favor insira um nome diferente para o seu torneio!\n")
                                torneioinvalido=True
                        if torneioinvalido==False:
                            escolhaValida=True

                    escolhaValida=False                    

                    clear()

                    while escolhaValida==False:
                        try:
                            pesominimo = int(input("Digite o peso mínimo do lutador para este torneio: "))
                            if 50<pesominimo<=150:
                                escolhaValida=True
                            else:
                                print("Entre com um valor numérico que esteja entre 50 e 150!!")
                        except:
                            print("Entre com um valor numérico que esteja entre 50 e 150!!")   

                    clear()
                    escolhaValida=False

                    while escolhaValida==False:
                        try:
                            pesomaximo = int(input("Digite o peso máximo do lutador para este torneio: "))
                            if 50<pesomaximo<=150 and (pesomaximo-pesominimo)<=10:
                                escolhaValida=True
                            else:
                                print("Entre com um valor numérico maior que {a} e  menor que 150!!/n".format(a=pesominimo))
                                print("Lembrando que o lutador de menor peso só pode ter 10kg a menos que o lutador de maior peso")
                        except:
                            print("Entre com um valor numérico maior que {a} e  menor que 150!!/n".format(a=pesominimo))
                            print("Lembrando que o lutador de menor peso só pode ter 10kg a menos que o lutador de maior peso") 
                    clear()
                    escolhaValida=False
                    multiplasfaixas=False
                    faixaux = []
                    while escolhaValida==False:
                        faixa = input("Digite a faixa que os participantes do torneio deverão ter para participar: ")
                        if faixa.lower() not in faixas:
                            print("Entre com uma faixa válida! Ela pode ser: ")
                            print("branca, cinza, amarela, laranja, verde, roxa, azul, marrom, vermelha, preta\n")
                        else:
                            faixaux.append(faixa.lower())
                            while escolhaValida==False:
                                maisfaixa = input("Deseja incluir mais alguma faixa? Digite s ou n: \n")
                                if maisfaixa.lower() != "s" and maisfaixa.lower() != "sim" and maisfaixa.lower() != "n" and maisfaixa.lower() != "nao":
                                    print("Digite apenas a letra 's' ou a letra 'n'!!!\n")
                                else:
                                    escolhaValida = True
                            escolhaValida = False
                            if maisfaixa.lower()=="n" or maisfaixa.lower()=="nao":
                                escolhaValida=True
                            else:
                                multiplasfaixas = True

                    for i in range(0,len(torneios)):
                        if nome == torneios[i].nome:
                            print("Torneio invalido! Nome de torneio já existe.")
                            torneioinvalido = True

                    if torneioinvalido!=True:
                        torneios.append(Torneio(nome,luta,pesomaximo,pesominimo,faixaux[0]))  
                    if multiplasfaixas==True:
                        for i in range (0,len(faixaux)):
                            if faixaux[i] not in torneios[-1].faixas:
                                torneios[-1].colocarFaixas(faixaux[i])
                    clear()
                    print("Torneio criado com sucesso!!")
                    escolhaValida=False
                    while escolhaValida==False:
                        print("Deseja criar mais torneios ou voltar ao menu de torneios?\n")
                        maistorneio = input("Digite s para criar mais torneios ou digite n para voltar ao menu de torneios: ")
                        if maistorneio.lower() != "s" and maistorneio.lower() != "sim" and maistorneio.lower() != "n" and maistorneio.lower() != "nao":
                            print("Digite apenas a letra 's' ou a letra 'n'!!!\n")
                        else:
                            escolhaValida = True
                    if maistorneio.lower()!="s" and maistorneio.lower()!="sim":
                        jogo2 = False
                    escolhaValida==False
                    clear()                    
            #inscrever jogador em torneio 
            elif escolhamenu==2:  
                while jogo3==True:
                   
                    faixavalida = False
                    pesovalido = False
                    artemarcialvalida = False
                    lutadorvalido=False
                    escolhaValida=False
                    if len(torneios)==0:
                        print("Infelizmente, ainda nao existem torneios criados.\n")
                        print("Volte ao Menu de Torneios para criar seu Torneio personalizado!!")
                        jogo3=False
                    elif len(lutadorescadastrados)==0:
                        print("Infelizmente, ainda nao existem lutadores cadastrados.")
                        print("Por favor entre no Menu de Lutador para cadastrar lutadores")
                        jogo3=False
                    else:
                        print("Hora de inserir alguns lutadores nos torneios!!\n")
                        print("Os torneios existentes no momento são: \n")
                        while escolhaValida==False:
                            for i in range(0,len(torneios)):
                                print("{a}\n".format(a=torneios[i].nome))
                            torneio = input("Digite o nome exato de algum dos torneios acima listados: ")
                            for i in range(0,len(torneios)):
                                if torneio == torneios[i].nome:
                                    indextorneio = i
                                    escolhaValida = True
                        clear()
                        print("\nEscolha um destes lutadores para inscrevê-lo no torneio selecionado:\n")
                        escolhaValida=False
                        while escolhaValida==False:
                            for i in range(0,len(lutadorescadastrados)):
                                print("{a}\n".format(a=lutadorescadastrados[i].nome))
                            lutador = input("Digite o nome exato de algum dos lutadores acima listados para inscrevê-lo no torneio: \n")
                            for i in range(0,len(lutadorescadastrados)):
                                if lutador == lutadorescadastrados[i].nome:
                                    indexlutador = i
                                    escolhaValida = True
                        if lutadorescadastrados[indexlutador] not in torneios[indextorneio].lutadoresinscritos:
                            lutadorvalido=True
                        if lutadorescadastrados[indexlutador].faixa in torneios[indextorneio].faixas:
                            faixavalida=True
                        if torneios[indextorneio].pesomaximo>=lutadorescadastrados[indexlutador].peso and lutadorescadastrados[indexlutador].peso>=torneios[indextorneio].pesominimo:
                            pesovalido=True
                        if torneios[indextorneio].lutatorneio == lutadorescadastrados[indexlutador].artemarcial:
                            artemarcialvalida=True
                        if artemarcialvalida==True and pesovalido==True and faixavalida==True and lutadorvalido==True:
                            torneios[indextorneio].inscreverLutador(lutadorescadastrados[indexlutador])  
                            print("{a} cadastrado com sucesso!!".format(a=lutadorescadastrados[indexlutador].nome)) 
                            time.sleep(1)
                            clear()
                        else:
                            print("Lutador {a} invalido para este torneio.".format(a=lutadorescadastrados[indexlutador].nome))
                            print("Luta do torneio: {a}".format(a=torneios[indextorneio].lutatorneio))
                            print("Faixas permitidas no torneio: ")
                            for i in range(0,len(torneios[indextorneio].faixas)):
                                print("{a}" .format(a=torneios[indextorneio].faixas[i]))
                            print("Peso máximo: {a}".format(a=torneios[indextorneio].pesomaximo))                      
                            print("Peso mínimo: {a}".format(a=torneios[indextorneio].pesominimo))
                        escolhaValida=False
                        
                        while escolhaValida==False:
                            print("Deseja tentar inscrever mais jogadores ou voltar ao menu de torneios?")
                            maisinscricao = input("Digite s para inscrever mais jogadores ou digite n para voltar ao menu de torneios: ")
                            if maisinscricao.lower() != "s" and maisinscricao.lower() != "sim" and maisinscricao.lower() != "n" and maisinscricao.lower() != "nao":
                                print("Digite apenas a letra 's' ou a letra 'n'!!!\n")
                            else:
                                escolhaValida = True
                        
                        if maisinscricao.lower()!="s" and maisinscricao.lower()!="sim":
                            jogo3 = False
                        clear()
            #ver torneios existentes
            elif escolhamenu==3:
                print("Torneios existentes: ")
                for i in range (0,len(torneios)):
                    print("{a}\n\n".format(a=torneios[i].nome))
                time.sleep(2)
            #ver ranking de algum torneio
            elif escolhamenu==4:
                while jogo5==True:
                    if len(torneios)==0:
                        print("Infelizmente, ainda nao existem torneios criados.\n")
                        print("Volte ao Menu de Torneios para criar seu Torneio personalizado!!")
                        jogo6=False
                    elif len(lutadorescadastrados)==0:
                        print("Infelizmente, ainda nao existem lutadores cadastrados.")
                        print("Por favor entre no Menu de Lutador para cadastrar lutadores")
                        jogo6=False
                    else:
                        print("Os torneios existentes no momento são: ")
                        escolhaValida=False
                        while escolhaValida==False:
                            for i in range(0,len(torneios)):
                                print("{a}\n".format(a=torneios[i].nome))
                            torneio = input("Digite o nome exato de algum dos torneios acima listados: ")
                            for i in range(0,len(torneios)):
                                if torneio == torneios[i].nome:
                                    indextorneio = i
                                    escolhaValida = True
                        clear()
                        torneios[indextorneio].ordenarRanking()
                        for i in range(0,len(torneios[indextorneio].lutadoresinscritos)):
                            print("{a} - {b}".format(a=i+1,b=torneios[indextorneio].ordemranking[i].nome))
                        escolhaValida=False
                        while escolhaValida==False:
                            print("Deseja ver rankings de mais torneios?\n")
                            maisinscricao = input("Digite s para ver rankings de outros torneios ou digite n para voltar ao menu de torneios: ")
                            if maisinscricao.lower() != "s" and maisinscricao.lower() != "sim" and maisinscricao.lower() != "n" and maisinscricao.lower() != "nao":
                                print("Digite apenas a letra 's' ou a letra 'n'!!!\n")
                            else:
                                escolhaValida = True
                        
                        if maisinscricao.lower()!="s" and maisinscricao.lower()!="sim":
                            jogo5 = False
                        clear()
                    
            #ver jogadores inscritos em algum torneio
            elif escolhamenu==5:
                while jogo6==True:
                    clear()
                    if len(torneios)==0:
                        print("Infelizmente, ainda nao existem torneios criados.\n")
                        print("Volte ao Menu de Torneios para criar seu Torneio personalizado!!")
                        jogo6=False
                    elif len(lutadorescadastrados)==0:
                        print("Infelizmente, ainda nao existem lutadores cadastrados.")
                        print("Por favor entre no Menu de Lutador para cadastrar lutadores")
                        jogo6=False
                    else:
                        print("Os torneios existentes no momento são: ")
                        escolhaValida=False
                        while escolhaValida==False:
                            for i in range(0,len(torneios)):
                                print("{a}\n".format(a=torneios[i].nome))
                            torneio = input("Digite o nome exato de algum dos torneios acima listados: ")
                            for i in range(0,len(torneios)):
                                if torneio == torneios[i].nome:
                                    indextorneio = i
                                    escolhaValida = True
                        clear()
                        print("Lutadores inscritos: ")
                        for i in range (0,len(torneios[indextorneio].lutadoresinscritos)):
                            print("{a}\n".format(a=torneios[indextorneio].lutadoresinscritos[i].nome))
                        time.sleep(2)
                        escolhaValida=False
                        while escolhaValida==False:
                            print("Deseja ver mais lutadores ou voltar ao menu de torneios?")
                            continuar = input("Digite s para ver mais jogadores ou digite n para voltar ao menu de torneios: ")
                            if continuar.lower() != "s" and continuar.lower() != "sim" and continuar.lower() != "n" and continuar.lower() != "nao":
                                print("Digite apenas a letra 's' ou a letra 'n'!!!\n")
                            else:
                                escolhaValida = True
                        if continuar.lower()!="s" or continuar.lower()!="sim":
                            jogo6 = False
            #começar luta entre dois oponentes
            elif escolhamenu==6:
                while jogo7==True:
                    clear()
                    escolhaValida=False
                    if len(torneios)==0:
                        print("Infelizmente, ainda nao existem torneios criados.\n")
                        print("Volte ao Menu de Torneios para criar seu Torneio personalizado!!")
                        jogo7=False
                    elif len(lutadorescadastrados)<2:
                        print("Infelizmente ainda nao existem lutadores suficientes cadastrados para começar uma luta")
                        print("Por favor entre no Menu de Lutador para cadastrar lutadores")
                        jogo7=False
                    else:
                        print("Hora de inserir alguns lutadores nos torneios!!\n")
                        print("Os torneios existentes no momento são: ")
                        while escolhaValida==False:
                            for i in range(0,len(torneios)):
                                print("{a}\n".format(a=torneios[i].nome))
                            torneio = input("Digite o nome exato de algum dos torneios acima listados: ")
                            for i in range(0,len(torneios)):
                                if torneio == torneios[i].nome:
                                    indextorneio = i
                                    escolhaValida = True
                        escolhaValida=False
                        clear()
                        if len(torneios[indextorneio].lutadoresinscritos)>=2:
                            counter = 0
                            print("\nEscolha dois destes lutadores para lutar pelo torneio selecionado:\n")
                            escolhaValida=False
                            while escolhaValida==False:
                                for i in range(0,len(torneios[indextorneio].lutadoresinscritos)):
                                    print("{a}\n".format(a=torneios[indextorneio].lutadoresinscritos[i].nome))
                                lutador1 = input("Digite o nome exato de algum dos lutadores acima listados para ser o primeiro dos dois lutadores: ")
                                for i in range(0,len(torneios[indextorneio].lutadoresinscritos)):
                                    if lutador1 == torneios[indextorneio].lutadoresinscritos[i].nome:
                                        indexlutador1 = i
                                        escolhaValida = True
                            clear()
                            for i in range (0,len(torneios[indextorneio].lutadoresinscritos)):
                                if torneios[indextorneio].lutadoresinscritos[i].faixa==torneios[indextorneio].lutadoresinscritos[indexlutador1].faixa:
                                    counter += 1
                            escolhaValida = False
                            if counter-1>=1:
                                while escolhaValida==False:
                                    for i in range(0,len(torneios[indextorneio].lutadoresinscritos)):
                                        print("{a}\n".format(a=torneios[indextorneio].lutadoresinscritos[i].nome))
                                    lutador2 = input("Digite o nome exato de algum dos lutadores acima listados, sem ser o mesmo selecionado antes, para ser o segundo lutador: ")
                                    for i in range(0,len(torneios[indextorneio].lutadoresinscritos)):
                                        if lutador2 == torneios[indextorneio].lutadoresinscritos[i].nome and indexlutador1!=i:
                                            indexlutador2 = i
                                            escolhaValida = True
                                            
                                clear()
                                escolhaValida=False
                                print("Calculando resultado da batalha")
                                time.sleep(0.5)
                                print(".")
                                time.sleep(0.5)
                                print(".")
                                time.sleep(0.5)
                                print(".")
                                time.sleep(0.2)
                                clear()
                                if classificarForça(torneios[indextorneio].lutadoresinscritos[indexlutador1].força,torneios[indextorneio].lutadoresinscritos[indexlutador1].odio,torneios[indextorneio].lutadoresinscritos[indexlutador1].experiencia) > classificarForça(torneios[indextorneio].lutadoresinscritos[indexlutador2].força,torneios[indextorneio].lutadoresinscritos[indexlutador2].odio,torneios[indextorneio].lutadoresinscritos[indexlutador2].experiencia):
                                    torneios[indextorneio].lutadoresinscritos[indexlutador1].adicionarVitoria()
                                    torneios[indextorneio].lutadoresinscritos[indexlutador1].inimigosderrotados.append(torneios[indextorneio].lutadoresinscritos[indexlutador2].nome)
                                    torneios[indextorneio].lutadoresinscritos[indexlutador2].adicionarDerrota()
                                    print("Vitoria de {a}!!!".format(a=torneios[indextorneio].lutadoresinscritos[indexlutador1].nome))
                                elif classificarForça(torneios[indextorneio].lutadoresinscritos[indexlutador1].força,torneios[indextorneio].lutadoresinscritos[indexlutador1].odio,torneios[indextorneio].lutadoresinscritos[indexlutador1].experiencia) < classificarForça(torneios[indextorneio].lutadoresinscritos[indexlutador2].força,torneios[indextorneio].lutadoresinscritos[indexlutador2].odio,torneios[indextorneio].lutadoresinscritos[indexlutador2].experiencia):
                                    torneios[indextorneio].lutadoresinscritos[indexlutador2].adicionarVitoria()
                                    torneios[indextorneio].lutadoresinscritos[indexlutador2].inimigosderrotados.append(torneios[indextorneio].lutadoresinscritos[indexlutador1].nome)
                                    torneios[indextorneio].lutadoresinscritos[indexlutador1].adicionarDerrota()
                                    print("Vitoria de {a}!!!".format(a=torneios[indextorneio].lutadoresinscritos[indexlutador2].nome))
                                else:
                                    randomico = r.randint(1,2)
                                    if randomico==1:
                                        torneios[indextorneio].lutadoresinscritos[indexlutador1].adicionarVitoria()
                                        torneios[indextorneio].lutadoresinscritos[indexlutador1].inimigosderrotados.append(torneios[indextorneio].lutadoresinscritos[indexlutador2].nome)
                                        torneios[indextorneio].lutadoresinscritos[indexlutador2].adicionarDerrota()
                                        print("Vitoria de {a}!!!".format(a=torneios[indextorneio].lutadoresinscritos[indexlutador1].nome))
                                    else:
                                        torneios[indextorneio].lutadoresinscritos[indexlutador2].adicionarVitoria()
                                        torneios[indextorneio].lutadoresinscritos[indexlutador1].inimigosderrotados.append(torneios[indextorneio].lutadoresinscritos[indexlutador2].nome)
                                        torneios[indextorneio].lutadoresinscritos[indexlutador1].adicionarDerrota()
                                        print("Vitoria de {a}!!!".format(a=torneios[indextorneio].lutadoresinscritos[indexlutador2].nome))
                                escolhaValida=False
                                while escolhaValida==False:
                                    print("Deseja realizar mais lutas ou voltar ao menu de torneios?")
                                    continuar = input("Digite s para realizar mais lutas ou digite n para voltar ao menu de torneios: ")
                                    if continuar.lower() != "s" and continuar.lower() != "sim" and continuar.lower() != "n" and continuar.lower() != "nao":
                                        print("Digite apenas a letra 's' ou a letra 'n'!!!\n")
                                    else:
                                        escolhaValida = True
                                if continuar.lower()!="s" and continuar.lower()!="sim":
                                    jogo7 = False
                                
                
                            else:
                                print("Não existe nenhum lutador com a mesma faixa do primeiro lutador selecionado! Lutas entre competidores apenas acontecem quando estes possuem a mesma faixa!!")
                                jogo7=False
                        else:
                            print("Numero de lutadores inscritos no torneio é insuficiente para começar uma luta")
                            jogo7=False
            
            elif escolhamenu==7:
                jogo1 = False
    
    #menu de lutador
    elif escolhamenu == 2:
        while jogo8==True:
            jogo1=True
            jogo2=True
            jogo3=True
            jogo4=True
            jogo5=True
            jogo6=True
            jogo7=True
            jogo8=True
            jogo9=True
            jogo10=True
            jogo11=True
            print("Seja bem-vindo ao MENU DE LUTADOR do nosso sistema!")
            print("Aqui você pode:\n")
            print("1 - Cadastrar lutadores!\n\n")
            print("2 - Ver todos os lutadores cadastrados!\n\n")
            print("3 - Ver detalhes sobre cada lutador!\n\n")
            print("4 - Retornar ao menu principal!\n\n")

            while escolhaValida==False:
                try:
                    escolhamenu = int(input("Digite o identificador numérico da opção que você deseja: "))
                    if 0<escolhamenu<=4:
                        escolhaValida=True
                    else:
                        print("Entre com um valor numérico, correspondente ao que deseja acessar no menu, sendo este 1, 2, 3 ou 4!!")
                except:
                    print("Entre com um valor numérico, correspondente ao que deseja acessar no menu, sendo este 1, 2, 3 ou 4!!")
            clear()
            escolhaValida=False
            
            if escolhamenu==1:
                while jogo9==True:
                    escolhaValida=False
                    print("Hora de cadastrar alguns lutadores brabíssimos!!\n")
                    
                    while escolhaValida==False:
                        nomevalido = True
                        nomelutador = input("Digite o nome do lutador a ser cadastrado: ")
                        for i in range (0,len(lutadorescadastrados)):
                            if nomelutador==lutadorescadastrados[i].nome:
                                print("Lutador com este nome já existe. Escolha outro nome!\n")
                                nomevalido = False
                        if nomevalido==True:
                            escolhaValida=True
                    escolhaValida=False
                    clear()
                    
                    print("Temos torneios de: \n")
                    print("1 - JUDÔ\n")
                    print("2 - KARATÊ\n")
                    print("3 - JIU-JITSU\n")
                    while escolhaValida==False:
                        try:
                            escolhamenu = int(input("Digite o identificador numérico da opção que o seu lutador deve ter proeficiência: "))
                            if 0<escolhamenu<=3:
                                escolhaValida=True
                            else:
                                print("Entre com um valor numérico, correspondente ao que deseja acessar no menu, sendo este 1, 2 ou 3!!")
                        except:
                            print("Entre com um valor numérico, correspondente ao que deseja acessar no menu, sendo este 1, 2 ou 3!!")
                    escolhaValida=False
                    if escolhamenu==1:
                        lutalutador = lutas[0]
                    elif escolhamenu==2:
                        lutalutador = lutas[1]
                    else:
                        lutalutador = lutas[2]
                    clear()

                    while escolhaValida==False:
                        try:
                            idade = int(input("Digite a idade do lutador: "))
                            if 18<=idade<=50:
                                escolhaValida=True
                            else:
                                print("Entre com um valor numérico que esteja entre 18 e 50!!")
                        except:
                            print("Entre com um valor numérico que esteja entre 18 e 50!!")  
                    escolhaValida = False
                    clear()
                    while escolhaValida==False:
                        try:
                            peso = int(input("Digite o peso do lutador: "))
                            if 50<=peso<=150:
                                escolhaValida=True
                            else:
                                print("Entre com um valor numérico que esteja entre 50 e 150!!")
                        except:
                            print("Entre com um valor numérico que esteja entre 50 e 150!!") 
                    clear()
                    escolhaValida = False
                    while escolhaValida==False:
                        try:
                            força = int(input("Digite a força do lutador: "))
                            if 0<=força<=100:
                                escolhaValida=True
                            else:
                                print("Entre com um valor numérico que esteja entre 0 e 100!!")
                        except:
                            print("Entre com um valor numérico que esteja entre 0 e 100!!") 
                    clear()
                    escolhaValida = False
                    while escolhaValida==False:
                        faixalutador = input("Digite a faixa do lutador: ")
                        if faixalutador.lower() not in faixas or faixalutador.lower()=="livre":
                            print("Entre com uma faixa válida! Ela pode ser: ")
                            print("branca, cinza, amarela, laranja, verde, roxa, azul, marrom, vermelha, preta\n")
                        else:
                            escolhaValida=True
                    escolhaValida=False
                    clear()
                    while escolhaValida==False:
                        try:
                            odio = int(input("Digite o nível de ódio/motivação do lutador: "))
                            if 0<=odio<=100:
                                escolhaValida=True
                            else:
                                print("Entre com um valor numérico que esteja entre 0 e 100!!")
                        except:
                            print("Entre com um valor numérico que esteja entre 0 e 100!!") 
                    clear()
                    escolhaValida = False
                    lutadorescadastrados.append(Lutador(nomelutador,idade,peso,força,faixalutador,lutalutador,odio))
                    print("{a} criado com sucesso!!".format(a=nomelutador))
                    clear()
                    while escolhaValida==False:
                        print("Deseja criar mais lutadores ou deseja voltar ao menu de lutador?\n")
                        maislutadores = input("Digite s para criar mais lutadores ou digite n para voltar ao menu de lutador: ")
                        if maislutadores.lower() != "s" and maislutadores.lower() != "sim" and maislutadores.lower() != "n" and maislutadores.lower() != "nao":
                            print("Digite apenas a letra 's' ou a letra 'n'!!!\n")
                        else:
                            escolhaValida = True
                    if maislutadores.lower()!="s" and maislutadores.lower()!="sim":
                        jogo9 = False
                    escolhaValida = False
                    clear()
                                     
         
            elif escolhamenu==2:
                print("Aqui estão listados todos os lutadores já cadastrados:\n")
                for i in range (0,len(lutadorescadastrados)):
                    print("{a}\n".format(a=lutadorescadastrados[i].nome))
                time.sleep(3)
                    

            elif escolhamenu==3:
                while jogo10==True:
                    escolhaValida=False
                    print("Lutadores cadastrados:\n")
                    while escolhaValida==False:
                            for i in range(0,len(lutadorescadastrados)):
                                print("{a}\n".format(a=lutadorescadastrados[i].nome))
                            lutador = input("Digite o nome exato de algum dos lutadores acima listados: ")
                            for i in range(0,len(lutadorescadastrados)):
                                if lutador == lutadorescadastrados[i].nome :
                                    indexlutador = i
                                    escolhaValida = True
                    clear()
                    print("Lutador: {a}".format(a=lutadorescadastrados[indexlutador].nome))
                    print("Idade: {a}".format(a=lutadorescadastrados[indexlutador].idade))
                    print("Peso: {a}".format(a=lutadorescadastrados[indexlutador].peso))
                    print("Arte Marcial: {a}".format(a=lutadorescadastrados[indexlutador].artemarcial))
                    print("Força: {a}".format(a=lutadorescadastrados[indexlutador].força))
                    print("Faixa: {a}".format(a=lutadorescadastrados[indexlutador].faixa))
                    print("Ódio: {a}".format(a=lutadorescadastrados[indexlutador].odio))
                    print("Vitórias: {a}".format(a=lutadorescadastrados[indexlutador].vitorias))
                    print("Derrotas: {a}".format(a=lutadorescadastrados[indexlutador].derrotas))
                    escolhaValida=False
                    while escolhaValida==False:
                        print("Deseja ver mais detalhes de lutadores ou deseja voltar ao menu de lutador?\n")
                        maislutadores = input("Digite s para ver mais lutadores ou digite n para voltar ao menu de lutador: ")
                        if maislutadores.lower() != "s" and maislutadores.lower() != "sim" and maislutadores.lower() != "n" and maislutadores.lower() != "nao":
                            print("Digite apenas a letra 's' ou a letra 'n'!!!\n")
                        else:
                            escolhaValida = True
                    escolhaValida = False
                    if maislutadores.lower()!="s" and maislutadores.lower()!="sim":
                        jogo10 = False 
                    clear()

            elif escolhamenu==4:
                jogo8 = False


    #criar torneio aleatorio
    elif escolhamenu == 3:
        while jogo11==True:
            nomeinvalido = True
            print("########## CRIAR TORNEIO ALEATORIO ##########")
            escolhaValida=False
            while escolhaValida==False:
                try:
                    quantidadelutadores = int(input("Digite quantos lutadores voce quer em seu torneio aleatorio: "))
                    escolhaValida=True
                    if quantidadelutadores>100 or quantidadelutadores<1:
                        print("Entre com um valor numérico de 1 a 100!")
                except:
                    print("Entre com um valor numérico de 1 a 100!")
            pesomaximotorneiorandom = r.randint(60,150)
            nometorneio = "Torneio"+str(r.randint(0,100))
            while nomeinvalido==True:
                    for i in range (0,len(torneios)):
                        if nometorneio == torneios[i].name:
                            nometorneio = "Torneio"+str(r.randint(0,10000))
                            break
                    nomeinvalido=False
            nomeinvalido = True    
            quantidadeanterior = len(lutadorescadastrados)
            torneios.append(Torneio(nometorneio,lutas[r.randint(0,2)],pesomaximotorneiorandom,r.randint(r.randint(pesomaximotorneiorandom-10,pesomaximotorneiorandom),pesomaximotorneiorandom),faixas[r.randint(0,9)]))
            for i in range(0,quantidadelutadores):
                pesoaleatorio = r.randint(50,150)
                idadealeatoria = r.randint(18,50)
                lutaaleatoria = lutas[r.randint(0,2)]
                faixaaleatoria = faixas[r.randint(0,9)]
                forçaaleatoria = r.randint(0,100)
                odioaleatorio = r.randint(0,100)
                nomenaotaoaleatorio = "fulano"+str(i)
                
                while nomeinvalido==True:
                    for i in range (0,len(lutadorescadastrados)):
                        if nomenaotaoaleatorio == lutadorescadastrados[i].name:
                            nomenaotaoaleatorio = "cicrano"+str(r.randint(0,1000))
                            break
                    nomeinvalido=False                   
                lutadorescadastrados.append(Lutador(nomenaotaoaleatorio,idadealeatoria,pesoaleatorio,forçaaleatoria,faixaaleatoria,lutaaleatoria,odioaleatorio))
            for i in range (quantidadeanterior,len(lutadorescadastrados)):
                
                if lutadorescadastrados[i].faixa==torneios[-1].faixas[0] and torneios[-1].pesominimo<=lutadorescadastrados[i].peso<=torneios[-1].pesomaximo and lutadorescadastrados[i].artemarcial==torneios[-1].lutatorneio:
                    torneios[-1].inscreverLutador(lutadorescadastrados[i])
            print("Computando novos lutadores ")
            time.sleep(0.5)
            print(".")
            time.sleep(0.5)
            print(".")
            time.sleep(0.5)
            print(".\n\n")
            time.sleep(0.2)
            
            print("Novos lutadores inscritos com sucesso!!") 
            time.sleep(1)
            clear()               

            escolhaValida=False
            while escolhaValida==False:
                print("Deseja criar mais torneios aleatórios ou voltar ao menu principal?\n")
                maislutadores = input("Digite s para tentar criar torneio aleatorio novamente ou digite n para voltar ao menu principal: ")
                if maislutadores.lower() != "s" and maislutadores.lower() != "sim" and maislutadores.lower() != "n" and maislutadores.lower() != "nao":
                    print("Digite apenas a letra 's' ou a letra 'n'!!!\n")
                else:
                    escolhaValida = True
            escolhaValida=False
            if maislutadores.lower()!="s" and maislutadores.lower()!="sim":
                jogo11 = False 
            clear()


    else:
        print("Até a próxima!")
        time.sleep(2)
        clear()
        jogo = False

    jogo1=True
    jogo2=True
    jogo3=True
    jogo4=True
    jogo5=True
    jogo6=True
    jogo7=True
    jogo8=True
    jogo9=True
    jogo10=True
    jogo11=True






         

        

