import sys
import pygame


pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
bg_surf = pygame.image.load("./graphics/background.png").convert()
pygame.display.set_caption("Meteor shooter")



# test_surface = pygame.Surface((200, 100))
# relative root folder
ship_surf = pygame.image.load("./graphics/ship.png").convert_alpha() 


# import text
font = pygame.font.Font("./graphics/subatomic.ttf", 50)
# True = AntiAliasing
text_surf = font.render("Space", True, (255, 255, 255))

# Attach to the display surface 
# By def, all surfaces are black. Blit (block image transfer): d_s.blit(surface, position)


while True: 
    # Check for input -> events (nouse click/movement, button press)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update the game

    display_surface.fill((200, 200, 200))
    display_surface.blit(bg_surf, (0, 0))
    display_surface.blit(ship_surf, (200, 400))
    display_surface.blit(text_surf, (500, 200))
    # test_surface.fill((255, 191, 0))
    # display_surface.blit(test_surface, (WINDOW_WIDTH - test_surface.get_width(), 80))
    # Show the frame to the player / update the display surface (ca)
    pygame.display.update()

