import pygame
from jogador import Jogador


pygame.init()
clock =pygame.time.Clock()
#TELA
tela=pygame.display.set_mode((800, 500))




#NOME DO JOGO
pygame.display.set_caption('angola plus')

#FUNDO DO JOGO
FUNDO= pygame.image.load("imagens/estrada.png")
FUNDO = pygame.transform.scale(FUNDO,(800,500))

#CARREGAMENTO DO JOGO
carregamento = True


while carregamento:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            carregamento = False

    

    tela.fill((3,5,0))
    tela.blit(FUNDO,(0,0))