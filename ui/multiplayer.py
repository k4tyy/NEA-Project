import pygame

def multiplayer_game():
    screen = pygame.display.set_mode((1000,900))

    pygame.display.set_caption("Pac-Man")

    screen.fill((34,34, 77))

    font = pygame.font.Font("assets/fonts/PixelOperatorMono8-Bold.ttf", 50)

    text = font.render("MULTIPLAYER", True, "white")
    screen.blit(text, (100, 450))

    pygame.display.flip()