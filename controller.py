from card import Card
import pygame

class Controller:
    def __init__(self):
        """
        docstring
        """
        
    def mainloop(self):
        while(True):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                deck = [card, card]
                card = card.Card()
                pygame.draw(deck)
                
                pygame.display.flip()