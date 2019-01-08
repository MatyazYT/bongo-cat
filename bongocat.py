import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 30# frames per second setting
fpsClock = pygame.time.Clock()

# set up the window
displayCat = pygame.display.set_mode((800, 600), 0, 32)
pygame.display.set_caption('Animation')

WHITE = (255, 255, 255)
catNothing = pygame.image.load('catimg/catNothing.png')
catLeft = pygame.image.load('catimg/catLeft.png')
catRight = pygame.image.load('catimg/catRight.png')
catBoth = pygame.image.load('catimg/catBoth.png')

def playAudio(audiofile):
    pygame.mixer.init()
    pygame.mixer.music.load(audiofile)
    pygame.mixer.music.play()
    pygame.event.wait()

while True:
    displayCat.fill(WHITE)

    displayCat.blit(catNothing, (0, 0))

    # pressed = pygame.key.get_pressed()
    # if pressed[pygame.K_d]:
    #     # right
    #     playAudio('catimg/bongo1.mp3')
    #     displayCat.blit(catRight, (0, 0))
    # if pressed[pygame.K_a]:
    #     playAudio('catimg/bongo0.mp3')
    #     displayCat.blit(catLeft, (0, 0))
    # if pressed[pygame.K_s]:
    #     playAudio('catimg/bongo4.mp3')
    #     displayCat.blit(catBoth, (0, 0))


    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.type == pygame.K_d:
                playAudio('catimg/bongo1.mp3')
                displayCat.blit(catRight, (0, 0))
            if event.type == pygame.K_a:
                playAudio('catimg/bongo0.mp3')
                displayCat.blit(catLeft, (0, 0))
            if event.type == pygame.K_s:
                playAudio('catimg/bongo4.mp3')
                displayCat.blit(catBoth, (0, 0))


    pygame.display.update()
    fpsClock.tick(FPS)