import pygame
import math

pygame.init()

Width, Height = 900 , 900
window =  pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Stellar Simulator")

SUN_COLOR = (250,250,0)
BLUE = (20,100,255)
RED = (180,69,23)
DARK_GREY = (80,78,81)
WHITE = (250,250,250)

FONT = pygame.font.SysFont("roboto",16)

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

        if len(self.orbit) > 2:
            updated_points = []
            for point in self.orbit:
                x,y = point
                x = x * self.SCALE + Width / 2
                y = y * self.SCALE + Height / 2
                updated_points.append((x,y))

            pygame.draw.lines(window,self.color,False, updated_points, 2)
        pygame.draw.circle(window,self.color,(x,y),self.radius)
        if not self.sun:
            distance_text = FONT.render(f"{round(self.distance_to_sun/1000,1)}KM",1,WHITE)
            window.blit(distance_text, (x - distance_text.get_width()/2,y - distance_text.get_width()/2))

    def attraction(self, other):
        other_x , other_y = other.x, other.y
        distance_x = other_x - self.x
        distance_y = other_y - self.y
        distance = math.sqrt(distance_x ** 2 + distance_y ** 2)

        if other.sun:
            self.distance_to_sun = distance

        force = self.G * self.mass * other.mass / distance**2
        theta = math.atan2(distance_y,distance_x)
        force_x = math.cos(theta) * force
        force_y = math.sin(theta) * force
        return force_x, force_y

    def update_position(self,planets):
        total_fx = total_fy = 0
        for planet in planets:
            if self == planet:
                continue

            fx, fy = self.attraction(planet)
            total_fx += fx
            total_fy += fy

        self.x_velocity += total_fx / self.mass * self.TIMESETP
        self.y_velocity += total_fy / self.mass * self.TIMESETP

        self.x += self.x_velocity * self.TIMESETP
        self.y += self.y_velocity * self.TIMESETP
        self.orbit.append((self.x,self.y))

def main():
    run = True
    clock = pygame.time.Clock()

    sun = Planet(0,0,35,SUN_COLOR,1.98812 * 10**30)
    sun.sun = True

    earth = Planet(-1 * Planet.AU,0,15,BLUE,5.9742 * 10**24)
    earth.y_velocity = 29.738 * 1000
    mars = Planet(-1.56 * Planet.AU,0,18,RED,6.39 * 10**23)
    mars.y_velocity = 24.077 * 1000
    mercury = Planet(0.387 * Planet.AU,0,11,DARK_GREY,0.330*10**24)
    mercury.y_velocity = -47.4 * 1000
    venus = Planet(0.723 * Planet.AU,0,9,WHITE, 4.8685 * 10**24)
    venus.y_velocity = -35.02 * 1000
    planets = [sun,earth,mars,mercury,venus]

    while run:
        clock.tick(60)
        window.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for planet in planets:
            planet.update_position(planets)
            planet.draw(window)

        pygame.display.update()


    pygame.quit()

if __name__ == '__main__':
    main()
