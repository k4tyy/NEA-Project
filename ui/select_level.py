import sys
import pygame

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

#levels buttons functions
def easy_level(): 
    return "game"
    return "easy"

def medium_level():
    return "medium"

def hard_level():
    return "hard"

def select_level_menu():
    #set up window
    screen = pygame.display.set_mode((1000,900))
    
    pygame.display.set_caption("Pac-Man")

    screen.fill((34,34, 77))

    clock = pygame.time.Clock()

    #buttons size and position and function
    easy_button = Button((screen.get_width() - 440) // 2, 120, 440, 160, "EASY", easy_level)
    medium_button = Button((screen.get_width() - 440) // 2, 320, 440, 160, "MEDIUM", medium_level)
    hard_button = Button((screen.get_width() - 440) // 2, 520, 440, 160, "HARD", hard_level)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                selected_level = easy_button.clicked(event.pos)
                if selected_level:
                    return selected_level
                selected_level = medium_button.clicked(event.pos)
                if selected_level:
                    return selected_level
                selected_level = hard_button.clicked(event.pos)
                if selected_level:
                    return selected_level
                
        #draw buttons
        pygame.draw.rect(screen, (226, 171, 94), easy_button.rect)
        pygame.draw.rect(screen, (226, 171, 94), medium_button.rect)
        pygame.draw.rect(screen, (226, 171, 94), hard_button.rect)

        #set font
        font = pygame.font.Font("assets/fonts/PixelOperatorMono8-Bold.ttf", 60)

        #buttons text

        #EASY button
        if easy_button.rect.collidepoint(pygame.mouse.get_pos()):
            text = font.render("EASY", True, "white")
        else:
            text = font.render("EASY", True, (34, 34, 77))

        text_rect = text.get_rect(center=easy_button.rect.center)
        screen.blit(text, text_rect)

        #MEDIUM button 
        if medium_button.rect.collidepoint(pygame.mouse.get_pos()):
            text = font.render("MEDIUM", True, "white")
        else:
            text = font.render("MEDIUM", True, (34, 34, 77))

        text_rect = text.get_rect(center=medium_button.rect.center)
        screen.blit(text, text_rect)

        #HARD button
        if hard_button.rect.collidepoint(pygame.mouse.get_pos()):
            text = font.render("HARD", True, "white")
        else:
            text = font.render("HARD", True, (34, 34, 77))

        text_rect = text.get_rect(center=hard_button.rect.center)
        screen.blit(text, text_rect)

        pygame.display.flip()
        clock.tick(60)


# def pacman(level):
#    play_screen = pygame.Rect((screen.get_width() - 800) // 2, (screen.get_height() - 700) // 2, 800, 700)
#    pygame.draw.rect(screen, (69,75,145), play_screen)

    #if level == "easy":
        #easy pacman
    #elif level == "medium":
        #medium pacman
    #else:
        #hard pacman