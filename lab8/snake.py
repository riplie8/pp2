import pygame, sys, random
from pygame.math import Vector2


class SNAKE:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(0, 0)
        self.new_block = False

    def draw_snake(self):
        for index, block in enumerate(self.body):
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)

            if index == 0:
                pygame.draw.rect(screen, (0, 100, 200), block_rect)
            else:
                pygame.draw.rect(screen, (0, 150, 255), block_rect)

    def move_snake(self):
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

    def add_block(self):
        self.new_block = True

    def reset(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(0, 0)


class FRUIT:
    def __init__(self):
        self.randomize()

    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
        pygame.draw.rect(screen, (255, 0, 0), fruit_rect)

    def randomize(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)


class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()
        self.current_speed = 150
        self.lvl_change = 5
        self.level = 1

    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()

    def draw_elements(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.draw_score()
        self.draw_level()

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_block()
            self.check_level_up()

        for block in self.snake.body[1:]:
            if block == self.fruit.pos:
                self.fruit.randomize()

    def check_level_up(self):
        score = len(self.snake.body) - 3

        level = (score // self.lvl_change) + 1
        self.level = level

        new_speed = self.current_speed

        if level == 1:
            new_speed = 150
        elif level == 2:
            new_speed = 100
        elif level == 3:
            new_speed = 75
        elif level == 4:
            new_speed = 50
        elif level == 5:
            new_speed = 25
        elif level >= 6:
            new_speed = 1

        if new_speed != self.current_speed:
            self.current_speed = new_speed
            pygame.time.set_timer(SCREEN_UPDATE, self.current_speed)

    def check_fail(self):
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()

        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        self.snake.reset()
        self.current_speed = 150
        pygame.time.set_timer(SCREEN_UPDATE, self.current_speed)
        self.level = 1

    def draw_score(self):
        score_text = str(len(self.snake.body) - 3)
        score_surface = game_font.render(score_text, True, (56, 74, 12))
        score_x = int(cell_size * cell_number - 60)
        score_y = int(cell_size * cell_number - 40)
        score_rect = score_surface.get_rect(center=(score_x, score_y))
        bg_rect = pygame.Rect(score_rect.left - 10, score_rect.top - 5, score_rect.width + 20, score_rect.height + 10)

        pygame.draw.rect(screen, (167, 209, 61), bg_rect)
        screen.blit(score_surface, score_rect)
        pygame.draw.rect(screen, (56, 74, 12), bg_rect, 2)

    def draw_level(self):
        level_text = f"Level: {self.level}"
        level_surface = game_font.render(level_text, True, (56, 74, 12))

        level_x = int(cell_size * cell_number - 80)
        level_y = int(40)
        level_rect = level_surface.get_rect(center=(level_x, level_y))
        bg_rect = pygame.Rect(level_rect.left - 10, level_rect.top - 5, level_rect.width + 20, level_rect.height + 10)

        pygame.draw.rect(screen, (167, 209, 61), bg_rect)
        screen.blit(level_surface, level_rect)
        pygame.draw.rect(screen, (56, 74, 12), bg_rect, 2)


pygame.init()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
clock = pygame.time.Clock()
game_font = pygame.font.Font(None, 35)

SCREEN_UPDATE = pygame.USEREVENT
main_game = MAIN()

pygame.time.set_timer(SCREEN_UPDATE, main_game.current_speed)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_RIGHT:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1, 0)
            if event.key == pygame.K_DOWN:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0, 1)
            if event.key == pygame.K_LEFT:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1, 0)

    screen.fill((175, 215, 70))
    main_game.draw_elements()
    pygame.display.flip()
    clock.tick(60)