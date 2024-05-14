import pygame
from jogador import Jogador


pygame.init()
clock =pygame.time.Clock()
#TELA
tela=pygame.display.set_mode((800, 500))

#JOGADOR
jogador1 = Jogador("tuga.png", 100, 100, 420, 400)






#NOME DO JOGO
pygame.display.set_caption('angola plus')

#FUNDO DO JOGO
FUNDO= pygame.image.load("mar2.jpg")
FUNDO = pygame.transform.scale(FUNDO,(800,500))

#CARREGAMENTO DO JOGO
carregamento = True


while carregamento:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            carregamento = False

    
    
    
    #EXIBIR TELA
    tela.fill((3,5,0))
    tela.blit(FUNDO,(0,0))
   
    #MOBILIDADE DO JOGADOR
    jogador1.movimenta_via_controle( pygame.K_LEFT, pygame.K_RIGHT)
    jogador1.apareca(tela)



    pygame.display.update()


    #ajustando FPS
    clock.tick(70)