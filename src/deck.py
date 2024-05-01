from src.card import Card
import random
class Deck:
    def __init__(self):
        #Starting a deck of empty cards
        self.cards = []
        #Making deck full of 52 cards, with 13 cards of each suit
        for i in range(1,14):
            for j in range(1,5):
                self.cards.append(Card(j, i, None))

    def pull_card(self, place):
        return self.cards[place]

    def order(self):
        print(len(self.cards))
        order = ""
        for i in range(len(self.cards)):
                order += str(Card.name(self.cards[i])) + " of " + str(Card.suit_count(self.cards[i])) + ", Chips: " + str(Card.chips_count(self.cards[i])) + ", Mult: " + str(Card.mult_count(self.cards[i])) + "\n"
        return order
    
    def shuffle(self):
        random.shuffle(self.cards)