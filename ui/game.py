import sys
import pygame

#paused tab creation
def pause_game():
    pause_tab = pygame.Rect((screen.get_width() - 700) // 2, (screen.get_height() - 620) // 2, 700, 620)
    pygame.draw.rect(screen, "white", pause_tab)

#making map grid
def draw_grid():
  block_size = ""

#game function to run the game
def game():
    #pygame.init()

    global screen
    screen = pygame.display.set_mode((1000,900))

    pygame.display.set_caption("Pac-Man")

    screen.fill((34,34, 77))

    current_score = "0"
    high_score = "0"
    lives = 3

    font = pygame.font.Font("assets/fonts/PixelOperatorMono8-Bold.ttf", 25)
    
    current_score_text = font.render("CURRENT SCORE: " + current_score, True, "white")
    screen.blit(current_score_text, (0, 5))

    high_score_text = font.render("HIGH SCORE: " + high_score, True, "white")
    screen.blit(high_score_text, (660, 5))

    heart1 = pygame.image.load("assets/pngs/red_heart.png").convert_alpha()
    heart1 = pygame.transform.scale(heart1, (heart1.get_width() * 2.5, heart1.get_height() * 2.5))

    heart2 = pygame.image.load("assets/pngs/red_heart.png").convert_alpha()
    heart2 = pygame.transform.scale(heart2, (heart2.get_width() * 2.5, heart2.get_height() * 2.5))

    heart3 = pygame.image.load("assets/pngs/red_heart.png").convert_alpha()
    heart3 = pygame.transform.scale(heart3, (heart3.get_width() * 2.5, heart3.get_height() * 2.5))
    

    #draw hearts
    screen.blit(heart1, (10, 800))
    screen.blit(heart2, (90, 800))
    screen.blit(heart3, (170, 800))

    pygame.display.flip()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

    pygame.quit()