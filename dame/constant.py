import pygame

LARGEUR, HAUTEUR = 800, 800
LIGNES, COLONNES = 8, 8
TAILLE_CASE = LARGEUR//COLONNES

# rgb
ROUGE = (255, 0, 0)
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
BLEU = (0, 0, 255)
GRIS = (128,128,128)
marron = (88,41,0)
beige = (200,173,127)

COURONNE = pygame.transform.scale(pygame.image.load('assets/couronne.png'), (44, 25))