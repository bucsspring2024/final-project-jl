from src.pack import Pack
import pygame
import random
class Shop:
    def __init__(self, screen, width, height, field_array, procced_planets, money):
        screen.fill("green")
        choice = ""
        font = pygame.font.Font(None, 48)        
        welcome = font.render("Welcome to the Shop", True, "Black")
        screen.blit(welcome, (width/4,80))
        self.leave_rect = pygame.Rect(0, height/2 - 50, 300, 300)
        pygame.draw.rect(screen, "Purple", self.leave_rect)
        leave = font.render("Click to leave", True, "Black")
        screen.blit(leave, (50, (height/2) + 100))
        pygame.display.flip()
        self.pack1 = random.randint(1,3)
        self.pack2 = random.randint(1,3)
        pack1_choose = False
        pack2_choose = False
        self.col_array = ["Blue", "Purple", "Brown"]
        self.price = 10
        self.money = money
        price = font.render("Price:" + str(self.price), True, "Black")
        currency = font.render("Current total money:" + str(self.money), True, "Black")
        screen.blit(currency, (0,0))
        self.rect_pack1 = pygame.Rect(width - (width/4) + 20, height - (height/2) + 20, 400, 600)
        self.rect_pack2 = pygame.Rect(width - (width/2) + 20, height - (height/2) + 20, 400, 600)
        Buying = True

        while Buying:
            if pack1_choose == False:
                self.pack_col1 = pygame.draw.rect(screen, self.col_array[self.pack1 - 1], self.rect_pack1)
                screen.blit(price,(width - (width/4) + 20, height - (height/2) + 20))
            if pack2_choose == False:
                self.pack_col2 = pygame.draw.rect(screen, self.col_array[self.pack2 - 1], self.rect_pack2)
                screen.blit(price,(width - (width/2) + 20, height - (height/2) + 20))
            pygame.display.flip()
            for event in pygame.event.get():  
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.position = pygame.mouse.get_pos()
                    if self.rect_pack1.collidepoint(self.position) and self.money > self.price:
                        self.money -= self.price
                        pack1_choose = True
                        if self.pack1 == 1:
                            choice = "Plan"
                        if self.pack1 == 2:
                            choice = "Tarot"
                        if self.pack1 == 3:
                            choice = "Card"
                        
                        Pack(choice, screen, width, height, field_array, procced_planets)
                        pygame.display.flip()

                    if self.rect_pack2.collidepoint(self.position):
                        pack2_choose = True
                        if self.pack2 == 1:
                            choice = "Plan"
                        if self.pack2 == 2:
                            choice = "Tarot"
                        if self.pack2 == 3:
                            choice = "Card"
                        
                        Pack(choice, screen, width, height, field_array, procced_planets)
                        pygame.display.flip()
                        

                    if self.leave_rect.collidepoint(self.position):
                        Buying = False
    
    def get_money(self):
        return self.money