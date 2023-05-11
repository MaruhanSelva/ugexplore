import pygame
import sys
import os
from pygame.locals import *

from src.modules.button import Button

def win(screen, wins, endless):
    from src.pages.mining import mining
    from src.pages.menu import main_menu

    running = True

    screen.fill((0,255,127))

    while running:

        MOUSE_POS = pygame.mouse.get_pos()

        ENDING_TEXT = pygame.font.Font("assets/fonts/Block.ttf", 80).render("you won", True, "#F2EDA7")
        ENDING_RECT = ENDING_TEXT.get_rect(center=(640, 200))

        REPLAY_BUTTON = Button(image=pygame.image.load("assets/images/PlayRect.png"), pos=(640, 400), 
                            text_input="replay", font=pygame.font.Font("assets/fonts/BlockOutline.ttf", 70), base_color="#d7fcd4", hovering_color="White")

        MENU_BUTTON = Button(image=pygame.image.load("assets/images/PlayRect.png"), pos=(640, 550), 
                            text_input="menu", font=pygame.font.Font("assets/fonts/BlockOutline.ttf", 70), base_color="#d7fcd4", hovering_color="White")

        REPLAY_BUTTON.changeColor(MOUSE_POS)
        REPLAY_BUTTON.update(screen)

        MENU_BUTTON.changeColor(MOUSE_POS)
        MENU_BUTTON.update(screen)

        screen.blit(ENDING_TEXT, ENDING_RECT)


        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if REPLAY_BUTTON.checkForInput(MOUSE_POS):
                        mining(screen, wins, endless)
                    
                    if MENU_BUTTON.checkForInput(MOUSE_POS):
                         main_menu(screen, 0)

                    
        pygame.display.update()

def lose(screen, wins, endless):
    from src.pages.mining import mining
    from src.pages.menu import main_menu

    running = True

    screen.fill((178,34,34))

    while running:

        MOUSE_POS = pygame.mouse.get_pos()

        ENDING_TEXT = pygame.font.Font("assets/fonts/Block.ttf", 80).render("the mine collapsed", True, "#000000")
        ENDING_RECT = ENDING_TEXT.get_rect(center=(640, 200))

        REPLAY_BUTTON = Button(image=pygame.image.load("assets/images/PlayRect.png"), pos=(640, 400), 
                            text_input="replay", font=pygame.font.Font("assets/fonts/BlockOutline.ttf", 70), base_color="#000000", hovering_color="White")

        MENU_BUTTON = Button(image=pygame.image.load("assets/images/PlayRect.png"), pos=(640, 550), 
                            text_input="menu", font=pygame.font.Font("assets/fonts/BlockOutline.ttf", 70), base_color="#000000", hovering_color="White")

        REPLAY_BUTTON.changeColor(MOUSE_POS)
        REPLAY_BUTTON.update(screen)

        MENU_BUTTON.changeColor(MOUSE_POS)
        MENU_BUTTON.update(screen)

        screen.blit(ENDING_TEXT, ENDING_RECT)


        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if REPLAY_BUTTON.checkForInput(MOUSE_POS):
                        mining(screen, wins, endless)
                    
                    if MENU_BUTTON.checkForInput(MOUSE_POS):
                        main_menu(screen, 0)

                    
        pygame.display.update()