import pygame

# General Setup
pygame.init() 
WIDTH = 1280
HEIGHT = 720

display_surace = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Space Shooter')
running = True

# Create surface
surf = pygame.Surface(( 100, 200 ))

# Drawing Screen
while running:
    
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # draw the game
    display_surace.fill('darkgray')
    display_surace.blit(surf)
    pygame.display.update()

pygame.quit()