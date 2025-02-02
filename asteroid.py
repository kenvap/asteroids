import pygame
import random
from circleshape import CircleShape
from constants import * # noqa: F403

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        color = (255, 255, 255)  # White color
        line_width = 2
        pygame.draw.circle(screen, color, self.position, self.radius, line_width)

    def split(self):
        self.kill()
        if self.radius > ASTEROID_MIN_RADIUS:  # noqa: F405
            random_angle = random.uniform(20, 50)
            v1 = self.velocity.rotate(random_angle) * 1.2
            v2 = self.velocity.rotate(-random_angle) * 1.2
            new_radius = self.radius - ASTEROID_MIN_RADIUS  # noqa: F405
            splinter_1 = Asteroid(self.position.x, self.position.y, new_radius)
            splinter_2 = Asteroid(self.position.x, self.position.y, new_radius)
            #print(f"Number of sprites in group: {len(self.groups()[0])}")
            splinter_1.velocity = v1  # Set first asteroid's velocity
            splinter_2.velocity = v2  # Set second asteroid's velocity
            #return splinter_1, splinter_2  # Return the asteroid objects
        return None
        

    def update(self, dt):
        self.position += self.velocity * dt
        '''
        screen_rect = pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
        # Check if the asteroid is outside the screen
        if not screen_rect.collidepoint(self.x, self.y):
            self.kill()  # Remove the asteroid sprite when it leaves the screen
        '''