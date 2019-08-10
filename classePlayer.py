# Recriacao do jogo classico Pong utilizando Python e a biblioteca pygame
# Autor: Claudio Kamoda
# Data: 07/08/2019
# Classe player

import pygame   # importacao da biblioteca


class player(object):
    # construtor
    def __init__(self, x, y, alt, larg):
        self.x = x                          # coordenada x
        self.y = y                          # coordenada y
        self.alt = alt                      # altura
        self.larg = larg                    # largura
        self.vel = 5                        # velocidade de movimentacao
        self.pontos = 0                     # pontos

    # funcao para desenhar a barra
    def desenha_player(self, jan):
        pygame.draw.rect(jan, (255, 255, 255), (self.x, self.y, self.larg, self.alt))
