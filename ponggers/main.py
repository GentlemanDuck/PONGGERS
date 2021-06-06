import pygame; import sys; from modules import actors

#abrir pygame
pygame.init()

#tela
resu = larg, alt = 800, 600
tela = pygame.display.set_mode(resu)

#nome e icone
pygame.display.set_caption("PONGGERS")
icone = pygame.image.load("data/ponggers_icon.png")
pygame.display.set_icon(icone)

#cores - R / G / B
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#fps
rodando = True
clock = pygame.time.Clock()
FPS = 60

#players
        #player1
playerOne = actors.player('data/player_one.png', 16, 108)
playerOne.rect.x = 35; playerOne.rect.y = 234
p1Sfx = pygame.mixer.Sound('data/p1hit.wav')
p1score = 0

        #player2
playerTwo = actors.player('data/player_two.png', 16, 108)
playerTwo.rect.x = 754; playerTwo.rect.y = 234
p2Sfx = pygame.mixer.Sound('data/p2hit.wav')
p2score = 0
        
        #velocidade dos jogadores
playerSpeed = 5

#bola
bolasfx = pygame.mixer.Sound('data/wallBounce.wav')
bola = actors.ball('data/ball.png', 14, 14, bolasfx)
bola.rect.x = 394; bola.rect.y = 284

#volume base
vol = 50
sounds = [bolasfx, p2Sfx, p1Sfx]

#rodar jogo
rodando = True

while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
        print(event)

    if pygame.sprite.collide_mask(bola, playerOne):
        bola.bounce()
        pygame.mixer.Sound('data/p1hit.wav').play()
    elif pygame.sprite.collide_mask(bola, playerTwo):
        bola.bounce()
        pygame.mixer.Sound('data/p2hit.wav').play()

#fundo
    tela.fill(BLACK)
    pygame.draw.line(tela, WHITE, [400, 0], [400, 600], 6)

#mostrar personagem
    tela.blit(playerOne.image, (playerOne.rect.x, playerOne.rect.y))
    tela.blit(playerTwo.image, (playerTwo.rect.x, playerTwo.rect.y))
    tela.blit(bola.image, (bola.rect.x, bola.rect.y))
    bola.update()

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
    
    
    #atualizar tela
    pygame.display.update()
    clock.tick(FPS)
