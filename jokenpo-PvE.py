pedra = 1
papel = 2
tesoura = 3
escolhaP1 = int(input("Jogador [1] Digite\n------------------\n(1) para Pedra\n(2) para Papel\n(3) para Tesoura\n------------------\n:"))
escolhaP2 = int(input("Jogador [2] Digite\n------------------\n(1) para Pedra\n(2) para Papel\n(3) para Tesoura\n------------------\n:"))
if escolhaP1 == escolhaP2:
    print("Empate!")
elif escolhaP1 ==1 and escolhaP2 ==2:
    print("Jogador 2 Ganhou!")
elif escolhaP1 ==1 and escolhaP2 ==3:
    print("Jogador 1 Ganhou!")
elif escolhaP1 ==2 and escolhaP2 ==1:
    print("Jogador 1 Ganhou!")
elif escolhaP1 ==2 and escolhaP2 ==3:
    print("Jogador 2 Ganhou!")
elif escolhaP1 ==3 and escolhaP2 ==1:
    print("Jogador 1 Ganhou!")
elif escolhaP1 ==3 and escolhaP2 ==2:
    print("Jogador 2 Ganhou!")

e = input("Digite (S) para Jogar Novamente ou (N) para Acabar o Jogo: ")
while e == "S" or e == "s":
    pedra = 1
    papel = 2
    tesoura = 3
    escolhaP1 = int(input(
        "Jogador [1] Digite\n------------------\n(1) para Pedra\n(2) para Papel\n(3) para Tesoura\n------------------\n:"))
    escolhaP2 = int(input(
        "Jogador [2] Digite\n------------------\n(1) para Pedra\n(2) para Papel\n(3) para Tesoura\n------------------\n:"))
    if escolhaP1 == escolhaP2:
        print("Empate!")
    elif escolhaP1 == 1 and escolhaP2 == 2:
        print("Jogador 2 Ganhou!")
    elif escolhaP1 == 1 and escolhaP2 == 3:
        print("Jogador 1 Ganhou!")
    elif escolhaP1 == 2 and escolhaP2 == 1:
        print("Jogador 1 Ganhou!")
    elif escolhaP1 == 2 and escolhaP2 == 3:
        print("Jogador 2 Ganhou!")
    elif escolhaP1 == 3 and escolhaP2 == 1:
        print("Jogador 1 Ganhou!")
    elif escolhaP1 == 3 and escolhaP2 == 2:
        print("Jogador 2 Ganhou!")

    e = input("Digite (S) para Jogar Novamente ou (N) para Acabar o Jogo: ")
else:
    print("Fim do Jogo!")
