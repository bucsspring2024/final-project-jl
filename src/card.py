import random
import pygame
class Card:
    def __init__(self, suit, val, image, buff = None):
        self.val = val
        self.buff = buff
        self.mult = 0
        self.name_current = ""

        self.img = image
        #Defining suits of cards
        if suit == 1:
            self.suit = "Spades"
        if suit == 2:
            self.suit = "Clubs"
        if suit == 3:
            self.suit = "Hearts"
        if suit == 4:
            self.suit = "Diamonds" 
        #Defining chip value for each card, Ace has value of 1, 2-10 are 2-10 and Jack,Queen,King are 11-13    
        if self.val == 1:  
            self.chips = 11
            self.name_current = "Ace"
        if self.val in range(2,11):
            self.chips = self.val
            self.name_current = str(self.val)
        if self.val in range(11,14):
            self.chips = 10
            if self.val == 11:
                self.name_current = "Jack"
            if self.val == 12:
                self.name_current = "Queen"
            if self.val == 13:
                self.name_current = "King"
    
    def rand_card(self):
        rand_val = random.randint(0, 11)
        rand_suit = random.randint(0,3)
        card_array = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
        suit_array = ["Spades", "Clubs", "Hearts", "Diamonds"]
        return card_array[rand_val], suit_array[rand_suit]
        
    
            
    def chips_count(self):
        return self.chips
    
    def mult_count(self):
        return self.mult
    
    def suit_count(self):
        return self.suit
    
    def name(self):
        return self.name_current
    
        #Needs section defining buffs
