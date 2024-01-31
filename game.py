import pygame
from .constants import ROUGE, BLANC, BLEU, TAILLE_CASE, NOIR
from checkers.plateau import Plateau

class Jeu:
    def __init__(self, win):
        self._init()
        self.win = win
    
    def mettre_a_jour(self):
        self.plateau.dessiner(self.win)
        self.dessiner_coups_valides(self.coups_valides)
        pygame.display.update()

    def _init(self):
        self.selectionne = None
        self.plateau = Plateau()
        self.tour = NOIR
        self.coups_valides = {}

    def gagnant(self):
        return self.plateau.gagnant()

    def reinitialiser(self):
        self._init()

    def selectionner(self, ligne, colonne):
        if self.selectionne:
            resultat = self._deplacer(ligne, colonne)
            if not resultat:
                self.selectionne = None
                self.selectionner(ligne, colonne)
        
        piece = self.plateau.obtenir_piece(ligne, colonne)
        if piece != 0 and piece.couleur == self.tour:
            self.selectionne = piece
            self.coups_valides = self.plateau.obtenir_coups_valides(piece)
            return True
            
        return False

    def _deplacer(self, ligne, colonne):
        piece = self.plateau.obtenir_piece(ligne, colonne)
        if self.selectionne and piece == 0 and (ligne, colonne) in self.coups_valides:
            self.plateau.deplacer(self.selectionne, ligne, colonne)
            sautes = self.coups_valides[(ligne, colonne)]
            if sautes:
                self.plateau.retirer(sautes)
            self.changer_tour()
        else:
            return False

        return True

    def dessiner_coups_valides(self, coups):
        for coup in coups:
            ligne, colonne = coup
            pygame.draw.circle(self.win, BLEU, (colonne * TAILLE_CASE + TAILLE_CASE//2, ligne * TAILLE_CASE + TAILLE_CASE//2), 15)

    def changer_tour(self):
        self.coups_valides = {}
        if self.tour == NOIR:
            self.tour = BLANC
        else:
            self.tour = NOIR
