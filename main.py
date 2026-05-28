import pygame
from os.path import join
from random import randint

# General Setup
pygame.init() 
WIDTH = 1280
HEIGHT = 720

display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Space Shooter')
running = True
clock = pygame.time.Clock()

# Create plain surface
surf = pygame.Surface(( 100, 200 ))
surf.fill('orange')
x = 100

# Player
player_surf = pygame.image.load(join('sprites', 'player.png')).convert_alpha()
player_rect = player_surf.get_frect(center = (WIDTH / 2, HEIGHT / 2))
player_direction = pygame.math.Vector2(1, 0)
player_speed = 100

# Stars
star_surf = pygame.image.load(join('sprites', 'star.png')).convert_alpha()
star_positions = [(randint(0, WIDTH), randint(0, HEIGHT)) for i in range(20)]

# Asteroid
asteroid_surf = pygame.image.load(join('sprites', 'asteroid.png')).convert_alpha()
asteroid_rect = asteroid_surf.get_frect(center = (WIDTH / 2, HEIGHT / 2))

# Laser
laser_surf = pygame.image.load(join('sprites', 'laser.png')).convert_alpha()
laser_rect = laser_surf.get_frect(bottomleft = (20, HEIGHT - 20))

# Drawing Screen
while running:

    dt = clock.tick() / 1000
    
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # draw the game, drawing matters in lines, display background first, then stars, then ship
    display_surface.fill('darkgray')

    for pos in star_positions:
        display_surface.blit(star_surf, pos)

    display_surface.blit(asteroid_surf, asteroid_rect)
    display_surface.blit(laser_surf, laser_rect)

    # Player Movement
    player_rect.center += player_direction * player_speed * dt
    display_surface.blit(player_surf, player_rect)

    pygame.display.update()

pygame.quit()