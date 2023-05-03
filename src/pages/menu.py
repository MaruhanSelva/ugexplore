import pygame
import sys
import os
from pygame.locals import *
from src.pages.mining import mining

from src.modules.button import Button

mine = pygame.image.load("assets/images/mine.png")
BACKGROUND_IMG = pygame.transform.scale(mine, (1280, 720))

def main_menu(screen, wins):
    running = True

    screen.fill((0, 0, 0))

    while running:
        screen.blit(BACKGROUND_IMG, (0,0))


        MENU_MOUSE_POS = pygame.mouse.get_pos()


        MENU_TEXT = pygame.font.Font("assets/fonts/Block.ttf", 80).render("underground explorers", True, "#F2EDA7")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 200))

        
        PLAY_BUTTON = Button(image=pygame.image.load("assets/images/PlayRect.png"), pos=(640, 400), 
                             text_input="play", font=pygame.font.Font("assets/fonts/BlockOutline.ttf", 70), base_color="#d7fcd4", hovering_color="White")
        

        screen.blit(MENU_TEXT, MENU_RECT)

        PLAY_BUTTON.changeColor(MENU_MOUSE_POS)
        PLAY_BUTTON.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    ## PLAY SCREEN
                    print("Hello")
                    mining(screen, wins)
            
                    


        pygame.display.update()
        



