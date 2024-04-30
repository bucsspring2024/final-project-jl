from functions.hand import Hand
class Planet:
    def __init__(self, hand_name):
        self.hand = hand_name



    def shop_purchase(self, shop_card,hand):
        self.plan = shop_card
        if self.plan == "High Card":
            self.pluto(hand)
        if self.plan == "Pair":
            self.mercury(hand)
        if self.plan == "Two Pair":
            self.uranus(hand)
        if self.plan == "Flush":
            self.jupiter(hand)
        if self.plan == "Three of A Kind":
            self.venus(hand)
        if self.plan == "Full House":
            self.earth(hand)
        if self.plan == "Straight":
            self.saturn(hand)
        if self.plan == "Four of a Kind":
            self.mars(hand)
        if self.plan == "Straight Flush":
            self.neptune(hand)
        if self.plan == "Five of a Kind":
            self.planet_x(hand)    
        if self.plan == "Flush House":
            self.ceres(hand)    
        if self.plan == "Flush Five":
            self.eris(hand)    
                
    def pluto(self,hand):
        hand.chips += 10
        hand.mult += 1
    def mercury(self,hand):
        hand.chips += 15
        hand.mult += 1  
    def uranus(self,hand):
        hand.chips += 20
        hand.mult += 1
    def jupiter(self,hand):
        hand.chips += 15
        hand.mult += 2
    def venus(self,hand):
        hand.chips += 20
        hand.mult += 2
    def earth(self,hand):
        hand.chips += 25
        hand.mult += 2
    def saturn(self,hand):
        hand.chips += 30
        hand.mult += 2
    def mars(self,hand):
        hand.chips += 30
        hand.mult += 3
    def neptune(self,hand):
        hand.chips += 40
        hand.mult += 3
    def planet_x(self,hand):
        hand.chips += 35
        hand.mult += 3
    def ceres(self,hand):
        hand.chips += 40
        hand.mult += 3
    def eris(self,hand):
        hand.chips += 40
        hand.mult += 3