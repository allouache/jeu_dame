import pygame
from .constant import NOIR, LIGNES, TAILLE_CASE, COLONNES, marron, BLANC, beige
from .piece import Piece

class Plateau:
    def __init__(self):
        self.plateau = []
        self.rouge_restants = self.blanc_restants = 12
        self.rouge_rois = self.blanc_rois = 0
        self.creer_plateau()
    
    def dessiner_cases(self, win):
        win.fill(beige)
        for ligne in range(LIGNES):
            for colonne in range(ligne % 2, COLONNES, 2):
                pygame.draw.rect(win, marron, (ligne*TAILLE_CASE, colonne *TAILLE_CASE, TAILLE_CASE, TAILLE_CASE))

    def deplacer(self, piece, ligne, colonne):
        self.plateau[piece.ligne][piece.colonne], self.plateau[ligne][colonne] = self.plateau[ligne][colonne], self.plateau[piece.ligne][piece.colonne]
        piece.deplacer(ligne, colonne)

        if ligne == LIGNES - 1 or ligne == 0:
            piece.promouvoir_roi()
            if piece.couleur == BLANC:
                self.blanc_rois += 1
            else:
                self.rouge_rois += 1 

    def obtenir_piece(self, ligne, colonne):
        return self.plateau[ligne][colonne]

    def creer_plateau(self):
        for ligne in range(LIGNES):
            self.plateau.append([])
            for colonne in range(COLONNES):
                if colonne % 2 == ((ligne + 1) % 2):
                    if ligne < 3:
                        self.plateau[ligne].append(Piece(ligne, colonne, BLANC))
                    elif ligne > 4:
                        self.plateau[ligne].append(Piece(ligne, colonne, NOIR))
                    else:
                        self.plateau[ligne].append(0)
                else:
                    self.plateau[ligne].append(0)
        
    def dessiner(self, win):
        self.dessiner_cases(win)
        for ligne in range(LIGNES):
            for colonne in range(COLONNES):
                piece = self.plateau[ligne][colonne]
                if piece != 0:
                    piece.dessiner(win)

    def retirer(self, pieces):
        for piece in pieces:
            self.plateau[piece.ligne][piece.colonne] = 0
            if piece != 0:
                if piece.couleur == NOIR:
                    self.rouge_restants -= 1
                else:
                    self.blanc_restants -= 1
    
    def gagnant(self):
        if self.rouge_restants <= 0:
            return BLANC
        elif self.blanc_restants <= 0:
            return NOIR
        
        return None 
    
    def obtenir_coups_valides(self, piece):
        coups = {}
        gauche = piece.colonne - 1
        droite = piece.colonne + 1
        ligne = piece.ligne

        if piece.couleur == NOIR or piece.roi:
            coups.update(self._traverser_gauche(ligne -1, max(ligne-3, -1), -1, piece.couleur, gauche))
            coups.update(self._traverser_droite(ligne -1, max(ligne-3, -1), -1, piece.couleur, droite))
        if piece.couleur == BLANC or piece.roi:
            coups.update(self._traverser_gauche(ligne +1, min(ligne+3, LIGNES), 1, piece.couleur, gauche))
            coups.update(self._traverser_droite(ligne +1, min(ligne+3, LIGNES), 1, piece.couleur, droite))
    
        return coups

    def _traverser_gauche(self, debut, fin, pas, couleur, gauche, sautes=[]):
        coups = {}
        dernier = []
        for r in range(debut, fin, pas):
            if gauche < 0:
                break
            
            actuel = self.plateau[r][gauche]
            if actuel == 0:
                if sautes and not dernier:
                    break
                elif sautes:
                    coups[(r, gauche)] = dernier + sautes
                else:
                    coups[(r, gauche)] = dernier
                
                if dernier:
                    if pas == -1:
                        ligne = max(r-3, 0)
                    else:
                        ligne = min(r+3, LIGNES)
                    coups.update(self._traverser_gauche(r+pas, ligne, pas, couleur, gauche-1, sautes=dernier))
                    coups.update(self._traverser_droite(r+pas, ligne, pas, couleur, gauche+1, sautes=dernier))
                break
            elif actuel.couleur == couleur:
                break
            else:
                dernier = [actuel]

            gauche -= 1
        
        return coups

    def _traverser_droite(self, debut, fin, pas, couleur, droite, sautes=[]):
        coups = {}
        dernier = []
        for r in range(debut, fin, pas):
            if droite >= COLONNES:
                break
            
            actuel = self.plateau[r][droite]
            if actuel == 0:
                if sautes and not dernier:
                    break
                elif sautes:
                    coups[(r,droite)] = dernier + sautes
                else:
                    coups[(r, droite)] = dernier
                
                if dernier:
                    if pas == -1:
                        ligne = max(r-3, 0)
                    else:
                        ligne = min(r+3, LIGNES)
                    coups.update(self._traverser_gauche(r+pas, ligne, pas, couleur, droite-1, sautes=dernier))
                    coups.update(self._traverser_droite(r+pas, ligne, pas, couleur, droite+1, sautes=dernier))
                break
            elif actuel.couleur == couleur:
                break
            else:
                dernier = [actuel]

            droite += 1
        
        return coups