import pygame
from controller import GameController

def main():
    pygame.init()
    game_controller = GameController()
    game_controller.run()
    
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######

# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    main()
