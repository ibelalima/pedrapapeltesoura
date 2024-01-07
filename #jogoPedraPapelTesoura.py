import random
import os
#jogoPedraPapelTesoura
jogar_novamente= True
while jogar_novamente:
    escolha = int(input("Escolhas: 1- para jogar contra outro jogador, ou 2 para jogar contra a maquina"))

    if escolha == 1:
        nome_jogadorA = input('digite seu nome ')
        nome_jogadorB = input('digite seu nome ')
        os.system('cls')
        print("\n",nome_jogadorA,"\n")
        jogadorA= int(input("Escolha: \n 1- Pedra \n 2-Papel \n 3-Tesoura \n"))
        os.system('cls')
        print("\n",nome_jogadorB,"\n")
        jogadorB=  int(input("Escolha: \n 1- Pedra \n 2-Papel \n 3-Tesoura "))
        os.system('cls')

        if jogadorA == jogadorB:
            print ('empate')
        elif jogadorA == 1 and jogadorB ==3 or jogadorA == 2 and jogadorB == 1 or jogadorA == 3 and jogadorB==2:
            print(nome_jogadorA, "venceu!")
        else:
            print( nome_jogadorB,"venceu!")
    elif escolha == 2:
        jogadorA = input('digite seu nome ')
        os.system('cls')
        print(jogadorA)
        jogadorA= int(input("Escolha: \n 1- Pedra \n 2-Papel \n 3-Tesoura "))
        jogadorB= random.randint(1,3)
        if jogadorB == 1:
            print('A máquina escolheu pedra!')
        elif jogadorB == 2:
            print('A máquina escolheu papel!')
        else:
            print('A máquina escolheu tesoura')
        if jogadorA == jogadorB:
            print ('empate')
        elif jogadorA == 1 and jogadorB ==3 or jogadorA == 2 and jogadorB == 1 or jogadorA == 3 and jogadorB==2:
            print("Você venceu!")
        else:
            print("A maquina venceu!")
    teste = input("você quer jogar novamente ? Sim ou Não")

    if teste == "Não" or teste =="Nao" or teste =="n" or teste =="nao" or teste =="não":
        jogar_novamente = False
        print("Fim de jogo")
