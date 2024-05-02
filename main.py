import pygame
from src.controller import Controller
#import your controller

def main():
    pygame.init()
    cont = Controller()
    #Create an instance on your controller object
    screen = cont.screen
    width = cont.width
    height = cont.height
    cont.mainloop(screen, width, height)
    #Call your mainloop
    
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######

# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    main()
