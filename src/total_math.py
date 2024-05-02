from src.card import Card
from src.planet import Planet
class Total_Math:
    def __init__(self, plan_chips, plan_mult):
        self.chips = 0
        self.mult = 0
        self.chips += plan_chips
        self.mult += plan_mult
        

    def add_cards(self, hand_chips, hand_mult):
        self.chips += hand_chips
        self.mult += hand_mult

        
    def add_jokers(self, joker_chips, joker_mult):
        self.chips += joker_chips
        self.mult += joker_mult

    def total(self):
        return self.chips * self.mult