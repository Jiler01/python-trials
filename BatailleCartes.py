import random
import time
import os


class Maillon:
    def __init__(self, before, value, next):
        self.before: Maillon = before
        self.value = value
        self.next: Maillon = next

    def set_next(self, value):
        self.next = value

    def set_before(self, value):
        self.before = value


class File:
    def __init__(self, *args, mode: None | str = None):
        '''
        Mode : str default mode for self.take(): either 'FIFO' or 'LIFO'
        '''
        self.len = 0
        self.begining = Maillon(None, None, None)
        self.end = Maillon(self.begining, None, None)
        self.begining.set_next(self.end)
        self.mode = mode
        if self.mode == 'FIFO':
            self.take = self.take_first_in
        elif self.mode == 'LIFO':
            self.take = self.take_last_in

        for el in args:
            self.add(el)

    def add(self, value):
        self.begining.set_next(
            Maillon(self.begining, value, self.begining.next))
        self.begining.next.next.set_before(self.begining.next)
        self.len += 1

    def take_first_in(self):
        if self.end.before == self.begining:
            return None
        val = self.end.before.value
        self.end.before.before.set_next(self.end)
        self.end.set_before(self.end.before.before)
        self.len -= 1
        return val

    def take_last_in(self):
        if self.begining.next == self.end:
            return None
        val = self.begining.next.value
        self.begining.next.next.set_before(self.begining)
        self.begining.set_next(self.begining.next.next)
        self.len -= 1
        return val

    def __str__(self) -> str:
        s = '| ~ '
        c: Maillon = self.begining.next
        while c != self.end:
            s += str(c.value) + ' ~ '
            c = c.next
        return s + '|'


class Carte:
    def __init__(self, famille: str, valeur: int):
        self.famille = famille
        self.valeur = valeur

    def est_superieur_a(self, other, egality_fallback=lambda: False):
        return (self.valeur == 1 and other.valeur != 1) or (self.valeur > other.valeur and not other.valeur == 1)

    def __str__(self):
        conv = {1: 'A', 11: 'V', 12: 'D', 13: 'R'}
        if self.valeur in conv:
            return conv[self.valeur] + self.famille
        return str(self.valeur) + self.famille


class Jeu:
    def __init__(self, noms: list[str]):
        self.noms = noms
        self.creation_decks()
        self.finished = False
        self.jouer()

    def creation_decks(self):
        jeudecartes = []
        # Creation des cartes
        for num in range(1, 14):
            for fam in ['♠️', '♦️', '♥️', '♣️']:
                jeudecartes.append(Carte(fam, num))
        # Melange des cartes
        random.shuffle(jeudecartes)
        # Distribution des cartes
        self.decks: list[File] = []
        slic = len(jeudecartes)//len(self.noms)
        for i in range(len(self.noms)):
            deck = File(mode='FIFO')
            for carte in jeudecartes[slic*i:slic*(i+1)]:
                deck.add(carte)
            self.decks.append(deck)

    def jouer(self):
        os.system('cls')
        while not self.finished:
            self.tour_de_jeu()

    def purge(self):
        i = 0
        while i < len(self.decks):
            if self.decks[i].len == 0:
                print(f'{self.noms[i]} est éliminé faute de cartes.')
                self.noms.pop(i)
                self.decks.pop(i)
            else:
                i += 1
        if len(self.decks) == 1:
            print(f"{self.noms[0]} à gagné !")
            self.finished = True

    def tour_de_jeu(self):
        tour = 0

        # Jeux
        def jeux(tour, table: dict[int, dict[int, Carte]] = {}, say=True):
            if not self.finished:
                self.purge()
            if not self.finished:
                for joueur in range(len(self.decks)):
                    if joueur not in table:
                        table[joueur] = {}
                    c = self.decks[joueur].take()
                    if say:
                        print(f'{self.noms[joueur]} joue {c}.')
                    else:
                        print(f'{self.noms[joueur]} pose une carte retournée')
                    if c is not None:
                        table[joueur][tour] = c
            return table
        table = jeux(tour)

        # Gagnant
        gagnant_trouve = False
        while not gagnant_trouve:
            gagnant = None
            for joueur in table:
                if tour in table[joueur]:
                    if gagnant is not None and table[joueur][tour].valeur == table[gagnant][tour].valeur:
                        gagnant_trouve = False
                    if gagnant is None or table[joueur][tour].est_superieur_a(table[gagnant][tour]):
                        gagnant = joueur
                        gagnant_trouve = True
            if not gagnant_trouve:
                tour += 1
                table = jeux(tour, jeux(-tour, table, say=False))
            if self.finished:
                return
        print(f'{self.noms[gagnant]} remporte le tour.')  # type: ignore

        # Retour des cartes
        for joueur in table:
            for tour in table[joueur]:
                self.decks[gagnant].add(table[joueur][tour])  # type: ignore

        # Nombre de cartes
        for joueur in range(len(self.decks)):
            print(f'{self.noms[joueur]} a {self.decks[joueur].len} cartes')

        time.sleep(.5)
        os.system('cls')


# Jeu(['Zeus', 'Hades', 'Posseidon', 'Hera', 'Hestia',' Demeter', 'Athena', 'Ares', 'Appolon', 'Artemis'])
