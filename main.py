import pygame
from constants import *
from logger import log_state

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}\r\nScreen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.time.Clock()
    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        log_state()
        screen.fill("black")
        pygame.display.flip()
        pygame.time.Clock().tick(60)
        dt = pygame.time.Clock().tick(60) / 1000.0

if __name__ == "__main__":
    main()
