# Recriacao do jogo classico Pong utilizando Python e a biblioteca pygame
# Autor: Claudio Kamoda
# Data: 07/08/2019
# Funcoes basicas


# funcao para determinar o movimento da bola
def movimento(b, j1, j2):
    # checa colisao com a margem da tela
    if b.coord[1] <= 0 or b.coord[1] >= 290:
        b.move[1] *= -1                         # inverte a direcao y da bola

    # checa se houve colisao bola-barra
    if (b.coord[0] - j1.x <= j1.larg and j1.y + j1.alt > b.coord[1] > j1.y - b.tam) \
            or (j2.x - b.coord[0] <= b.tam and j2.y + j2.alt > b.coord[1] > j2.y - b.tam):
        b.move[0] *= -1                         # inverte a direcao x da bola

    b.coord[0] += b.move[0]
    b.coord[1] += b.move[1]

    return


# verifica se a bola saiu da tela pelas laterais
def pontuacao(b, j1, j2):
    if b.coord[0] < -20:
        j2.pontos += 1
        return 1
    if b.coord[0] > 500:
        j1.pontos += 1
        return 1

    return 0
