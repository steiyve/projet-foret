#creer par nicolas
#creer le 2023-04-18
#dessine une foret

import pygame
import sys
import turtle

#initialization des chose utile
pygame.init()
image_path = ""
t = turtle.Turtle()

#les fonctions
def demande():
    global image_path
    nbSapin = input("vous voulez tous beaucoup de sapin: ")
    path = ["image/picpick_39980-preview.jpeg", "image/téléchargement (1).jpg"]
    #de la logique pour les sapin
    if nbSapin == "oui":
        image_path = path[1]
    else:
        image_path = path[0]    

demande()
image = pygame.image.load(image_path)
#creer le fenetre et cest atribut
screen_width, screen_height = image.get_size()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("projet foret")

#dessiner limage
screen.blit(image, (0, 0))
pygame.display.flip()

#des variable
running = True
#une boucle
while running:
    #une autre boucle
    for event in pygame.event.get():
        #de la logique
        if event.type == pygame.QUIT:
            running = False

for i in range(18):
    t.fd(33)
    t.left(180-(360/19))

#on quite
print("les source pour les image sont dans source.txt")
pygame.quit()
sys.exit()
