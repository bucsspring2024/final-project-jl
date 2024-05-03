from src.card import Card
class Hand:
    high_card_chips = 5
    high_card_mult = 1
    pair_chips = 10
    pair_mult = 2
    two_pair_chips = 20
    two_pair_mult = 2
    three_of_a_kind_chips = 30
    three_of_a_kind_mult = 3
    straight_chips = 30
    straight_mult = 4
    flush_chips = 35
    flush_mult = 4
    full_house_chips = 40
    full_house_mult = 4
    four_of_a_kind_chips = 60
    four_of_a_kind_mult = 7
    straight_flush_chips = 100
    straight_flush_mult = 8
    five_of_a_kind_chips = 120
    five_of_a_kind_mult = 12
    flush_house_chips = 140
    flush_house_mult = 14
    flush_five_chips = 160
    flush_five_mult = 16
    def __init__(self, cards, procced_planets):
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
            self.pair(procced_planets)
            self.hand_name = "Pair"
        elif len(valsame) == 2:
            self.two_pair(procced_planets)
            self.hand_name = "Two Pair"
        elif len(valsame) == 3:
            self.three_of_a_kind(procced_planets)
            self.hand_name = "Three of A Kind"
        elif len(valsame) == 7:
            self.four_of_a_kind(procced_planets)
            self.hand_name = "Four of a Kind"
        elif len(valsame) == 10 and not len(suitsame) == 10:
            self.five_of_a_kind(procced_planets)
            self.hand_name = "Five of a Kind"
        elif len(suitsame) == 10 and not len(valsame) == 10:
            self.flush(procced_planets)
            self.hand_name = "Flush"        
        elif vals == list(range(vals[0],vals[-1]+1)) or vals == [1,10,11,12,13] and not suitsame == 10:
            self.straight(procced_planets)
            self.hand_name = "Straight"
        elif (vals == list(range(vals[0],vals[-1]+1)) or vals == [1,10,11,12,13]) and suitsame == 10:
            self.straight_flush(procced_planets)
            self.hand_name = "Straight Flush"
        elif len(suitsame) == 10 and len(valsame) == 10:
            self.flush_five(procced_planets)
            self.hand_name = "Flush Five"
        elif len(valsame) == 4 and not len(suitsame) == 10:
            self.full_house(procced_planets)
            self.hand_name = "Full House"
        elif len(valsame) == 4 and len(suitsame) == 10:
            self.flush_house(procced_planets)     
            self.hand_name = "Flush House"                             
        else:
            self.high_card(procced_planets)
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



    def high_card(self,procced_planets):
        self.chips = self.high_card_chips + 10*procced_planets[0]
        self.mult = self.high_card_mult + 1*procced_planets[0]
   
    
    def pair(self,procced_planets):

        self.chips = self.pair_chips +15*procced_planets[1]
        self.mult = self.pair_mult +1*procced_planets[1]

    
    def two_pair(self,procced_planets):

        self.chips = self.two_pair_chips +20*procced_planets[2]
        self.mult = self.two_pair_mult +1*procced_planets[2]
    
    def three_of_a_kind(self,procced_planets):

        self.chips = self.three_of_a_kind_chips +20*procced_planets[3]
        self.mult = self.three_of_a_kind_mult  +2*procced_planets[3]
 
    def flush(self,procced_planets):

        self.chips = self.flush_chips +15*procced_planets[4]
        self.mult = self.flush_mult +2*procced_planets[4]
    
    def full_house(self,procced_planets):

        self.chips = self.full_house_chips +25*procced_planets[5]
        self.mult = self.full_house_mult +2*procced_planets[5]     

    def straight(self,procced_planets):

        self.chips = self.straight_chips  +30*procced_planets[6]
        self.mult = self.straight_mult +2*procced_planets[6]

    def four_of_a_kind(self,procced_planets):

        self.chips = self.four_of_a_kind_chips +30*procced_planets[7]
        self.mult = self.four_of_a_kind_mult  +3*procced_planets[7]
    
    def straight_flush(self,procced_planets):

        self.chips = self.straight_flush_chips +40*procced_planets[8]
        self.mult = self.straight_flush_mult +3**procced_planets[8]
    
    def five_of_a_kind(self,procced_planets):

        self.chips = self.five_of_a_kind_chips +35*procced_planets[9]
        self.mult = self.five_of_a_kind_mult +3*procced_planets[9]
        
    def flush_house(self,procced_planets):

        self.chips = self.flush_house_chips +40*procced_planets[10]
        self.mult = self.flush_house_mult +3*procced_planets[10]
    
    def flush_five(self,procced_planets):

        self.chips = self.flush_five_chips +40*procced_planets[11]
        self.mult = self.flush_five_mult +3*procced_planets[11]