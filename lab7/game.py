import pygame

pygame.init()
screen = pygame.display.set_mode((500, 500))
done = False
is_green = True
x = 30
y = 30
clock = pygame.time.Clock()
while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                is_green = not is_green

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: y -= 3
        if pressed[pygame.K_DOWN]: y += 3
        if pressed[pygame.K_LEFT]: x -= 3
        if pressed[pygame.K_RIGHT]: x += 3
        screen.fill((0, 0, 0))

        if is_green:
            color = (255, 255, 0)
        else:
            color = (255, 0, 200)
        pygame.draw.rect(screen, color, pygame.Rect(x, y, 60, 60))
        pygame.display.flip()
        clock.tick(60)