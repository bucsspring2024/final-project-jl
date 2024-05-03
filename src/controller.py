from src.deck import Deck
from src.hand import Hand
from src.total_math import Total_Math
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
        self.round_number = 0
        self.max_chips = 0
        self.draw = 8
        self.money = 0 
        self.joker_money = 0
        self.chips_to_win = 0
        self.field_array = []
        self.fail = False
        self.procced_planets = [0,0,0,0,0,0,0,0,0,0,0,0]
        while(True):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                self.field_wid = int(width/4)
                self.field_height = int(height/4)
                self.field_rect = pygame.Rect(int(width - (width/5)), 0, int(self.field_wid), int(self.field_height))

                self.deck = Deck(self.field_wid, self.field_height)

                self.current_hand = []
                self.current_chips = 0
                
                
                if self.round_number == 0:
                    self.open_game()
                
                self.round_number += 1
                
                self.round_start()
                
                self.play_loop()
                pygame.time.wait(2000)
                if self.fail == True:
                    self.game_over()
                    exit()
                
                self.money += 10
                
                self.current_shop = Shop(screen, width, height, self.field_array, self.procced_planets, self.money)
            
        
                #self.tarot_proc()

                

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
        self.hand_array = []
        self.drawn_cards = []

        self.held_hand = []
        self.hand_size = 0
        self.attempts = 5
        self.clicked_rects = []
        while playing:
                
                self.rect_list = []
                self.card_chips = 0
                for i in range(self.draw):
                    self.hand_array.append(self.deck.pull_card(i))
                    if len(self.deck.cards) == 0 or self.attempts == 0:
                        self.fail = True
                        playing = False
                        
                    self.left = ((self.width/8)*i) + 50
                    self.top = self.height - (self.height / 4)
                    self.hand_array[i].img = pygame.Rect(self.left, self.top, self.field_wid/3, self.field_height - 20)
                    self.drawn_cards.append(self.hand_array[i])
                    self.rect_draw = pygame.draw.rect(self.screen, "brown", self.hand_array[i].img)
                    self.rect_list.append(self.rect_draw)
                    font = pygame.font.Font(None, 48)
                    self.suit_col = ""
                    if self.hand_array[-1].suit == "Clubs" or self.hand_array[-1].suit == "Spades":
                        self.suit_col = "Black"
                    if self.hand_array[-1].suit == "Hearts" or self.hand_array[-1].suit == "Diamonds":
                        self.suit_col = "Red"
                    
                    self.value = font.render(str(self.hand_array[-1].name_current), True, self.suit_col)
                    self.suit = font.render(str(self.hand_array[-1].suit), True, self.suit_col)
                    self.screen.blit(self.value, (self.hand_array[-1].img))
                    self.screen.blit(self.suit, (self.hand_array[-1].img.left,self.hand_array[-1].img.top + 50))

                    pygame.display.flip()
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.position = pygame.mouse.get_pos()
                        print("rect_list" + str(self.rect_list))
                        print("held hand" + str(self.held_hand))
                        for i in range(len(self.rect_list)):
                            if self.rect_list[i].collidepoint(self.position) and self.rect_list[i] not in self.clicked_rects:
                                self.drawn_cards[i].img.top -= self.height / 2
                                self.held_hand.append(self.drawn_cards[i])
                                self.hand_size += 1
                                print(self.hand_size)
                                self.hand_array.remove(self.drawn_cards[i])
                                pygame.draw.rect(self.screen, "brown", self.held_hand[-1].img)
                                
                                if self.held_hand[-1].suit == "Clubs" or self.held_hand[-1].suit == "Spades":
                                    self.suit_col = "Black"
                                if self.held_hand[-1].suit == "Hearts" or self.held_hand[-1].suit == "Diamonds":
                                    self.suit_col = "Red"
                                self.value = font.render(str(self.held_hand[-1].name_current), True, self.suit_col)
                                self.suit = font.render(str(self.held_hand[-1].suit), True, self.suit_col)
                                self.screen.blit(self.value, (self.held_hand[-1].img))
                                self.screen.blit(self.suit, (self.held_hand[-1].img.left,self.held_hand[-1].img.top + 50))
                                self.clicked_rects.append(self.rect_list[i])

                        pygame.display.flip()
                        if self.hand_size == 5:
                            break
                if self.hand_size == 5:
                    self.hand = Hand(self.held_hand,self.procced_planets)
                    for i in range(len(self.hand.hand)):
                        self.card_chips += Hand.chips_count(self.hand.hand[i])
                    self.hand_chips = self.hand.chips_count() + self.card_chips
                    self.hand_mult = self.hand.mult_count()
                    
                    self.val = Total_Math(self.hand.chips_count(), self.hand.mult_count())
                    self.val.add_cards(self.hand_chips, self.hand_mult)
                    self.current_chips += self.val.total()
                    if self.val.total() < self.max_chips:
                        self.max_chips = self.val.total()
                if self.hand_size == 5:
                    self.cover_score = pygame.Rect(0,0,400,100)
                    pygame.draw.rect(self.screen, "purple", self.cover_score)
                    self.hand_played = font.render("Hand played: " + str(self.hand.hand_name), True, "Blue")
                    self.screen.blit(self.hand_played, (700, 100))
                font = pygame.font.Font(None, 48)        
                self.score = font.render("Current score: " + str(self.current_chips), True, "Red")
                self.score_needed = font.render("Score to win current round: " + str(self.chips_to_win), True, "Red")
                self.attempted = font.render("Attempts left: " + str(self.attempts), True, "Red")
                self.rounds = font.render("Round: " + str(self.round_number), True, "Red")
                self.screen.blit(self.score, (0, 0))
                self.screen.blit(self.score_needed, (0, 100))
                self.screen.blit(self.attempted, (0, 200))
                self.screen.blit(self.rounds, (0, 300))
                self.deck_len = font.render("Remaining cards in deck: " + str(len(self.deck.cards)), True, "Red")
                self.screen.blit(self.deck_len, (400, 0))

                self.hand_array.clear()
                pygame.display.flip()

                if self.hand_size == 5:
                    self.cover = pygame.Rect(0,0,1300,300)
                    pygame.draw.rect(self.screen, "purple", self.cover)
                    self.card_reset = pygame.Rect(0, self.height/4, self.width, self.height/2 + self.height/4)
                    pygame.time.wait(2000)
                    self.hand_size = 0
                    self.hand_array.clear()
                    self.rect_list.clear()
                    self.held_hand.clear()
                    self.drawn_cards.clear()
                    self.clicked_rects.clear()
                    pygame.draw.rect(self.screen, "purple", self.card_reset)
                    for q in range(8):
                        self.deck.cards.remove(self.deck.pull_card(q))
                    self.attempts -= 1

                

                if self.chips_to_win <= self.current_chips:
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

    def game_over(self):
        self.screen.fill("Black")
        fileref = open("highscore.txt")
        if int(fileref.read()) < self.max_chips:
            fileref = open("highscore.txt", 'w')
            fileref.write(str(self.max_chips))
            fileref.close()
        font = pygame.font.Font(None, 100)
        game_over = font.render("Game Over", True, "Red")
        highscore = font.render("You made it to round: " + str(self.round_number), True, "Red")
        highscore_chips = font.render("Largest amount of chips in one hand: " + str(self.max_chips), True, "Red")
        overall_highscore = font.render("Best hand of all games: " + fileref.read(), True, "Red")
        self.screen.blit(game_over, ((self.width/2) - 150, (self.height/2)))
        self.screen.blit(highscore, ((self.width/2) - 150, (self.height/2) + 200))
        self.screen.blit(highscore_chips, ((self.width/2) - 150, (self.height/2) + 400))
        self.screen.blit(overall_highscore, ((self.width/2) - 150, (self.height/2) + 600))
        pygame.display.flip()
        pygame.time.wait(5000)