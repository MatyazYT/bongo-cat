__author__ = 'matyy'

import pygame, sys
import simpleaudio as sa
import time
import random
from pygame.locals import *

pygame.init()
pygame.font.init()

listaCircleR = []
listaCircleL = []

displayCat = pygame.display.set_mode((1000, 500), 0, 32)

class circle:
    def __init__(self, ejeX):
        #560
        self.X = ejeX
        self.Y = 0
        self.mostrar = True
        self.hitbox = pygame.Rect(self.X, self.Y, 100, 100)
    def actualizarHitbox(self):
        self.hitbox = pygame.Rect(self.X, self.Y, 100, 100)
    def mostrarHitbox(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), self.hitbox)


# tipo de letra
myfont = pygame.font.Font("fonts/ComicNeue-Regular.ttf", 30)
myfont2 = pygame.font.Font("fonts/ComicNeue-Regular.ttf", 30)

FPS = 60# frames per second setting
fpsClock = pygame.time.Clock()

currentFPS = fpsClock.get_fps()

# set up the window 900x400
#pygame.display.set_caption('Cat Hero - ' + str(currentFPS))

#frames explosion
exp1 = pygame.image.load('exp/frame01.png')
exp2 = pygame.image.load('exp/frame02.png')
exp3 = pygame.image.load('exp/frame03.png')
exp4 = pygame.image.load('exp/frame04.png')
exp5 = pygame.image.load('exp/frame05.png')
exp6 = pygame.image.load('exp/frame06.png')
exp7 = pygame.image.load('exp/frame07.png')
exp8 = pygame.image.load('exp/frame08.png')
exp9 = pygame.image.load('exp/frame09.png')
exp10 = pygame.image.load('exp/frame10.png')
exp11 = pygame.image.load('exp/frame11.png')
exp12 = pygame.image.load('exp/frame12.png')
exp13 = pygame.image.load('exp/frame13.png')
exp14 = pygame.image.load('exp/frame14.png')
exp15 = pygame.image.load('exp/frame15.png')
exp16 = pygame.image.load('exp/frame16.png')

hitcircle = pygame.image.load('hitcircle.png')
hitcircle = pygame.transform.scale(hitcircle, (100, 100))
hitcircle2 = pygame.image.load('hitcircle.png')


hitRight = pygame.Rect(575, 310, 60, 60)
hitLeft = pygame.Rect(430, 300, 60, 60)
hitFailRight = pygame.Rect(560, 450, 100, 100)
hitFailLeft = pygame.Rect(415, 450, 100, 100)
# transparent = pygame.image.load('catimg/white.jpg').convert()

exp = [exp1, exp2, exp3, exp4, exp5, exp6, exp7, exp8, exp9, exp10, exp11, exp12, exp13, exp14, exp15, exp16]

explosion = False

actual = 0

contadorKeys = 0

blitX = 820

blitY = 15

teclasforPress = 100

WHITE = (255, 255, 255)
RED = (255, 0, 0)
ORANGE = (255, 127, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
VIOLET = (139, 0, 255)

coorX = 55
coorY = 200

hitY = 0

puntosDisplay = True

contadorSound = True

audioWin = True

sonarMusica = True

bajandoY1 = 11 # 7
bajandoY2 = 15 # 10


# imagenes de gato
catNothing = pygame.image.load('catimg/catNothing.png').convert()
# 803x300
catNothing = pygame.transform.scale(catNothing, (800, 300))
catLeft = pygame.image.load('catimg/catLeft.png').convert()
# 798x 297
catLeft = pygame.transform.scale(catLeft, (800, 300))
catRight = pygame.image.load('catimg/catRight.png').convert()
# 797x297
catRight = pygame.transform.scale(catRight, (800, 300))
catBoth = pygame.image.load('catimg/catBoth.png').convert()
# 798x298
catBoth = pygame.transform.scale(catBoth, (800, 300))
img_actual = catNothing
contador = 0
bloqueo = False
img_actual = catNothing
randomSpawnR = random.randint(1, 2)*FPS
randomSpawnL = random.randint(2, 4)*FPS
timerR = 0
timerL = 0

def playAudio(audiofile):
    wave_obj = sa.WaveObject.from_wave_file(audiofile)
    play_obj = wave_obj.play()

def stopAllAudio():
    sa.stop_all()



while True:
    if sonarMusica:
        playAudio('catimg/background10min.wav')
        sonarMusica=False
    if timerR >= randomSpawnR:
        listaCircleR.append(circle(560))
        randomSpawnR = random.randint(1, 3) * FPS
        timerR = 0
    else:
        timerR += 1

    if timerL >= randomSpawnL:
        listaCircleL.append(circle(415))
        randomSpawnL = random.randint(1, 5) * FPS
        timerL = 0
    else:
        timerL += 1

    hitY += 50

    # hitRect = pygame.Rect(560, hitY, 100, 100)
    pygame.display.set_caption('Bongo Hero Cat - ' + str(FPS) + ' FPS')
    colors = random.choice([RED, ORANGE, YELLOW, GREEN, BLUE, VIOLET])
    userKey = False
    displayCat.fill(WHITE)
    # if contadorKeys >= teclasforPress:
    #     texto = "EXPLOSION LISTA! Presiona Backspace!"
    #     blitX = 450
    #     blitY = 15
    texto = "Puntos: " + str(contadorKeys)
    textsurface = myfont.render(texto, False, (colors))

    if contadorKeys >= 20:
        winwin = "Ganaste! UwU"
        if audioWin:
            stopAllAudio()
            playAudio('catimg/win.wav')
            audioWin=False
            time.sleep(14)
            exit(code=None)
        wintext = myfont.render(winwin, False, (colors))
        displayCat.blit(wintext, (790, blitY))
        puntosDisplay = False
        for circulo in listaCircleR:
            circulo.mostrar = False
        for circulo in listaCircleL:
            circulo.mostrar = False
        # if puntos display =False not display
        #time.sleep(10)
        #exit(code=None)
    if contadorKeys <= -5:
        explosion=True
        if contadorSound:
            stopAllAudio()
            playAudio('catimg/Explosion+3.wav')
            # playAudio('catimg/crabrave.wav')
            contadorSound = False
        loselose = "Perdiste, intentalo de nuevo"
        losetext = myfont.render(loselose, False, (colors))
        displayCat.blit(losetext, (600, blitY))
        for circulo in listaCircleR:
            circulo.mostrar=False
        for circulo in listaCircleL:
            circulo.mostrar=False
        puntosDisplay=False
    # pressed = pygame.key.get_pressed()
    # if pressed[pygame.K_f]:
    #     # right
    #     playAudio('catimg/bongo0.wav')
    #     img_actual=catRight
    #     userKey = True
    # if pressed[pygame.K_s]:
    #     playAudio('catimg/bongo1.wav')
    #     img_actual=catLeft
    #     userKey = True
    # if pressed[pygame.K_d]:
    #     playAudio('catimg/bongo0.wav')
    #     img_actual=catBoth
    #     userKey = True


    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                playAudio('catimg/bongo0.wav')
                for circulo in listaCircleR:
                    if circulo.hitbox.colliderect(hitRight):
                        contadorKeys += 1
                        circulo.mostrar=False
                img_actual=catRight
                userKey = True
            if event.key == pygame.K_s:
                playAudio('catimg/bongo1.wav')
                for circulo in listaCircleL:
                    if circulo.hitbox.colliderect(hitLeft):
                        contadorKeys += 1
                        circulo.mostrar = False
                img_actual=catLeft
                userKey=True
            # if event.key == pygame.K_d:
            #     playAudio('catimg/bongo0.wav')
            #     img_actual=catBoth
            #     userKey=True
            # if event.key == pygame.K_BACKSPACE:
            #     if contadorKeys >= teclasforPress:
            #         playAudio('catimg/Explosion+3.wav')
            #         explosion = True
            #         playAudio('catimg/crabrave.wav')
    for circulo in listaCircleL:
        if circulo.hitbox.colliderect(hitFailLeft):
            contadorKeys -= 1
            circulo.mostrar=False
    for circulo in listaCircleR:
        if circulo.hitbox.colliderect(hitFailRight):
            contadorKeys -= 1
            circulo.mostrar=False

    if userKey and bloqueo == False:
        displayCat.blit(img_actual,(coorX,coorY))
        #playAudio('catimg/bongo0.mp3')
        userKey = False
    else:
        if explosion:
            # w/crab rave 9
            if contador % 15 == 0:
                img_actual = exp[actual]
                if actual == len(exp) - 1:
                    actual = 0
                    explosion = False
                    pygame.quit()
                    sys.exit()
                actual += 1
            #370x200
            displayCat.blit(img_actual, (460, 250))
            contador += 1
        else:
            displayCat.blit(catNothing, (coorX, coorY))

    if puntosDisplay:
        displayCat.blit(textsurface, (blitX, blitY))
    for circulo in listaCircleR:
        circulo.actualizarHitbox()
        #circulo.mostrarHitbox(displayCat)
        displayCat.blit(hitcircle, (560,circulo.Y))
        circulo.Y+=random.randint(bajandoY1,bajandoY2)
    for circulo in listaCircleL:
        circulo.actualizarHitbox()
        #circulo.mostrarHitbox(displayCat)
        displayCat.blit(hitcircle, (415,circulo.Y))
        circulo.Y+=random.randint(bajandoY1,bajandoY2)

    listaT=[]
    for circulo in listaCircleR:
        if circulo.mostrar:
            listaT.append(circulo)
    listaCircleR=listaT

    listaT=[]
    for circulo in listaCircleL:
        if circulo.mostrar:
            listaT.append(circulo)
    listaCircleL=listaT


    #pygame.draw.rect(displayCat, (0, 255, 0), hitRight)
    #pygame.draw.rect(displayCat, (0, 255, 0), hitLeft)
    #pygame.draw.rect(displayCat, (255, 0, 0), hitFailRight)
    #pygame.draw.rect(displayCat, (255, 0, 0), hitFailLeft)
    pygame.display.update()
    fpsClock.tick(FPS)