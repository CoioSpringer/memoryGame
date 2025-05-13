import random
def jogodamemoria():

    jogador1 = str(input("Nome do Jogador 1: "))
    jogador2 = str(input("Nome do Jogador 2: "))

    turno_1 = True

    count_pontos_jogador_1 = count_pontos_jogador_2 = 0

    tabuleiro = [[0, 0, 1], [1, 2 ,2], [3, 3, 4], [4, 5, 5]]
    tabuleiro_emborcado = [['*', '*', '*'], ['*', '*' ,'*'], ['*', '*', '*'], ['*', '*', '*']]
    random.shuffle(tabuleiro)
    print()
    #jogador1
    while turno_1 == True:
        if tabuleiro_emborcado == tabuleiro:
            print("Fim de Jogo!")
            break
        print("Este é o estado atual do tabuleiro: ")
        print()
        for linha in tabuleiro_emborcado:
            print(linha)
        print()
        print(f"Vez de {jogador1}")
        print()
        while True:
            escolha_casa_x = int(input("Escolha a linha em que quer selecionar a peça: "))
            escolha_casa_y = int(input("Escolha a coluna em que quer selecionar a peça: "))
            if tabuleiro_emborcado[escolha_casa_x][escolha_casa_y] != '*':
                print("Jogada inválida, tente novamente.")
            else:
                break
        retorno = tabuleiro_emborcado[escolha_casa_x][escolha_casa_y]
        tabuleiro_emborcado[escolha_casa_x][escolha_casa_y] = tabuleiro[escolha_casa_x][escolha_casa_y]
        primeira_escolha = tabuleiro[escolha_casa_x][escolha_casa_y]
        if retorno != '*':
            print("Jogada inválida, tente novamente: ")
            escolha_casa_x = int(input("Escolha a linha em que quer selecionar a peça: "))
            escolha_casa_y = int(input("Escolha a coluna em que quer selecionar a peça: "))
            retorno = tabuleiro_emborcado[escolha_casa_x][escolha_casa_y]
            tabuleiro_emborcado[escolha_casa_x][escolha_casa_y] = tabuleiro[escolha_casa_x][escolha_casa_y]
            primeira_escolha = tabuleiro[escolha_casa_x][escolha_casa_y]
        else:
            print()
            for linha in tabuleiro_emborcado:
                print(linha)
            print()
            print(f"Primeira peça escolhida: {primeira_escolha}")

        while True:
            escolha_casa_i = int(input("Escolha a linha em que quer selecionar a peça: "))
            escolha_casa_j = int(input("Escolha a coluna em que quer selecionar a peça: "))
            if tabuleiro_emborcado[escolha_casa_i][escolha_casa_j] != '*':
                print("Jogada inválida, tente novamente.")
            else:
                break
        retorno_segunda = tabuleiro_emborcado[escolha_casa_i][escolha_casa_j]
        tabuleiro_emborcado[escolha_casa_i][escolha_casa_j] = tabuleiro[escolha_casa_i][escolha_casa_j]
        segunda_escolha = tabuleiro[escolha_casa_i][escolha_casa_j]
        if retorno_segunda != '*':
            print("Jogada inválida, tente novamente: ")
            escolha_casa_i = int(input("Escolha a linha em que quer selecionar a peça: "))
            escolha_casa_j = int(input("Escolha a coluna em que quer selecionar a peça: "))
            retorno = tabuleiro_emborcado[escolha_casa_i][escolha_casa_j]
            tabuleiro_emborcado[escolha_casa_i][escolha_casa_j] = tabuleiro[escolha_casa_i][escolha_casa_j]
            segunda_escolha = tabuleiro[escolha_casa_i][escolha_casa_j]
        else:
            for linha in tabuleiro_emborcado:
                print(linha)
        print(f"Segunda peça escolhida {segunda_escolha}")

        if primeira_escolha == segunda_escolha:
            print()
            print(f"{jogador1} achou um par, jogue novamente!")
            count_pontos_jogador_1 += 1
        else:
            print()
            print(f"{jogador1} errou")
            tabuleiro_emborcado[escolha_casa_x][escolha_casa_y] = retorno
            tabuleiro_emborcado[escolha_casa_i][escolha_casa_j] = retorno_segunda
            turno_1 = False


            #jogador2
            while turno_1 == False:
                if tabuleiro_emborcado == tabuleiro:
                    print("Fim de Jogo!")
                    break
                print("Este é o estado atual do tabuleiro: ")
                for linha in tabuleiro_emborcado:
                    print(linha)
                print(f"Vez de {jogador2}")
                while True:
                    escolha_casa_x = int(input("Escolha a linha em que quer selecionar a peça: "))
                    escolha_casa_y = int(input("Escolha a coluna em que quer selecionar a peça: "))
                    if tabuleiro_emborcado[escolha_casa_x][escolha_casa_y] != '*':
                        print("Jogada inválida, tente novamente.")
                    else:
                        break
                retorno = tabuleiro_emborcado[escolha_casa_x][escolha_casa_y]
                tabuleiro_emborcado[escolha_casa_x][escolha_casa_y] = tabuleiro[escolha_casa_x][escolha_casa_y]
                primeira_escolha = tabuleiro[escolha_casa_x][escolha_casa_y]
                if retorno != '*':
                    print("Jogada inválida, tente novamente: ")
                    escolha_casa_x = int(input("Escolha a linha em que quer selecionar a peça: "))
                    escolha_casa_y = int(input("Escolha a coluna em que quer selecionar a peça: "))
                    retorno = tabuleiro_emborcado[escolha_casa_x][escolha_casa_y]
                    tabuleiro_emborcado[escolha_casa_x][escolha_casa_y] = tabuleiro[escolha_casa_x][escolha_casa_y]
                    primeira_escolha = tabuleiro[escolha_casa_x][escolha_casa_y]
                else:
                    for linha in tabuleiro_emborcado:
                        print(linha)
                    print(f"Primeira peça escolhida: {primeira_escolha}")

                while True:
                    escolha_casa_i = int(input("Escolha a linha em que quer selecionar a peça: "))
                    escolha_casa_j = int(input("Escolha a coluna em que quer selecionar a peça: "))
                    if tabuleiro_emborcado[escolha_casa_i][escolha_casa_j] != '*':
                        print("Jogada inválida, tente novamente.")
                    else:
                        break
                retorno_segunda = tabuleiro_emborcado[escolha_casa_i][escolha_casa_j]
                tabuleiro_emborcado[escolha_casa_i][escolha_casa_j] = tabuleiro[escolha_casa_i][escolha_casa_j]
                segunda_escolha = tabuleiro[escolha_casa_i][escolha_casa_j]
                if retorno_segunda != '*':
                    print("Jogada inválida, tente novamente: ")
                    escolha_casa_i = int(input("Escolha a linha em que quer selecionar a peça: "))
                    escolha_casa_j = int(input("Escolha a coluna em que quer selecionar a peça: "))
                    retorno = tabuleiro_emborcado[escolha_casa_i][escolha_casa_j]
                    tabuleiro_emborcado[escolha_casa_i][escolha_casa_j] = tabuleiro[escolha_casa_i][escolha_casa_j]
                    segunda_escolha = tabuleiro[escolha_casa_i][escolha_casa_j]
                else:
                    for linha in tabuleiro_emborcado:
                        print(linha)
                print(f"Segunda peça escolhida {segunda_escolha}")


                if primeira_escolha == segunda_escolha:
                    print(f"{jogador2} achou um par, jogue novamente!")
                    count_pontos_jogador_2 += 1
                else:
                    print(f"{jogador2} errou")
                    tabuleiro_emborcado[escolha_casa_x][escolha_casa_y] = retorno
                    tabuleiro_emborcado[escolha_casa_i][escolha_casa_j] = retorno_segunda
                    turno_1 = True

    print(f"Total de pontos de {jogador1}: {count_pontos_jogador_1}")
    print(f"Total de pontos de {jogador2}: {count_pontos_jogador_2}")

    if count_pontos_jogador_1 > count_pontos_jogador_2:
        print(f"{jogador1} Venceu! ^-^")
    elif count_pontos_jogador_2 > count_pontos_jogador_1:
        print(f"{jogador2} Venceu! ^-^")
    else:
        print("Empate! e.e")

jogodamemoria()