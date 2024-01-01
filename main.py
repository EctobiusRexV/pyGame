# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
clock = pygame.time.Clock()
running = True
surfaces = {}

for i in range(10):
    surfaces[i] = pygame.display.set_mode((1280, 720))


current_level = 0

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    surfaces[current_level].fill(pygame.Color(10, 138, 1))
    # pygame.draw.rect(surfaces[current_level], pygame.Color(0, 0, 0), pygame.Rect(300, 300, 60, 60))
    pygame.draw.rect(surfaces[current_level], pygame.Color(50, 50, 50), pygame.Rect(0, 0, 50, 260))
    pygame.draw.rect(surfaces[current_level], pygame.Color(50, 50, 50), pygame.Rect(0, 0, 500, 50))
    pygame.draw.rect(surfaces[current_level], pygame.Color(50, 50, 50), pygame.Rect(780, 0, 500, 50))
    pygame.draw.rect(surfaces[current_level], pygame.Color(50, 50, 50), pygame.Rect(1230, 0, 50, 260))
    pygame.draw.rect(surfaces[current_level], pygame.Color(50, 50, 50), pygame.Rect(1230, 0, 50, 260))
    pygame.draw.rect(surfaces[current_level], pygame.Color(50, 50, 50), pygame.Rect(0, 540, 50, 260))
    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
