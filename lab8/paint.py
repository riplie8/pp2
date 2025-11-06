import pygame


def main():
    pygame.init()
    w = 800
    h = 600
    screen = pygame.display.set_mode((w, h))
    clock = pygame.time.Clock()

    radius = 15
    mode = 'blue'
    activeShape = 1
    painting = []
    current_stroke = []

    while True:

        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
                if event.key == pygame.K_SPACE:
                    painting = []
                if event.key == pygame.K_UP:
                    radius = min(200, radius + 1)
                elif event.key == pygame.K_DOWN:
                    radius = max(1, radius - 1)
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'

            if event.type == pygame.MOUSEBUTTONDOWN:
                colors, shapes = drawUI(screen, w)
                for i in colors:
                    if i[0].collidepoint(event.pos):
                        mode = i[1]
                for i in shapes:
                    if i[0].collidepoint(event.pos):
                        activeShape = i[1]
                        current_stroke = []

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 and len(current_stroke) > 0:
                    painting.append((mode, current_stroke[:], activeShape, radius))
                    current_stroke = []

            if event.type == pygame.MOUSEMOTION:
                if pygame.mouse.get_pressed()[0] and event.pos[1] > 115:
                    current_stroke.append(event.pos)

        screen.fill('white')
        drawUI(screen, w)

        mouse = pygame.mouse.get_pos()
        if mouse[1] > 100:
            if activeShape == 0:
                pygame.draw.rect(screen, mode, [mouse[0] - radius, mouse[1] - radius, radius * 2, radius * 2])
            if activeShape == 1:
                pygame.draw.circle(screen, mode, mouse, radius)

        for paint in painting:
            for i in range(len(paint[1]) - 1):
                drawLineBetween(screen, paint[1][i], paint[1][i + 1], paint[3], paint[0], paint[2])

        for i in range(len(current_stroke) - 1):
            drawLineBetween(screen, current_stroke[i], current_stroke[i + 1], radius, mode, activeShape)

        pygame.display.flip()
        clock.tick(60)


def drawUI(screen, w):
    pygame.draw.rect(screen, (255, 165, 0), [0, 0, w, 100])
    pygame.draw.line(screen, 'black', [0, 100], [w, 100])

    rect = [pygame.Rect(10, 10, 80, 80), 0]
    pygame.draw.rect(screen, 'black', [20, 20, 60, 60])
    circ = [pygame.Rect(100, 10, 80, 80), 1]
    pygame.draw.circle(screen, 'black', [140, 50], 30)

    color_width = (w - 200) // 6
    blue = [pygame.draw.rect(screen, (0, 0, 255), [200, 10, color_width, 40]), (0, 0, 255)]
    red = [pygame.draw.rect(screen, (255, 0, 0), [200 + color_width, 10, color_width, 40]), (255, 0, 0)]
    green = [pygame.draw.rect(screen, (0, 255, 0), [200 + color_width * 2, 10, color_width, 40]), (0, 255, 0)]
    yellow = [pygame.draw.rect(screen, (255, 255, 0), [200 + color_width * 3, 10, color_width, 40]), (255, 255, 0)]
    black = [pygame.draw.rect(screen, (0, 0, 0), [200 + color_width * 4, 10, color_width, 40]), (0, 0, 0)]
    eraser = [pygame.draw.rect(screen, (255, 255, 255), [200 + color_width * 5, 10, color_width, 40]), (255, 255, 255)]
    return [blue, red, green, yellow, black, eraser], [rect, circ]


def drawLineBetween(screen, start, end, width, color, shape_type):
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))

    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])

        if shape_type == 0:
            pygame.draw.rect(screen, color, [x - width, y - width, width * 2, width * 2])
        elif shape_type == 1:
            pygame.draw.circle(screen, color, (x, y), width)


main()