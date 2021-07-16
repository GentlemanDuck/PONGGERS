import pygame; from pygame.locals import *; import sys; from modules import actors; from time import sleep; from random import randint

#abrir pygame
pygame.init()

#tela
resu = larg, alt = 800, 600
tela = pygame.display.set_mode(resu)


def load_all():

        #fundo
        tela.fill(BLACK)
        pygame.draw.line(tela, WHITE, [400, 0], [400, 600], 6)

        #pontuação
        text = fonte.render(str(p1score), 1, WHITE)
        tela.blit(text, (300,10))
        text = fonte.render(str(p2score), 1, WHITE)
        tela.blit(text, (475,10))

        #mostrar personagem
        tela.blit(playerOne.image, (playerOne.rect.x, playerOne.rect.y))
        tela.blit(playerTwo.image, (playerTwo.rect.x, playerTwo.rect.y))
        tela.blit(bola.image, (bola.rect.x, bola.rect.y))
        bola.update(playerOne, playerTwo)


def reset_all():
        p2score = 0
        playerTwo.rect.x = 754; playerTwo.rect.y = 234
        p1score = 0
        playerOne.rect.x = 35; playerOne.rect.y = 234
        bola.rect.x = 394; bola.rect.y = 284
        bola.vel = [randint(-3, 3), randint(-3, 3)]
        while bola.vel == 0:
            bola.vel = [randint(-3, 3), randint(-3, 3)]

#nome e icone
pygame.display.set_caption("PONGGERS")
icone = pygame.image.load("data/ponggers_icon.png")
pygame.display.set_icon(icone)

#cores - R / G / B
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (169, 169, 169)

#fonte
fonte = pygame.font.Font('data/comic.ttf', 40)

#fps
clock = pygame.time.Clock()
FPS = 60

#players
        #player1
p1score = 0 
playerOne = actors.player('data/player_one.png', 16, 108, fonte)
playerOne.rect.x = 35; playerOne.rect.y = 234
p1Sfx = pygame.mixer.Sound('data/p1hit.wav')

        #player2
playerTwo = actors.player('data/player_two.png', 16, 108, fonte)
playerTwo.rect.x = 754; playerTwo.rect.y = 234
p2Sfx = pygame.mixer.Sound('data/p2hit.wav')
p2score = 0

        #velocidade dos jogadores
playerSpeed = 5

#bola
bolasfx = pygame.mixer.Sound('data/wallBounce.wav')
bola = actors.ball('data/ball.png', 14, 14, bolasfx)
bola.rect.x = 394; bola.rect.y = 284

#rodar jogo
gameRun = True
rodando = False
inMenu = True
leftclick = False

#TILE
titleFont = pygame.font.Font('data/comic.ttf', 60)

#PLAY
playButt = fonte.render('Jogar', 1, BLACK)
playSquare = pygame.Rect(310, 260, 170, 65)
pScolor = WHITE

#QUIT
quitButt = fonte.render('Sair', 1, BLACK)
quitSquare = pygame.Rect(310, 350, 170, 65)
qScolor = WHITE

#***** * WINS!
winSquare = pygame.Rect(130, 240, 540, 110)
p1win = titleFont.render('PLAYER 1 VENCE', 1, WHITE)
p2win = titleFont.render('PLAYER 2 VENCE', 1, WHITE)

while gameRun:
    while inMenu:   
        tela.fill(BLACK)
        
        #PONGGERS
        title = titleFont.render('PONGGERS', 1, WHITE)
        tela.blit(title, (235, 130))
        
        #PLAY
        pygame.draw.rect(tela, pScolor, playSquare)
        tela.blit(playButt, (340, 260))

        #QUIT
        pygame.draw.rect(tela, qScolor, quitSquare)
        tela.blit(quitButt, (350, 350))

        #play click
        if playSquare.collidepoint(pygame.mouse.get_pos()):
            pScolor = GREY
            if leftclick:
                inMenu = False
                rodando = True
                p2score = 0
                p1score = 0
                while bola.vel == 0:
                    bola.vel = [randint(-3, 3), randint(-3, 3)]
                load_all()
        else:
            pScolor = WHITE

        #quit click
        if quitSquare.collidepoint(pygame.mouse.get_pos()):
            qScolor = GREY
            if leftclick:
                inMenu = False
                gameRun = False
        else:
            qScolor = WHITE
       
        #Sc Update
        pygame.display.update() 

        leftclick = False
        #event update
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False
                inMenu = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    leftclick = True
            #print(event)        

#jogo msm
    while rodando:

#detectar colisão
        if pygame.sprite.collide_mask(bola, playerOne):
            bola.bounce()
            pygame.mixer.Sound('data/p1hit.wav').play()
        elif pygame.sprite.collide_mask(bola, playerTwo):
            bola.bounce()
            pygame.mixer.Sound('data/p2hit.wav').play()
          
                #não deixa a bola sair do mapa
        if bola.rect.x>=786:
            bola.vel[0] = -bola.vel[0]
            bola.sfx.play()
            p1score += 1
        if bola.rect.x<=0:
            bola.vel[0] = -bola.vel[0]
            bola.sfx.play()
            p2score += 1
        if bola.rect.y>586:
            bola.vel[1] = -bola.vel[1]
            bola.sfx.play()
        if bola.rect.y<0:
            bola.vel[1] = -bola.vel[1]
            bola.sfx.play()

        load_all()

        #controles    
        ctrl = pygame.key.get_pressed()
        if ctrl[pygame.K_UP]:
            playerTwo.moveUp(playerSpeed)
        elif ctrl[pygame.K_DOWN]:
            playerTwo.moveDown(playerSpeed)
        if ctrl[pygame.K_w]:
            playerOne.moveUp(playerSpeed)
        elif ctrl[pygame.K_s]:
            playerOne.moveDown(playerSpeed)
        if ctrl[pygame.K_ESCAPE]:
            inMenu = True
            rodando = False

        #checar evento
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False
                gameRun = False
            #print(event)

        #acabar partida
        if p1score > 4:
            reset_all()
            load_all()
            pygame.draw.rect(tela, GREY, winSquare)
            tela.blit(p1win, (160, 240))
            tela.blit(pygame.font.Font('data/comic.ttf', 20).render('aperte ESC para voltar ao menu', 1, WHITE), (160, 310))
            pygame.display.update()

        if p2score > 4:
            reset_all()
            load_all()
            pygame.draw.rect(tela, GREY, winSquare)
            tela.blit(p2win, (160, 240))
            tela.blit(pygame.font.Font('data/comic.ttf', 20).render('aperte ESC para voltar ao menu', 1, WHITE), (160, 310))
            pygame.display.update()

        #atualizar tela
        pygame.display.update()
        clock.tick(FPS)

pygame.quit()
sys.exit()
