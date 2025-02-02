import pygame  # type: ignore
import sys  # noqa: F401
from asteroidfield import AsteroidField
from constants import * # noqa: F403
from asteroid import Asteroid
from player import Player 
from shot import Shot
#from constants import SCREEN_WIDTH, SCREEN_HEIGHT

def main():
    pygame.init()
    # Set up the display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #noqa: F405
    pygame.display.set_caption("Asteroids Game")
    # Create a clock object to control the frame rate
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    # Create a group to contain all asteroids
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Shot.containers = (shots, updatable, drawable) 
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable, )
    # Create an instance of the asteroid field
    asteroid_field = AsteroidField()  # noqa: F841
      
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) # noqa: F405

    dt = 0

    # main loop
    while True:  # noqa: F405
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # After your event handling loop
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            player.shoot()
            # The shot will automatically be added to the shots group
            # because we set up the containers 

        for obj in updatable:
            obj.update(dt)

        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game over!")
                sys.exit()

            for shot in shots:
                if shot.collision(asteroid):
                    shot.kill()
                    asteroid.split()
               
        # Fill the screen with black color (RGB)
        screen.fill((0, 0, 0))
        
        for obj in drawable:
             obj.draw(screen)   

        # Update the display
        pygame.display.flip()

        # Cap the frame rate at 60 frames per second
        dt = clock.tick(60) / 1000
        #if dt > 0.015:  # only print if dt is larger than expected
        #    print(f"Delta time: {dt}")
if __name__ == "__main__":
    main()