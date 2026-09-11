import pygame
import sys

import ui.PacManMenu
import ui.select_level
import ui.game
import ui.multiplayer
import ui.customise

#start pygame
pygame.init()

#set initial game state to menu
global game_state
game_state = "menu"

#main loop
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if game_state == "menu":
            game_state = ui.PacManMenu.menu()
        elif game_state == "select_level":
            game_state = ui.select_level.select_level_menu()
        elif game_state == "game":
            game_state = ui.game.game()
        elif game_state == "multiplayer":
            game_state = ui.customise.customise_game
        elif game_state == "customise":
            game_state = ui.customise.customise_game()

pygame.quit()