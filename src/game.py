import pygame

from config import Settings

from src.classes.rocket import SpaceRocket
from src.utils import helpers
from src.utils import resources


def game():
    """
    Главный игровой цикл для космической игры. Обрабатывает пользовательский ввод, обновляет состояние игры
    и рисует элементы игры на экране: космический корабль, астероиды, ракеты, взрывы.
    Управляет механиками игры, такими как жизни, счет и спавн астероидов.
    """
    # Инициализация жизней и счета на основе настроек
    LIVES = Settings.LIVES
    SCORE = Settings.SCORE

    # Переменная для контроля цикла игры
    running = True

    # Создание космического корабля
    space_rocket = SpaceRocket([Settings.WIDTH / 2, Settings.HEIGHT / 2], [0, 0], 0, resources.img_rocket,
                               resources.img_accelerating_rocket,
                               resources.img_info_rocket)

    # Создание пустых групп для астероидов, ракет и взрывов
    asteroids_group = set()
    missile_group = set()
    explosion_group = set()

    # Установка таймера для спавна астероидов
    ROCK_SPAWN = pygame.USEREVENT + 1
    pygame.time.set_timer(ROCK_SPAWN, 1000)

    screen = pygame.display.set_mode((Settings.WIDTH, Settings.HEIGHT))
    # Показываем вступительный экран
    if not helpers.show_intro(screen, resources.img_background, resources.img_intro, resources.img_info_intro):
        return

    asteroids_group.clear()
    # Главный игровой цикл
    while running:

        # Отображение фона игры
        screen.blit(resources.img_background, (0, 0))

        # Обработка событий в игре (нажатия клавиш, выход из игры и т.д.)
        for event in pygame.event.get():

            # Выход из игры, если пользователь закрыл окно или нажал ESC
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

            # Спавн астероидов, если событие ROCK_SPAWN срабатывает и у игрока есть жизни
            if event.type == ROCK_SPAWN:
                if LIVES > 0:
                    helpers.asteroid_spawner(asteroids_group, running, space_rocket)

            # Обработка нажатий клавиш для действий игрока
            if event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_LEFT:
                        space_rocket.decrement_angle_vel()
                    case pygame.K_RIGHT:
                        space_rocket.increment_angle_vel()
                    case pygame.K_UP:
                        space_rocket.set_thrust(True)
                    case pygame.K_SPACE:
                        space_rocket.shoot(missile_group)
                    case pygame.K_RETURN:
                        if LIVES <= 0:
                            LIVES = 3
                            SCORE = 0

            # Обработка отпускания клавиш (например, остановка вращения или тяги)
            if event.type == pygame.KEYUP:
                match event.key:
                    case pygame.K_LEFT:
                        if space_rocket.angle_vel == 0:
                            continue
                        space_rocket.increment_angle_vel()
                    case pygame.K_RIGHT:
                        if space_rocket.angle_vel == 0:
                            continue
                        space_rocket.decrement_angle_vel()
                    case pygame.K_UP:
                        space_rocket.set_thrust(False)

        # Проверка на столкновения между космическим кораблем и астероидами
        if helpers.group_collide(asteroids_group, space_rocket, explosion_group):
            LIVES -= 1
            space_rocket.reset([Settings.WIDTH / 2, Settings.HEIGHT / 2])

        # Обновление и рисование космического корабля, если у игрока есть жизни
        if LIVES > 0:
            space_rocket.draw(screen)
            space_rocket.update()

        # Обработка и рисование других групп спрайтов (астероида, ракет, взрывов)
        helpers.process_sprite_group(asteroids_group, screen)
        helpers.process_sprite_group(missile_group, screen)

        # Обработка столкновений между ракетами и астероидами
        SCORE += helpers.group_group_collide(asteroids_group, missile_group, explosion_group)
        helpers.process_sprite_group(explosion_group, screen)

        # Если жизни закончились, отображаем экран окончания игры
        if LIVES <= 0:
            helpers.draw_on_screen(screen, resources.img_intro, resources.img_info_intro.get_center(),
                                   resources.img_info_intro.get_size(), [Settings.WIDTH / 2, Settings.HEIGHT / 2],
                                   resources.img_info_intro.get_size())

            # Удаление оставшихся астероидов из игры
            for asteroid in list(asteroids_group):
                asteroids_group.remove(asteroid)

        # Отображение счета и количества жизней на экране
        score_render = resources.font.render("Score: " + str(SCORE), True, (255, 255, 255))
        screen.blit(score_render, (10, 15))
        lives_render = resources.font.render("Lives: " + str(LIVES), True, (255, 255, 255))
        screen.blit(lives_render, (1660, 15))

        # Обновление экрана для отображения нового кадра
        pygame.display.update()
