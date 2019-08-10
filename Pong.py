# Recriacao do jogo classico Pong utilizando Python e a biblioteca pygame
# Autor: Claudio Kamoda
# Data: 07/08/2019
# Arquivo principal

# importacao da biblioteca e modulos
import pygame
import funcoes as f
import classePlayer as cp
import classeBola as cb


pygame.init()   # inicializacao da bibioteca

# altura e largura da janela em pixels
JAN_LARGURA = 500
JAN_ALTURA = 300

# inicializacao da janela
jan = pygame.display.set_mode((JAN_LARGURA, JAN_ALTURA))

pygame.display.set_caption("Pong")              # Legenda superior da tela
fonte = pygame.font.SysFont('zig', 30, True)    # objeto que recebe o a fonte do placar
clock = pygame.time.Clock()                     # clock

# instanciacao dos objetos (ver classes)
jog_Esq = cp.player(20, 135, 30, 10)                    # barra da esquerda
jog_Dir = cp.player(470, 135, 30, 10)                   # barra da direita
bola = cb.bola(10)                                      # bola
meioDeCampo = pygame.image.load('meio de campo.png')    # linha central da tela


# funcao que agrega todas as operacoes de desenho na tela
def desenhaTela():
    jan.fill((0, 0, 0))             # preenche a tela com a cor preta para apagar a iteracao anterior
    jog_Esq.desenha_player(jan)     # desenha a barra da esquerda
    jog_Dir.desenha_player(jan)     # desenha a barra da direita
    bola.desenha_bola(jan)              # desenha a bola
    jan.blit(meioDeCampo, (245, 0))     # desenha a linha central
    placar1 = fonte.render(str(jog_Esq.pontos),1, (255, 255, 255))      # placar da esquerda
    placar2 = fonte.render(str(jog_Dir.pontos),1, (255, 255, 255))      # placar da direita
    jan.blit(placar1, (180, 20))    # desenha o placar da esquerda
    jan.blit(placar2, (290, 20))    # desenha o placar da direita
    pygame.display.update()         # atualiza a tela

    return


# laco principal
run = True
while run:
    clock.tick(30)  # taxa de 30 atualizacoes por segundo
    
    for event in pygame.event.get():        # verifica se o jogador fechou a tela
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()         # le os inputs do teclado

    # comandos do jogador da esquerda
    if keys[pygame.K_w] and jog_Esq.y != 0:
        jog_Esq.y -= jog_Esq.vel
    if keys[pygame.K_s] and jog_Esq.y != (JAN_ALTURA - jog_Esq.alt):
        jog_Esq.y += jog_Esq.vel

    # comandos do jogador da direita
    if keys[pygame.K_UP] and jog_Dir.y != 0:
        jog_Dir.y -= jog_Dir.vel
    if keys[pygame.K_DOWN] and jog_Dir.y != (JAN_ALTURA - jog_Dir.alt):
        jog_Dir.y += jog_Dir.vel

    f.movimento(bola, jog_Esq, jog_Dir)         # verifica o movimento da bola
    if f.pontuacao(bola, jog_Esq, jog_Dir):     # verifica a pontuacao
        bola = cb.bola(10)
    desenhaTela()                               # desenha a tela depois dos inputs

pygame.quit()       # encerra o jogo
