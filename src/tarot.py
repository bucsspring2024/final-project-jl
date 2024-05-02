import random
import pygame
from src.card import Card
from src.deck import Deck
from src.hand import Hand
from src.planet import Planet
class Tarot:
    def __init__(self, field_wid, field_height):
        self.tarot_array = ["Magician", "High Priestess", "Empress", "Emperor", "Hierophant", "Hermit", "Strength", "Hanged Man", "Temperance", "Star", "Moon", "Sun", "World"]
        self.rect = pygame.Rect(field_wid/3, field_height - 20)

    def rand_tar(self):
        rand = random.randint(0, 12)
        return self.tarot_array[rand]
    
    def shop_purchase(self, shop_card, field):
        self.tar = shop_card
        if self.tar == "Magician":
            field.append(self.magician(self.rect))
        if self.tar == "High Priestess":
            field.append(self.high_priestess(self.rect))
        if self.tar == "Empress":
            field.append(self.empress(self.rect))
        if self.tar == "Emperor":
            field.append(self.emperor(self.rect))
        if self.tar == "Hierophant":
            field.append(self.hierophant(self.rect))
        if self.tar == "Hermit":
            field.append(self.hermit(self.rect))
        if self.tar == "Strength":
            field.append(self.strength(self.rect))
        if self.tar == "Hanged Man":
            field.append(self.hanged_man(self.rect))
        if self.tar == "Temperance":
            field.append(self.temperance(self.rect))
        if self.tar == "Star":
            field.append(self.star(self.rect))
        if self.tar == "Moon":
            field.append(self.moon(self.rect))
        if self.tar == "Sun":
            field.append(self.sun(self.rect))
        if self.tar == "World":
            field.append(self.world(Hand.hand,self.rect))
        return field

    def run_Tarot(self, name, card, img, field_array, money, joker_money, deck):
        if name == "Magician":
                card.buff = "Lucky"
        if name == "High Priestess":
            Planet.plan_proc(Planet.rand_plan())
            Planet.plan_proc(Planet.rand_plan())
        if name == "Empress":
                card.buff = "Mult"
        if name == "Emperor":
            tarot1 = self.rand_tar()
            tarot2 = self.rand_tar()
            field_array.append(tarot1)
            field_array.append(tarot2)
        if name == "Hierophant":
                card.buff = "Chips"
        if name == "Hermit":
            if money > 20:
                money += 20
            else:
                money += money
        if name == "Strength":
                card.val += 1
        if name == "Hanged Man":
                deck.remove(card)
        if name == "Temperance":
            money += joker_money
        if name == "Star":
            card.suit = "Diamonds"
        if name == "Moon":
            card.suit = "Clubs"
        if name == "Sun":
            card.suit = "Hearts"
        if name == "World": 
            card.suit = "Spades"
