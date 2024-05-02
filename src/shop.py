from src.pack import Pack
from src.joker import Joker
import pygame
import random
class Shop:
    def __init__(self, screen, width, height, field_array):
        screen.fill("green")
        font = pygame.font.Font(None, 48)        
        welcome = font.render("Welcome to the Shop", True, "Black")
        screen.blit(welcome, (width/4,80))
        pygame.display.flip()
        self.pack1 = random.randint(1,3)
        self.pack2 = random.randint(1,3)
        self.col_array = ["Blue", "Purple", "Brown"]
        self.rect_pack1 = pygame.Rect(width - (width/4) + 20, height - (height/4) + 20, 100, 200)
        self.pack_col1 = pygame.draw.rect(screen, self.col_array[self.pack1 - 1], self.rect_pack1)
        self.rect_pack2 = pygame.Rect(width - (width/8) + 20, height - (height/4) + 20, 100, 200)
        self.pack_col2 = pygame.draw.rect(screen, self.col_array[self.pack2 - 1], self.rect_pack1)
        
        for event in pygame.event.get():  
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.position = pygame.mouse.get_pos()
                if self.rect_pack1.collidepoint(self.position):
                    if self.pack1 == 1:
                        choice = "Plan"
                    if self.pack1 == 2:
                        choice = "Tarot"
                    if self.pack1 == 3:
                        choice = "Card"
                    Pack(choice, width, height, field_array)
                if self.rect_pack2.collidepoint(self.position):
                    if self.pack2 == 1:
                        choice = "Plan"
                    if self.pack2 == 2:
                        choice = "Tarot"
                    if self.pack2 == 3:
                        choice = "Card"
                    Pack(choice, width, height, field_array)