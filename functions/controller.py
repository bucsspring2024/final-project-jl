from functions.deck import Deck
from functions.hand import Hand
from functions.math import Math
from functions.planet import Planet
import pygame

class Controller:
    def __init__(self):
        """
        docstring
        """
        screen = pygame.display.set_mode()
        screen.fill("white")
        self.mainloop(screen)

    def mainloop(self):
        while(True):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                self.deck = Deck()
                
        #Test 1: Description: Creating a Deck
        #Steps: Call the order function of the deck to print the total cards in the deck and a string of each card's name, suit, chips and mult.
        #Expected Outcome: 52, *Name* of *Suit*, Chips: *chips*, Mult: *mult*, from Ace to King, Spades,Clubs,Hearts,Diamonds, Chips from 11->2->13, Mult always 0
                print("Test 1:")                
                print(self.deck.order()) 
    

        #Test 2: Description: Shuffling Deck
        #Steps: Shuffle the deck, then call the order function again to show the deck order was changed.
        #Expected Outcome: 52, *Name* of *Suit*, Chips: *chips*, Mult: *mult* in random order of names, with their associated suits, chips and mults(0 so doesn't matter)
                print("Test 2:")
                self.deck.shuffle()
                print(self.deck.order())

        #Test 3: Description: Drawing a hand from deck
        #Steps: Creates a hand of 5 cards from the deck, taking from the top of the deck. Then uses the order function to show the same as before.
        #Expected Outcome: 5, whatever order Test 2's first 5 cards were in
                print("Test 3:")
                hand_array = []
                for i in range(5):
                    hand_array.append(self.deck.pull_card(i)) 
                hand = Hand(hand_array)
                print(hand.order())

        #Test 4: Description: Producing a total from a hand
        #Steps: Takes the hand from Test 3 and calculates the correct hand type, and then prints the name, and chips and mult associated with the hand. Includes the chips from the hand type but also the cards themselves.
        #Expected Outcome: *number of combined chips of all cards in hand added together*,*combined chips of cards with base hand chips*, *mult of hand, should be unchanged by cards*
                print("Test 4:")
                planet_name = Hand.name(hand)
                print(planet_name)
                card_chips = 0
                for i in range(len(hand.hand)):
                    card_chips += Hand.chips_count(hand.hand[i])
                print(card_chips)
                hand_chips = hand.chips_count() + card_chips
                print(hand_chips)
                hand_mult = hand.mult_count()
                print(hand_mult)
                val = Math(hand_chips, hand_mult)
                print(val.total())


        #Test 5: Description: Buying a planet from shop and checking change in total
        #Steps: Calls the planet function for whichever hand was played in Test 3 and found in Test 4, print to check chips/mult beforehand, then adds the chip/mult bonus from the planet card to the totals, then reprints again.
        #Expected Outcome: *Whatever chip and mult ended Test 4*, *Those numbers plus the new planet chips and mults*
                print("Test 5")
                #Shop in example will have high card planet, which user will buy
                print(hand_chips)
                print(hand_mult)
                planet = Planet(planet_name)
                Planet.shop_purchase(planet, planet_name,hand)
                hand_chips = hand.chips_count() + card_chips
                hand_mult = hand.mult_count()
                print(hand_chips)
                print(hand_mult)


        #Tests completed
                print("Tests complete!!")
                exit()