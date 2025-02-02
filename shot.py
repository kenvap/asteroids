import pygame # type: ignore
from circleshape import CircleShape
from constants import * # noqa: F403

class Shot(CircleShape):
    def __init__(self, x, y, radius, velocity):
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(velocity)  # Ensure velocity is always a Vector2

    def draw(self, screen):
        color = (255, 255, 255)  # White color
        line_width = 2
        pygame.draw.circle(screen, color, (int(self.position.x), int(self.position.y)), self.radius, line_width)

    def update(self, dt):
        self.position += self.velocity * dt