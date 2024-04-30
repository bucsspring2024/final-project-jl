class Card:
    def __init__(self, suit, val, buff = None):
        self.val = val
        self.buff = buff
        self.mult = 0
        self.name_current = ""
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
    
        
            
    def chips_count(self):
        return self.chips
    
    def mult_count(self):
        return self.mult
    
    def suit_count(self):
        return self.suit
    
    def name(self):
        return self.name_current
    
        #Needs section defining buffs
    