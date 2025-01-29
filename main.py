import pygame
import sys

# Инициализация pygame
pygame.init()

# Настройки экрана
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Simple Mario Game")

# Цвета
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Персонаж
player_size = 50
player_x = 100
player_y = screen_height - player_size - 10
player_speed = 5
player_jump_speed = 13
gravity = 1
is_jumping = False
jump_count = 1

# Платформы
platforms = [
    pygame.Rect(10, 400, 200, 20),
    pygame.Rect(400, 300, 200, 20),
    pygame.Rect(200, 200, 200, 20)
]

# Главный игровой цикл
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Обработка нажатий клавиш
    keys = pygame.key.get_pressed()
    new_player_x = player_x
    new_player_y = player_y

    if keys[pygame.K_LEFT]:
        new_player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        new_player_x += player_speed

    # Прыжок
    if not is_jumping:
        if keys[pygame.K_SPACE]:
            is_jumping = True
            jump_count = player_jump_speed
    else:
        if jump_count >= -player_jump_speed:
            neg = 1
            if jump_count < 0:
                neg = -1
            new_player_y -= (jump_count ** 2) * 0.5 * neg
            jump_count -= 1
        else:
            is_jumping = False

    # Гравитация
    if not is_jumping:
        new_player_y += gravity

    # Ограничение движения персонажа
    if new_player_x < 0:
        new_player_x = 0
    if new_player_x > screen_width - player_size:
        new_player_x = screen_width - player_size
    if new_player_y > screen_height - player_size:
        new_player_y = screen_height - player_size
        is_jumping = False

    # Проверка столкновений с платформами
    player_rect = pygame.Rect(new_player_x, new_player_y, player_size, player_size)
    for platform in platforms:
        if player_rect.colliderect(platform) and new_player_y + player_size <= platform.y + 5:
            new_player_y = platform.y - player_size
            is_jumping = False

    # Обновление координат персонажа
    player_x = new_player_x
    player_y = new_player_y

    # Отрисовка
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_size, player_size))

    for platform in platforms:
        pygame.draw.rect(screen, GREEN, platform)

    pygame.display.flip()
    clock.tick(30)