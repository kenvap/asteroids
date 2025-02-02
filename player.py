import pygame # type: ignore
from circleshape import CircleShape
from constants import * # noqa: F403
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)  # noqa: F405
        self.rotation = 0
        self.timer = 0

        # in the player class
    def triangle(self):
        forward = pygame.Vector2(0,-1).rotate(self.rotation)
        right = pygame.Vector2(0, -1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def shoot(self):
        if self.timer > 0:
            return None
        forward = pygame.Vector2(0, -1).rotate(self.rotation)
        # Start at the tip of the triangle
        shot_pos = self.position + (forward * self.radius)
        velocity = forward * PLAYER_SHOOT_SPEED  # noqa: F405
        shot = Shot(shot_pos[0], shot_pos[1], SHOT_RADIUS, velocity)  # noqa: F405
        self.timer = PLAYER_SHOOT_COOLDOWN  # noqa: F405
        return shot
    
    def draw(self, screen):
        color = (255, 255, 255)  # White color
        points = self.triangle()
        line_width = 2
        pygame.draw.polygon(screen, color, points, line_width)
        # pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt  # noqa: F405

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:  # Add this check for spacebar
            self.shoot()


        self.timer = max(0, self.timer - dt)  # decreases timer by the elapsed time       

    def move(self, dt):
        forward = pygame.Vector2(0, -1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt  # noqa: F405
