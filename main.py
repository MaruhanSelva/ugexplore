import pygame
import sys
import os
from pygame.locals import *
from src.pages.menu import main_menu


# Initialize pygame
pygame.init()

# Initialize Screen
screen = pygame.display.set_mode((1000, 720))

# Title and Icon
pygame.display.set_caption("Underground Explorers")
icon = pygame.image.load("assets/images/mining.png")
pygame.display.set_icon(icon)

# Main Menu Initiate
main_menu(screen, 0)







