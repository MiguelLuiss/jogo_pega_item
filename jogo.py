import pygame
from jogador import Jogador
from obstaculo_e_comida import Obstaculo

pygame.init()
clock =pygame.time.Clock()
#TELA
tela=pygame.display.set_mode((800, 500))

#JOGADOR
jogador1 = Jogador("tuga.png", 100, 100, 420, 400)


#MUSICA DO JOGO

som_fundo = pygame.mixer.Sound("som/musicafundo.mp3")
         
 #musica de fundo
pygame.mixer.music.load("som/musicafundo.mp3")


# Defina a repetição do som de fundo
pygame.mixer.music.set_endevent(pygame.USEREVENT)

# Inicie a reprodução do som de fundo
pygame.mixer.music.play()


lista_comida_boa = [Obstaculo("maca.png", 50,50,700,47),
                Obstaculo("cereja.png", 50,50,700,118),
                Obstaculo("pera.png", 50,50,700,188),
                Obstaculo("roma.png", 50,50,700,330),]
                

lista_comida_ruim =[Obstaculo("canudo.png", 50,50,700,0),
                   Obstaculo("lampada.png", 50,50,700,0)]

#NOME DO JOGO
pygame.display.set_caption('plus')

#FUNDO DO JOGO
FUNDO= pygame.image.load("mar2.jpg")
FUNDO = pygame.transform.scale(FUNDO,(800,500))

#CARREGAMENTO DO JOGO
carregamento = True


while carregamento:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            carregamento = False



    #texto
    fonte =pygame.font.SysFont("Arial black", 14,True)
    
    
    #PONTUAÇÃO JOGADOR
    pontuacao_jogador =0
    
    
    #EXIBIR TELA
    tela.fill((3,5,0))
    tela.blit(FUNDO,(0,0))
   
    #MOBILIDADE DO JOGADOR
    jogador1.movimenta_via_controle( pygame.K_LEFT, pygame.K_RIGHT)
    jogador1.apareca(tela)

    
    for comida_ruim in lista_comida_ruim:
        comida_ruim.movimenta()
        comida_ruim.apareca(tela)



    #COLISÃO COM OBJETOS NEGATIVOS
        if jogador1.mascara.overlap(comida_ruim.mascara, (comida_ruim.pos_x - jogador1.jogador_pos_x,  comida_ruim. pos_y- jogador1.jogador_pos_y)):
            carregamento = False


            
        #GANHAR PONTO
          #MOBILIDADE OBSTACULOS E "PONTOS"
    for comida in lista_comida_boa:
        comida.movimenta()
        comida.apareca(tela)

        if jogador1.mascara.overlap(comida.mascara, (comida.pos_x - jogador1.jogador_pos_x,  comida. pos_y- jogador1.jogador_pos_y)):
            pontuacao_jogador = pontuacao_jogador +1
     
    texto_ponto = fonte.render(f"Pontuação do jogador {pontuacao_jogador+1} ", True,(255,200,0))
    tela.blit(texto_ponto,(10,10))
  
    
       

    #SUMIR COMIDA AO ENCOSTAR NO JOGADOR




    

    
    
    
    #ESPECIAL DO JOGO







    
    #Atualiza
    pygame.display.update()


    #ajustando FPS
    clock.tick(50)


