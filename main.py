import pygame
import sys
from enum import Enum, auto

import ui.PacManMenu
import ui.select_level
import ui.game
import ui.multiplayer
import ui.customise
from ui.ui_mode import ui_mode
   
#start pygame
pygame.init()

#set initial game state to menu
global game_state
game_state = ui_mode.MENU

#main loop
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if game_state == ui_mode.MENU:
            game_state = ui.PacManMenu.menu()
        elif game_state == ui_mode.SELECT_LEVEL:
            current_difficulty_level = ui.select_level.select_level_menu()
            game_state = ui_mode.GAME
        elif game_state == ui_mode.GAME:
            game_state = ui.game.game(current_difficulty_level)
        elif game_state == ui_mode.MULTIPLAYER:
            game_state = ui.customise.customise_game
        elif game_state == ui_mode.CUSTOMISE:
            game_state = ui.customise.customise_game()

pygame.quit()