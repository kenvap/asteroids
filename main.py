# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame #noqa: F401
from constants import * # noqa: F403
#from constants import SCREEN_WIDTH, SCREEN_HEIGHT

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}") # noqa: F405
    print(f"Screen height: {SCREEN_HEIGHT}") # noqa: F405
    # Initialize pygame
    pygame.init()

    # Set up the display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #noqa: F405
    pygame.display.set_caption("Asteroids Game")

    # main loop
    while True:  # noqa: F405
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 

        # Fill the screen with a color (RGB)
        screen.fill((0, 0, 0))

        # Update the display
        pygame.display.flip()
    
if __name__ == "__main__":
    main()