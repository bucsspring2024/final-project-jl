from src.deck import Deck
from src.hand import Hand
from src.total_math import Math
from src.planet import Planet
from src.pack import Pack
from src.tarot import Tarot
from src.shop import Shop
import pygame

class Controller:
    def __init__(self):
        """
        docstring
        """
        self.screen = pygame.display.set_mode()
        self.width, self.height = pygame.display.get_window_size()
        self.screen.fill("white")

    def mainloop(self, screen, width, height):
        while(True):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                self.field_wid = int(width/4)
                self.field_height = int(height/4)
                self.field_rect = pygame.Rect(int(width - (width/5)), 0, int(self.field_wid), int(self.field_height))

                self.deck = Deck(self.field_wid, self.field_height)
                self.draw = 8
                self.money = 0 
                self.joker_money = 0
                self.field_array = []
                self.current_hand = []
                self.hand_field = []
                self.chips_to_win = 0
                self.current_chips = 0
                self.chosen_hand = []


                self.open_game()
                
                self.round_start()
                self.play_loop()

                
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.position = pygame.mouse.get_pos()
                    if self.current_hand.img.collidepoint(self.position):
                        for i in range(self.draw):
                            self.chosen_hand.append[i]
                if len(self.chosen_hand) == 5:
                    self.hand = Hand(self.chosen_hand)

                #self.tarot_proc()

                self.current_shop = Shop(screen, width, height, self.field_array)

                exit()

    def round_start(self):
        self.chips_to_win += 200
        self.deck.shuffle()

    def open_game(self):
        starting = True
        while starting:
            font = pygame.font.Font(None, 48)        
            welcome = font.render("Welcome to Jalatro", True, "Red")
            begin = font.render("Click to begin", True, "Red")
            self.screen.blit(begin, ((self.width/2) - 150, (self.height/2)))
            self.screen.blit(welcome, ((self.width/2) - 200, (self.height/2) - 100))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    starting = False

    def play_loop(self):
        playing = True
        self.screen.fill("Purple")
        self.field = pygame.draw.rect(self.screen, "black", self.field_rect)
        pygame.display.flip()
        self.deck.shuffle()
        while playing:
            for i in range(self.draw):
                self.current_hand.append(self.deck.pull_card(i))
                self.deck.top = self.height - (self.height / 4)
                self.deck.left = (self.width/8) + ((self.width/8)*i)
                self.deck.placement(self.deck.top, self.deck.left)
                self.drawn_cards = pygame.draw.rect(self.screen, "brown", self.deck.pull_card(i).img)
                pygame.display.flip()
            if self.chips_to_win < self.current_chips:
                playing = False


    def tarot_proc(self):
        while(True):
            self.tarot_card_list = []
            for event in pygame.event.get():  
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.position = pygame.mouse.get_pos()
                    for i in range(self.draw):
                        if self.current_hand[i].img.collidepoint(self.position):
                            self.tarot_card_list.clear()
                            self.tarot_card_list.append(self.hand[i])
                    for i in len(self.field_array):
                        if self.field_array[i].rect.collidepoint(self.position):
                            Tarot.run_Tarot(self.field_array[i], self.field_array[i].name, self.tarot_card_list)