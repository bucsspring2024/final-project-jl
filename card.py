class Card:
    def __init__(self, suit, val, buff = None):
        self.val = val
        self.buff = buff
        #Defining suits of cards
        if suit == 1:
            self.suit = "Spade"
        if suit == 2:
            self.suit = "Club"
        if suit == 3:
            self.suit = "Heart"
        if suit == 4:
            self.suit = "Diamond" 
        #Defining chip value for each card, Ace has value of 1, 2-10 are 2-10 and Jack,Queen,King are 11-13    
        if self.val == 1:  
            self.chips = 11
        if self.val in range(2,11):
            self.chips = self.val
        if self.val in range(11,14):
            self.chips = 10
            
        #Needs section defining buffs