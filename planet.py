from hand import Hand
class Planet:
    def __init__(self, planet):
        self.plan = planet
        if self.plan == "pluto":
            self.pluto()
        if self.plan == "mercury":
            self.mercury()
        if self.plan == "uranus":
            self.uranus()
        if self.plan == "jupiter":
            self.jupiter()
        if self.plan == "venus":
            self.venus()
        if self.plan == "earth":
            self.earth()
        if self.plan == "saturn":
            self.saturn()
        if self.plan == "mars":
            self.mars()
        if self.plan == "neptune":
            self.neptune()
        if self.plan == "planet_x":
            self.planet_x()    
        if self.plan == "ceres":
            self.ceres()    
        if self.plan == "eris":
            self.eris()    
                
    def pluto(high_card):
        high_card.chips += 10
        high_card.mult += 1
    def mercury(pair):
        pair.chips += 15
        pair.mult += 1  
    def uranus(two_pair):
        two_pair.chips += 20
        two_pair.mult += 1
    def jupiter(flush):
        flush.chips += 15
        flush.mult += 2
    def venus(three_of_a_kind):
        three_of_a_kind.chips += 20
        three_of_a_kind.mult += 2
    def earth(full_house):
        full_house.chips += 25
        full_house.mult += 2
    def saturn(straight):
        straight.chips += 30
        straight.mult += 2
    def mars(four_of_a_kind):
        four_of_a_kind.chips += 30
        four_of_a_kind.mult += 3
    def neptune(straight_flush):
        straight_flush.chips += 40
        straight_flush.mult += 3
    def planet_x(five_of_a_kind):
        five_of_a_kind.chips += 35
        five_of_a_kind.mult += 3
    def ceres(flush_house):
        flush_house.chips += 40
        flush_house.mult += 3
    def eris(flush_five):
        flush_five.chips += 40
        flush_five.mult += 3