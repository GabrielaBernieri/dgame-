import pygame
import random
from pygame import *
import sys


class dinossauro(object):
    AZUL = (0, 0, 255)

    def __init__(self, pos_x, pos_y):
        self.pos_x = 66
        self.pos_y = 107
        self.pulo = False
        self.puloconta = 14

    def draw(self, fundo):
        self.rect = pygame.draw.rect(fundo, dinossauro.AZUL, [self.pos_x, self.pos_y, 20, -20])

    def pular(self):
        if self.pulo:
            if self.puloconta >= -14:
                neg = -1 if self.puloconta < 0 else 1
                self.pos_y -= (self.puloconta ** 2) * 0.1 * neg
                self.puloconta -= 1
            else:
                self.pulo = False
                self.puloconta = 14

    def colidiu(self, rect):
        return self.rect.colliderect(rect)


class cactu(object):
    CARMESIM = (220, 20, 60)

    def __init__(self, pos_c, pos_z, altura):
        self.pos_c = pos_c
        self.pos_z = pos_z
        self.altura = altura

    def draw(self, screen):
        self.rect = pygame.draw.rect(screen, cactu.CARMESIM, [self.pos_c, self.pos_z, 20, -self.altura], )
        
    def anda(self, placar):
        if self.pos_c > -20:
            self.pos_c -= 4
        if placar >= 10:
            self.pos_c -= 6
        if placar >= 30:
            self.pos_c -= 8
        if placar >= 80:
            self.pos_c -= 10
    

    def colidiu(self, rect):
        return self.rect.colliderect(rect)


def wait(key):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: return False
            if event.type == pygame.KEYDOWN:
                if event.key == key:
                    return True
                else:
                    return False


def jogo(dino, cact, screen, placar):
    fundo = pygame.Surface((largura, altura))
    fundo.fill(ROSA)
    screen.blit(fundo, (0, 0))
    tempo = pygame.time.Clock()
    
    while True:
        tempo.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: return False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                dino.pulo = True
                placar+=1

        screen.blit(fundo, (0, 0))
        pygame.draw.line(screen, BRANCO, [0, 109], [600, 109], 7)
        dino.pular()
        dino.draw(screen)
        
        if cact.pos_c <= -20: cact = cactu(600, 107, random.randrange(10, 30))
        
        cact.draw(screen)
        cact.anda(placar)

        pygame.display.update()

        if dino.colidiu(cact.rect):
            print('colidiu.....')
            return True


def main():
    preto = (0, 0, 0)
    fonte_jn = pygame.font.SysFont(pygame.font.get_default_font(), 25)
    fundo = pygame.Surface((largura, altura))
    fundo.fill(ROSA)
    screen.blit(fundo, (0, 0))
    pygame.draw.line(screen, BRANCO, [0, 109], [600, 109], 7)
    dino = dinossauro(66, 107)
    cact = cactu(600, 107, random.randrange(10, 30))
    dino.draw(screen)
    cact.draw(screen)
    pygame.display.update()
    if not wait(pygame.K_SPACE): return

    while jogo(dino, cact, screen, placar):
        fundo.fill(ROSA)
        msg = 'Precione S para jogar novamente'
        msg2 = 'Precione N para sair do jogo'
        texto = fonte_jn.render(msg, True, preto)
        texto2 = fonte_jn.render(msg2, True, preto)
        screen.blit(texto, (200, 30))
        screen.blit(texto2, (200, 55))
        pygame.display.update()
        if not wait(pygame.K_s): return
        dino = dinossauro(66, 107)
        cact = cactu(600, 107, random.randrange(10, 30))


ROSA = (255, 105, 180)
BRANCO = (255, 255, 255)
largura = 600
altura = 150
placar = 0 
screen = pygame.display.set_mode((largura, altura))
pygame.init()
pygame.font.init()
pygame.display.set_caption('block run')

main()
pygame.quit()
sys.exit(0) 




