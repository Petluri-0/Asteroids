from constants import SCREEN_WIDTH
from constants import SCREEN_HEIGHT
import pygame
import sys
from player import Player
from asteroids import Asteroids
from logger import log_state
from logger import log_event
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable,drawable)
    Asteroids.containers = (asteroids,updatable,drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots,updatable,drawable)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0
    x = SCREEN_WIDTH/2
    y = SCREEN_HEIGHT/2
    score = 0
    font = pygame.font.SysFont("Times Roman",12,True,False)
    player = Player(x,y)
    Asteroidfields = AsteroidField()
    while(True):
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 
        screen.fill("black")

        updatable.update(dt)
        for asteroid in asteroids:
            for shot in shots:
                if(shot.collides_with(asteroid)):
                    log_event("asteroid_shot")
                    asteroid.split()
                    shot.kill()
                    score+=1
            if(asteroid.collides_with(player)):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        for drawables in drawable:
            drawables.draw(screen)
        
        score_surface = font.render(f"Score{score}",True,"white")
        screen.blit(score_surface,(10,10))
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        #print(dt)
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
