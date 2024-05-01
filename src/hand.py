from src.card import Card
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
        self.hand_name = ""
        #creates a list of all values in hand and sorts them
        vals = [v1, v2, v3, v4, v5]
        vals.sort()
        self.contributing = [0,0,0,0,0]
        #creates values for how many iterations of cards having same values or same suits
        for i in range(len(self.hand)):
            for j in range(len(self.hand)):
                if i < j: 
                    if self.hand[i].val == self.hand[j].val:
                        valsame.append([i,j])
                        self.contributing[i] = 1
                        self.contributing[j] = 1
                    if self.hand[i].suit == self.hand[j].suit:
                        suitsame.append([i,j])
        #defines which value of same types for which hand
        if len(valsame) == 1:
            self.pair()
            self.hand_name = "Pair"
        elif len(valsame) == 2:
            self.two_pair()
            self.hand_name = "Two Pair"
        elif len(valsame) == 3:
            self.three_of_a_kind()
            self.hand_name = "Three of A Kind"
        elif len(valsame) == 7:
            self.four_of_a_kind()
            self.hand_name = "Four of a Kind"
        elif len(valsame) == 10 and not len(suitsame) == 10:
            self.five_of_a_kind()
            self.hand_name = "Five of a Kind"
        elif len(suitsame) == 10 and not len(valsame) == 10:
            self.flush()
            self.hand_name = "Flush"        
        elif vals == list(range(vals[0],vals[-1]+1)) or vals == [1,10,11,12,13] and not suitsame == 10:
            self.straight()
            self.hand_name = "Straight"
        elif (vals == list(range(vals[0],vals[-1]+1)) or vals == [1,10,11,12,13]) and suitsame == 10:
            self.straight_flush()
            self.hand_name = "Straight Flush"
        elif len(suitsame) == 10 and len(valsame) == 10:
            self.flush_five()
            self.hand_name = "Flush Five"
        elif len(valsame) == 4 and not len(suitsame) == 10:
            self.full_house()
            self.hand_name = "Full House"
        elif len(valsame) == 4 and len(suitsame) == 10:
            self.flush_house()     
            self.hand_name = "Flush House"                             
        else:
            self.high_card()
            self.hand_name = "High Card"
    
    def name(self):
        return self.hand_name
    
    def chips_count(self):
        return self.chips
    
    def mult_count(self):
        return self.mult

    def order(self):
            print(len(self.hand))
            order = ""
            for i in range(len(self.hand)):
                    order += str(Card.name(self.hand[i])) + " of " + str(Card.suit_count(self.hand[i])) + ", Chips: " + str(Card.chips_count(self.hand[i])) + ", Mult: " + str(Card.mult_count(self.hand[i])) + "\n"
            return order



    def high_card(self):
        high_card_chips = 5
        self.chips = high_card_chips
        high_card_mult = 1
        self.mult = high_card_mult
   
    
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