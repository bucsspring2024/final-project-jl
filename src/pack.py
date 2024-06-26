import pygame
from src.planet import Planet
from src.tarot import Tarot
from src.card import Card
class Pack:
    def __init__(self, choice, screen, width, height, field_array, procced_planets):
        self.screen = screen
        self.screen.fill("Green")
        if choice == "Plan":
            self.plan_pack(width, height, procced_planets)
        if choice == "Tarot":
            self.tarot_pack(width, height, field_array)
        if choice == "Card":
            self.card_pack(width, height)            

    def plan_pack(self, width, height, procced_planets): 
        self.pack1 = Planet.rand_plan()
        self.pack2 = Planet.rand_plan()
        self.pack3 = Planet.rand_plan()
        self.pack4 = Planet.rand_plan()
        self.user_choice = ""
        self.rect1 = pygame.Rect((width/8)-75, (height/2)-100, 150, 300)
        self.rect2 = pygame.Rect((width/4)+(width/8)-75, (height/2)-100, 150, 300)
        self.rect3 = pygame.Rect((width/2)+75, (height/2)-100, 150, 300)
        self.rect4 = pygame.Rect(width-(width/8)-75, (height/2)-100, 150, 300)
        pygame.draw.rect(self.screen, "Blue", self.rect1)
        pygame.draw.rect(self.screen, "Blue", self.rect2)
        pygame.draw.rect(self.screen, "Blue", self.rect3)
        pygame.draw.rect(self.screen, "Blue", self.rect4)
        pygame.display.flip()
        while True:
            for event in pygame.event.get():  
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print("mouse down")
                    self.position = pygame.mouse.get_pos()
                    if self.rect1.collidepoint(self.position):
                        self.user_choice = self.pack1
                        print("pack1")
                        break
                    if self.rect2.collidepoint(self.position):
                        self.user_choice = self.pack2
                        print("pack2")
                        break
                    if self.rect3.collidepoint(self.position):
                        self.user_choice = self.pack3
                        print("pack3")

                        break
                    if self.rect4.collidepoint(self.position):
                        self.user_choice = self.pack4
                        print("pack4")

                        break
                    print(self.user_choice)
            Planet.plan_proc(self.user_choice, procced_planets)
            break

    def tarot_pack(self, width, height, field_array):
        self.tarot1 = Tarot.rand_tar()
        self.tarot2 = Tarot.rand_tar()
        self.tarot3 = Tarot.rand_tar()
        self.tarot4 = Tarot.rand_tar()
        self.user_choice = ""
        self.rect1 = pygame.Rect((width/8)-75, (height/2)-100, 150, 300)
        self.rect2 = pygame.Rect((width/4)+(width/8)-75, (height/2)-100, 150, 300)
        self.rect3 = pygame.Rect((width/2)+75, (height/2)-100, 150, 300)
        self.rect4 = pygame.Rect(width-(width/8)-75, (height/2)-100, 150, 300)
        pygame.draw.rect(self.screen, "Purple", self.rect1)
        pygame.draw.rect(self.screen, "Purple", self.rect2)
        pygame.draw.rect(self.screen, "Purple", self.rect3)
        pygame.draw.rect(self.screen, "Purple", self.rect4)
        pygame.display.flip()
        while True:
            for event in pygame.event.get():  
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.position = pygame.mouse.get_pos()
                    if self.rect1.collidepoint(self.position):
                        self.user_choice = self.tarot1
                        break
                    if self.rect2.collidepoint(self.position):
                        self.user_choice = self.tarot2
                        break
                    if self.rect3.collidepoint(self.position):
                        self.user_choice = self.tarot3
                        break
                    if self.rect4.collidepoint(self.position):
                        self.user_choice = self.tarot4
                        break
            Tarot.shop_purchase(self.user_choice, field_array)
            break

    def card_pack(self, width, height):
        self.card1 = Card.rand_card()
        self.card2 = Card.rand_card()
        self.card3 = Card.rand_card()
        self.card4 = Card.rand_card()
        self.user_choice = ""
        self.rect1 = pygame.Rect((width/8)-75, (height/2)-100, 150, 300)
        self.rect2 = pygame.Rect((width/4)+(width/8)-75, (height/2)-100, 150, 300)
        self.rect3 = pygame.Rect((width/2)+75, (height/2)-100, 150, 300)
        self.rect4 = pygame.Rect(width-(width/8)-75, (height/2)-100, 150, 300)
        pygame.draw.rect(self.screen, "Brown", self.rect1)
        pygame.draw.rect(self.screen, "Brown", self.rect2)
        pygame.draw.rect(self.screen, "Brown", self.rect3)
        pygame.draw.rect(self.screen, "Brown", self.rect4)
        pygame.display.flip()
        while True:
            for event in pygame.event.get():  
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.position = pygame.mouse.get_pos()
                    if self.rect1.collidepoint(self.position):
                        self.user_choice = self.card1
                        break
                    if self.rect2.collidepoint(self.position):
                        self.user_choice = self.card2
                        break
                    if self.rect3.collidepoint(self.position):
                        self.user_choice = self.card3
                        break
                    if self.rect4.collidepoint(self.position):
                        self.user_choice = self.card4
                        break
            
            Card.shop_purchase(self.user_choice)
            break