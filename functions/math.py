from functions.card import Card
from functions.planet import Planet
class Math:
    def __init__(self, plan_chips, plan_mult):
        self.chips = plan_chips
        self.mult = plan_mult
        

    def add_cards(self, card_chips, card_mult):
        self.chips += Card.chips_count(card_chips)
        self.mult += Card.mult_count(card_mult)

        
    
    def add_jokers(self, joker_chips, joker_mult):
        self.total_chips += joker_chips
        self.total_mult += joker_mult

    def total(self):
        return "Total: " + str(self.chips * self.mult)