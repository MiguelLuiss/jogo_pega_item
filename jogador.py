import pygame
class Jogador:
    def __init__(self,arquivo_imagem, altura_imagem, largura_imagem, x_inicial, y_inicial):
        self.imagem = pygame.image.load(arquivo_imagem)
        
        self.altura = altura_imagem
        self.largura = largura_imagem
        
        self.imagem =pygame.transform.scale(self.imagem,(self.largura, self.altura))
        
        self.jogador_pos_x = x_inicial
        self.jogador_pos_y = y_inicial
    
        self.mascara = pygame.mask.from_surface(self.imagem)
        
    
    def apareca(self, tela):
        tela.blit(self.imagem,(self.jogador_pos_x, self.jogador_pos_y))

    def movimenta_via_controle(self, esquerda, direita):
            teclas = pygame.key.get_pressed()

            
            if teclas[esquerda]:
                if self.jogador_pos_x>0:
                    self.jogador_pos_x = self.jogador_pos_x -5
            
            if teclas[direita]:
                if self.jogador_pos_x<710:
                    self.jogador_pos_x = self.jogador_pos_x +5
