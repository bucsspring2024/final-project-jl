from src.card import Card
import random
import pygame
class Deck:
    def __init__(self, field_wid, field_height):
        #Starting a deck of empty cards
        self.field_wid = field_wid
        self.field_height = field_height
        self.cards = []
        self.left = 0
        self.top = 0
        

        #Making deck full of 52 cards, with 13 cards of each suit
        for i in range(1,14):
            for j in range(1,5):
                self.img = pygame.Rect(self.left, self.top, self.field_wid/3, self.field_height - 20)
                self.cards.append(Card(j, i, self.img, None))

    def print_img(self):
        return self.img

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