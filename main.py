import pygame
import math

pygame.init()

Width, Height = 900 , 900
window =  pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Stellar Simulator")

SUN_COLOR = (250,250,0)
BLUE = (20,100,255)
RED = (180,69,23)

class Planet:

    AU = 149.6e6 * 1000
    G = 6.67428e-11
    SCALE = 250 / AU
    TIMESETP = 3600*24
    def __init__(self,x ,y ,radius , color, mass):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass

        self.sun = False
        self.distance_to_sun = 0
        self.orbit = []

        self.x_velocity = 0
        self.y_velocity = 0

    def draw(self, window):
        x = self.x * self.SCALE + Width / 2
        y = self.y * self.SCALE + Height / 2
        pygame.draw.circle(window,self.color,(x,y),self.radius)





def main():
    run = True
    clock = pygame.time.Clock()

    sun = Planet(0,0,35,SUN_COLOR,1.98812 * 10**30)
    sun.sun = True

    earth = Planet(-1 * Planet.AU,0,15,BLUE,5.9742 * 10**24)
    mars = Planet(-1.56 * Planet.AU,0,18,RED,6.39 * 10**23)

    planets = [sun,earth,mars]

    while run:
        clock.tick(60)
        window.fill((0,13,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for planet in planets:
            planet.draw(window)

        pygame.display.update()


    pygame.quit()

if __name__ == '__main__':
    main()
