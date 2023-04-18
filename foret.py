#creer par nicolas
#creer le 2023-04-18
#dessine une foret

import pygame
import sys

#initialization des chose utile
pygame.init()
image_path = ""

#les fonctions
def demande():
    global image_path
    nbSapin = input("vous voulez tous beaucoup de sapin: ")
    path = ["picpick_39980-preview.jpeg", "téléchargement (1).jpg"]
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

#on quite
print("les sources pour les image:https://www.picandpick.com/soundwave-on-the-road/photos/39980-presque-%C3%AEle-gonfl%C3%A9e-de-sapins-sur-un-lac-bleu-turquoise- et https://fr.123rf.com/photo_76842552_touriste-visitant-le-lac-de-montagne-dans-la-for%C3%AAt-de-sapins-verts-dans-un-paysage-d-%C3%A9t%C3%A9-pittoresque-.html")
pygame.quit()
sys.exit()
