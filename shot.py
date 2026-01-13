import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS, LINE_WIDTH, SCREEN_WIDTH, SCREEN_HEIGHT

class Shot(CircleShape):
    def __init__(self, position, velocity):
        super().__init__(position.x, position.y, SHOT_RADIUS)
        self.velocity = velocity

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, SHOT_RADIUS, width=LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt
        # Remove shot if it goes off screen
        if (self.position.x < 0 or self.position.x > SCREEN_WIDTH or
                self.position.y < 0 or self.position.y > SCREEN_HEIGHT):
            self.kill()