# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/01_deck.ipynb.

# %% auto 0
__all__ = ['Deck']

# %% ../nbs/01_deck.ipynb 2
from fastcore.utils import *
from .card import *
# import random

# %% ../nbs/01_deck.ipynb 5
class Deck:
    def __init__(self):
        self.cards = [Card(s,r) for s in range(4) for r in range(1,14)]
    def __len__(self):
        return len(self.cards)
    def __str__(self):
        return '; '.join((map(str, self.cards)))
    def __contains__(self, card):
        return card in self.cards
    __repr__ = __str__

# %% ../nbs/01_deck.ipynb 18
@patch
def remove(self:Deck,
           card:Card): # Card to remove
    "Removes `card` from the deck or raises exception if it is not there"
    self.cards.remove(card)

# %% ../nbs/01_deck.ipynb 22
def draw_n(n:int, # number of cards to draw
           replace:bool=True): # whether or not draw with replacement
    "Draw `n` cards, with replacement iif `replace`"
    d = Deck()
    d.shuffle()
    if replace: return [d.cards[random.choice(range(len(d.cards)))] for _ in range(n)]
    else: return d.cards[:n]

# %% ../nbs/01_deck.ipynb 22
def draw_n(n:int, # number of cards to draw
           replace:bool=True): # whether or not draw with replacement
    "Draw `n` cards, with replacement iif `replace`"
    d = Deck()
    d.shuffle()
    if replace: return [d.cards[random.choice(range(len(d.cards)))] for _ in range(n)]
    else: return d.cards[:n]
