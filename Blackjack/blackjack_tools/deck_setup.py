import random

# 52 cards deck and hands creating (using OOP)
class Deck(object):
    deck_cards = []
    for i in range(1, 14):
        for j in range(4):
            if i == 1:
                deck_cards.append('A')
            elif i == 11:
                deck_cards.append('J')
            elif i == 12:
                deck_cards.append('Q')
            elif i == 13:
                deck_cards.append('K')
            else:
                deck_cards.append(str(i))


class Cards(Deck):
    def __init__(self):
        self.set = []

    def hit(self):
        adding_card = random.choice(Deck.deck_cards)
        self.set.append(adding_card)
        Deck.deck_cards.remove(adding_card)

    def retrieve(self):
        for card in self.set:
            Deck.deck_cards.append(card)