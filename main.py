import pygame
import sys
from dame.constant import LARGEUR, HAUTEUR, TAILLE_CASE, ROUGE
from dame.jeu import Jeu

FPS = 60

WIN = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption('Jeu de dames / MD4')

def obtenir_ligne_colonne_de_souris(pos):
    x, y = pos
    ligne = y // TAILLE_CASE
    colonne = x // TAILLE_CASE
    return ligne, colonne

def principal():
    run = True
    clock = pygame.time.Clock()
    jeu = Jeu(WIN)

    while run:
        clock.tick(FPS)

        if jeu.gagnant() is not None:
            print(jeu.gagnant())
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                ligne, colonne = obtenir_ligne_colonne_de_souris(pos)
                jeu.selectionner(ligne, colonne)

        jeu.mettre_a_jour()
    
    pygame.quit()

principal()