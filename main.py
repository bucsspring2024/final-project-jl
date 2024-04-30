import pygame
from functions import controller
#import your controller

def main():
    pygame.init()
    cont = controller
    #Create an instance on your controller object
    cont.Controller.mainloop(cont)
    #Call your mainloop
    
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######

# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    main()
