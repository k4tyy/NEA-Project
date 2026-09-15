import pygame

from ui.ui_mode import ui_mode

#button class for menu buttons
class Button:
    def __init__(self, x, y, width, height, text, function):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = pygame.font.Font("assets/fonts/PixelOperatorMono8-Bold.ttf", 50)
        self.function = function

    def clicked(self, mouse_pos):
        if self.is_clicked(mouse_pos):
            return self.function()

    def is_clicked(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            return self.function()

#states functions called by buttons
def select_level():
    return ui_mode.SELECT_LEVEL

def multiplayer_game():
    return ui_mode.MULTIPLAYER

def customise_game():
    return ui_mode.CUSTOMISE


#menu subroutine
def menu():
    #open window and set size and tab name
    screen = pygame.display.set_mode((1000,900))

    pygame.display.set_caption("Pac-Man")

    #buttons
    play_button = Button((screen.get_width() - 280) // 2, 320, 280, 180, "PLAY", select_level)
    multiplayer_button = Button((screen.get_width() - 600) // 2, 550, 600, 100, "MULTIPLAYER", multiplayer_game)
    customise_button = Button((screen.get_width() - 500) // 2, 700, 500, 100, "CUSTOMISE", customise_game)

    #font = pygame.font.Font("assets/fonts/PixelOperatorMono8-Bold.ttf", 50)
    clock = pygame.time.Clock()

    global running
    running = True

    #main loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                new_state = play_button.clicked(event.pos)
                if new_state:
                    return new_state
                new_state = multiplayer_button.clicked(event.pos)
                if new_state:
                    return new_state
                new_state = customise_button.clicked(event.pos)
                if new_state:
                    return new_state

            # game_state = globals().get('game_state', None)
            # if game_state == "game":
            #     return "game"

            # game_state = globals().get('game_state', None)
            # if game_state == "customise":
            #     return "customise"

        #set background colour
        screen.fill((34,34, 77))

        #buttons on menu screen
        pygame.draw.rect(screen, (226, 171, 94), play_button.rect)
        pygame.draw.rect(screen, (34, 34, 77), multiplayer_button.rect)
        pygame.draw.rect(screen, (34, 34, 77), customise_button.rect)

        font = pygame.font.Font("assets/fonts/PixelOperatorMono8-Bold.ttf", 70)

        #buttons

        #PLAY button
        if play_button.rect.collidepoint(pygame.mouse.get_pos()):
            text = font.render("PLAY", True, "white")
        else:
            text = font.render("PLAY", True, (34, 34, 77))

        text_rect = text.get_rect(center=play_button.rect.center)
        screen.blit(text, text_rect)
        
        font = pygame.font.Font("assets/fonts/PixelOperatorMono8-Bold.ttf", 50)

        #MULTIPLAYER button 
        if multiplayer_button.rect.collidepoint(pygame.mouse.get_pos()):
            text = font.render("MULTIPLAYER", True, "white")
        else:
            text = font.render("MULTIPLAYER", True, (226, 171, 94))

        text_rect = text.get_rect(center=multiplayer_button.rect.center)
        screen.blit(text, text_rect)

        if customise_button.rect.collidepoint(pygame.mouse.get_pos()):
            text = font.render("CUSTOMISE", True, "white")
        else:
            text = font.render("CUSTOMISE", True, (226, 171, 94))

        text_rect = text.get_rect(center=customise_button.rect.center)
        screen.blit(text, text_rect)

        pygame.display.flip()
        clock.tick(60)