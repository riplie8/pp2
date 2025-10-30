from time import get_clock_info

import pygame
pygame.init()
screen = pygame.display.set_mode((400, 300))
w = 400
h = 300
running = True
clock = pygame.time.Clock()

red = (255, 0, 0)

# Circle
x = 200
y = 150
radius = 25
c_color = red
speed = 20

while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            x -= speed
        if keys[pygame.K_RIGHT]:
            x += speed
        if keys[pygame.K_UP]:
            y -= speed
        if keys[pygame.K_DOWN]:
            y += speed

        if x - radius < 0:
            x = radius
        elif x + radius > w:
            x = w - radius

        if y - radius < 0:
            y = radius
        elif y + radius > h:
            y = h - radius

        screen.fill((255, 255, 255))

        pygame.draw.circle(screen, c_color, (x,y), radius)

        pygame.display.flip()
        clock.tick(60)

pygame.quit()