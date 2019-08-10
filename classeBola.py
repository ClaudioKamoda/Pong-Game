# Recriacao do jogo classico Pong utilizando Python e a biblioteca pygame
# Autor: Claudio Kamoda
# Data: 07/08/2019
# Classe bola

# importacao  das bibliotecas
import pygame
import random


class bola(object):
    # construtor
    def __init__(self, tam):
        self.tam = tam                              # tamanho
        self.vel = 2                                # velocidade de movimento
        self.coord = [self.bolaX(), self.bolaY()]   # tupla com as coordenadas
        self.move = self.mov_ini()                  # direcao dos movimentos

    def bolaX(self):
        return random.randint(200, 290)             # atribui uma posicao inicial aleatoria em x

    def bolaY(self):
        return random.randint(0, 290)               # atribui uma posicao inicial aleatoria em y

    def mov_ini(self):                      # atribui uma direcao inicial aleatoria
        dir = random.randint(1, 4)

        if dir == 1:
            mov = [self.vel, self.vel]      # direita-baixo (sudeste)
        elif dir == 2:
            mov = [-self.vel, self.vel]     # esquerda-baixo (sudoeste)
        elif dir == 3:
            mov = [self.vel, -self.vel]     # direita-cima (nordeste)
        else:
            mov = [-self.vel, -self.vel]    # esquerda-cima (noroeste)

        return mov

    # funcao para desenha a bola
    def desenha_bola(self, jan):
        pygame.draw.rect(jan, (255, 255, 255), (self.coord[0], self.coord[1], self.tam, self.tam))