import pygame
from constants import *
from logger import log_state
from player import Player

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}\r\nScreen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Create sprite groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    
    # Create player object
    player_object = Player((SCREEN_WIDTH // 2), (SCREEN_HEIGHT // 2))
    pygame.time.Clock()
    dt = 0
    
    # Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        log_state()
        # Create and fill background
        screen.fill("black")
        # Update and draw player object
        updatable.update(dt)
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()
        pygame.time.Clock().tick(60)
        dt = pygame.time.Clock().tick(60) / 1000.0

if __name__ == "__main__":
    main()
