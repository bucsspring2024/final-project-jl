from card import Card
class Deck:
    def __init__(self):
        #Starting a deck of empty cards
        self.cards = []
        #Making deck full of 52 cards, with 13 cards of each suit
        for i in range(1,14):
            for j in range(1,5):
                self.cards.append(Card(j, i, None))