from card import Card
class Hand:

    def __init__(self, cards):
        #Defines a hand as 5 cards, note cards can be empty
        self.hand = [cards[0], cards[1], cards[2], cards[3], cards[4]]
        v1 = self.hand[0].val
        v2 = self.hand[1].val
        v3 = self.hand[2].val
        v4 = self.hand[3].val
        v5 = self.hand[4].val
        valsame = []
        suitsame = []
        #creates a list of all values in hand and sorts them
        vals = [v1, v2, v3, v4, v5]
        vals.sort()
        
        #creates values for how many iterations of cards having same values or same suits
        for i in len(self.hand):
            for j in len(self.hand):
                if i < j: 
                    if self.hand[i].val == self.hand[j].val:
                        valsame.append([i,j])
                    if self.hand[i].suit == self.hand[j].suit:
                        suitsame.append([i,j])
        #defines which value of same types for which hand
        if len(valsame) == 1:
            self.pair()
        elif len(valsame) == 2:
            self.two_pair()
        elif len(valsame) == 3:
            self.three_of_a_kind()
        elif len(valsame) == 7:
            self.four_of_a_kind()
        elif len(valsame) == 10 and not len(suitsame) == 10:
            self.five_of_a_kind()
        elif len(suitsame) == 10 and not len(valsame) == 10:
            self.flush()        
        elif vals == list(range(vals[0],vals[-1]+1)) or vals == [1,10,11,12,13] and not suitsame == 10:
            self.straight()
        elif (vals == list(range(vals[0],vals[-1]+1)) or vals == [1,10,11,12,13]) and suitsame == 10:
            if vals == [1,10,11,12,13]:
                self.royal_flush()
            else:
                self.straight_flush()
        elif len(suitsame) == 10 and len(valsame) == 10:
            self.flush_five()
        elif len(valsame) == 4 and not len(suitsame) == 10:
            self.full_house()
        elif len(valsame) == 4 and len(suitsame) == 10:
            self.flush_house()                                  
        else:
            self.high_card()
        
    def high_card(self):
        self.chips = 5
        self.mult = 1   
    
    def pair(self):
        self.chips = 10 
        self.mult = 2 
    
    def two_pair(self):
        self.chips = 20 
        self.mult = 2 
    
    def three_of_a_kind(self):
        self.chips = 30 
        self.mult = 3 
        
    def straight(self):
        self.chips = 30 
        self.mult = 4 
        
    def flush(self):
        self.chips = 35 
        self.mult = 4 
    
    def full_house(self):
        self.chips = 40 
        self.mult = 4       
         
    def four_of_a_kind(self):
        self.chips = 60 
        self.mult = 7 
    
    def straight_flush(self):
        self.chips = 100 
        self.mult = 8 
    
    def five_of_a_kind(self):
        self.chips = 120 
        self.mult = 12 
        
    def flush_house(self):
        self.chips = 140 
        self.mult = 14 
    
    def flush_five(self):
        self.chips = 160 
        self.mult = 16 