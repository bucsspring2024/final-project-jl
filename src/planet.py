from src.hand import Hand
import random
class Planet:
    def __init__(self, hand_name):
        self.hand = hand_name
        

    def rand_plan():
        rand = random.randint(0, 11)
        plan_array = ["High Card", "Pair", "Two Pair", "Flush", "Three of A Kind", "Full House", "Straight", "Four of a Kind", "Straight Flush", "Five of a Kind","Flush House","Flush Five"]
        return plan_array[rand]
    

    def plan_proc(shop_card, procced_planets):
        plan = shop_card
        if plan == "High Card":
            procced_planets[0]+=1

        if plan == "Pair":
            procced_planets[1]+=1

        if plan == "Two Pair":
            procced_planets[2]+=1

        if plan == "Flush":
            procced_planets[3]+=1

        if plan == "Three of A Kind":
            procced_planets[4]+=1

        if plan == "Full House":
            procced_planets[5]+=1

        if plan == "Straight":
            procced_planets[6]+=1

        if plan == "Four of a Kind":
            procced_planets[7]+=1

        if plan == "Straight Flush":
            procced_planets[8]+=1

        if plan == "Five of a Kind":
            procced_planets[9]+=1

        if plan == "Flush House":
            procced_planets[10]+=1 

        if plan == "Flush Five":
            procced_planets[11]+=1
        return procced_planets
