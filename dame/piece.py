from .constant import ROUGE, BLANC, TAILLE_CASE, GRIS, COURONNE
import pygame

class Piece:
    MARGE = 15
    CONTOUR = 2

    def __init__(self, ligne, colonne, couleur):
        self.ligne = ligne
        self.colonne = colonne
        self.couleur = couleur
        self.roi = False
        self.x = 0
        self.y = 0
        self.calculer_position()

    def calculer_position(self):
        self.x = TAILLE_CASE * self.colonne + TAILLE_CASE // 2
        self.y = TAILLE_CASE * self.ligne + TAILLE_CASE // 2

    def promouvoir_roi(self):
        self.roi = True
    
    def dessiner(self, win):
        rayon = TAILLE_CASE//2 - self.MARGE
        pygame.draw.circle(win, GRIS, (self.x, self.y), rayon + self.CONTOUR)
        pygame.draw.circle(win, self.couleur, (self.x, self.y), rayon)
        if self.roi:
            win.blit(COURONNE, (self.x - COURONNE.get_width()//2, self.y - COURONNE.get_height()//2))

    def deplacer(self, ligne, colonne):
        self.ligne = ligne
        self.colonne = colonne
        self.calculer_position()

    def __repr__(self):
        return str(self.couleur)