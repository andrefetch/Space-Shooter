import pygame

# General Setup
pygame.init() 
WIDTH = 1280
HEIGHT = 720

display_surace = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Space Shooter')
running = True

# Create plain surface
surf = pygame.Surface(( 100, 200 ))
surf.fill('orange')
x = 100

# Importing Images
player_surf = pygame.image.load('sprites/ship.png')

# Drawing Screen
while running:
    
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # draw the game
    display_surace.fill('darkgray')
    x += 1
    display_surace.blit(surf, ( x, 150 ))
    pygame.display.update()

pygame.quit()