from src.hand import Hand
import random
class Planet:
    def __init__(self, hand_name):
        self.hand = hand_name
        self.plan_array = ["High Card", "Pair", "Two Pair", "Flush", "Three of A Kind", "Full House", "Straight", "Four of a Kind", "Straight Flush", "Five of a Kind","Flush House","Flush Five"]

    def rand_plan(self):
        rand = random.randint(0, 11)
        return self.plan_array[rand]
    
    def plan_proc(self, shop_card, hand):
        self.plan = shop_card
        if self.plan == "High Card":
            hand.chips += 10
            hand.mult += 1
        if self.plan == "Pair":
            hand.chips += 15
            hand.mult += 1 
        if self.plan == "Two Pair":
            hand.chips += 20
            hand.mult += 1
        if self.plan == "Flush":
            hand.chips += 15
            hand.mult += 2
        if self.plan == "Three of A Kind":
            hand.chips += 20
            hand.mult += 2
        if self.plan == "Full House":
            hand.chips += 25
            hand.mult += 2
        if self.plan == "Straight":
            hand.chips += 30
            hand.mult += 2
        if self.plan == "Four of a Kind":
            hand.chips += 30
            hand.mult += 3
        if self.plan == "Straight Flush":
            hand.chips += 40
            hand.mult += 3
        if self.plan == "Five of a Kind":
            hand.chips += 35
            hand.mult += 3    
        if self.plan == "Flush House":
            hand.chips += 40
            hand.mult += 3    
        if self.plan == "Flush Five":
            hand.chips += 40
            hand.mult += 3   
                
