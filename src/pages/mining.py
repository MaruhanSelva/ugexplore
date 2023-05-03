import pygame
import sys
import os
from pygame.locals import *
from src.modules.mininghelpers import MiningBoard
from src.modules.tile import Tile
from src.modules.button import Button
from src.pages.ending import win, lose


GRAY_COL = (128,128,128)
BEIGE_COL = (255,228,196)
BROWN_COL = (139,69,19)
DEFAULT_IMAGE_SIZE = (100, 100)

ROCK = pygame.image.load("assets/images/rocks.jpg")
DIRT = pygame.image.load("assets/images/dirt.png")
SAND = pygame.image.load("assets/images/sandy.jpg")

RESIZEROCK = pygame.transform.scale(ROCK, DEFAULT_IMAGE_SIZE)
RESIZEDIRT = pygame.transform.scale(DIRT, DEFAULT_IMAGE_SIZE)
RESIZESAND = pygame.transform.scale(SAND, DEFAULT_IMAGE_SIZE)

chisel_pic = pygame.image.load("assets/images/chisel.png")
resizec = pygame.transform.scale(chisel_pic, DEFAULT_IMAGE_SIZE)
hammer_pic = pygame.image.load("assets/images/mallet.png")
resizeh = pygame.transform.scale(hammer_pic, DEFAULT_IMAGE_SIZE)
back_pic = pygame.image.load("assets/images/back.png")
resizeb = pygame.transform.scale(back_pic, (50, 50))

ogem = pygame.image.load("assets/images/ogem.png")
ogem_big = pygame.transform.scale(ogem, DEFAULT_IMAGE_SIZE)
ggem = pygame.image.load("assets/images/ggem.png")
ggem_big = pygame.transform.scale(ggem, DEFAULT_IMAGE_SIZE)

treasures = [ogem_big, ggem_big, ogem_big, ggem_big]



def mining(screen, wins):
    from src.pages.menu import main_menu

    running = True
    
    screen.fill((130, 93, 73))

    size = 6
    treasure = 4

    m = MiningBoard(size)
    m.place_treasure(treasure)

    pygame.draw.rect(screen, (128, 0, 0), pygame.Rect(315, 35, 650, 650))
    pygame.draw.rect(screen, (184, 115, 51), pygame.Rect(320, 40, 640, 640))
    pygame.draw.rect(screen, (149, 69, 53), pygame.Rect(340, 60, 600, 600))

    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(20, 20, 60, 60))
    pygame.draw.rect(screen, (255,255,255), pygame.Rect(25, 25, 50, 50))

    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(995, 190, 110, 110))
    pygame.draw.rect(screen, (135,206,250), pygame.Rect(1000, 195, 100, 100))

    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(995, 410, 110, 110))
    pygame.draw.rect(screen, (220,20,60), pygame.Rect(1000, 415, 100, 100))

    HAMMER = True

    tr = m.get_treasures()
    t_dict = {}
    
    for i in range(0, treasure):
        t_dict[tr[i]] = treasures[i]
    

    while running:
        tr_count = 0

        MOUSE_POS = pygame.mouse.get_pos()

        # Back Button
        back_button = Button(resizeb, (50, 50), "", font=pygame.font.Font("assets/fonts/BlockOutline.ttf", 70), base_color="#d7fcd4", hovering_color="White")
        back_button.update(screen)

        # Hammer/Chisel Buttons
        hammer_button = Button(resizeh, (1050, 245), "", font=pygame.font.Font("assets/fonts/BlockOutline.ttf", 70), base_color="#d7fcd4", hovering_color="White")
        chisel_button = Button(resizec, (1050, 465), "", font=pygame.font.Font("assets/fonts/BlockOutline.ttf", 70), base_color="#d7fcd4", hovering_color="White")
        
        hammer_button.update(screen)
        chisel_button.update(screen)
        
        ## Render the Tiles/Layers
        tiles = []
        col = 0
        row = 0
        
        for i in range(size * size):
            if col == size:
                col = 0
                row = row + 1

            lval = 340 + col * 100
            tval = 60 + row * 100
            layer = m.getoutermostcell(row, col)

            if layer == 3:
                # Render the outermost layer
                t = Tile(RESIZEROCK, (lval + 50 , tval + 50))
                tiles.append(t)
                t.update(screen)
                # pygame.draw.rect(screen, GRAY_COL, pygame.Rect(lval, tval, 75, 75))
            elif layer == 2:
                t = Tile(RESIZESAND, (lval + 50 , tval + 50))
                tiles.append(t)
                t.update(screen)
                #pygame.draw.rect(screen, BEIGE_COL, pygame.Rect(lval, tval, 100, 100))
            elif layer == 1:
                
                if i in tr:
                    pic = t_dict[i]
                    t = Tile(RESIZEDIRT, (lval + 50, tval + 50))
                    t.update(screen)
                    t = Tile(pic, (lval + 50 , tval + 50))
                    tr_count = tr_count + 1
                else:
                    t = Tile(RESIZEDIRT, (lval + 50, tval + 50))

                tiles.append(t)
                t.update(screen)
                # pygame.draw.rect(screen, BROWN_COL, pygame.Rect(lval, tval, 100, 100))
                
            col = col + 1

        
        # Game Ending Conditions
        if tr_count == treasure:
            wins = wins + 1
            win(screen, wins)
        
        if m.get_dmg() >= 100:
            lose(screen, wins)

        
        # Event Handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # check if a tile was chosen
                for i in range(len(tiles)):
                    if tiles[i].checkForInput(MOUSE_POS):
                        x_val = i // size 
                        y_val = i - (size * x_val)
                        if HAMMER == True:
                            m.hammer(x_val, y_val)
                        else:
                            m.chisel(x_val, y_val)
                
                if hammer_button.checkForInput(MOUSE_POS):
                    HAMMER = True
                elif chisel_button.checkForInput(MOUSE_POS):
                    HAMMER = False
                elif back_button.checkForInput(MOUSE_POS):
                    main_menu(screen, wins)

                
        pygame.display.update()