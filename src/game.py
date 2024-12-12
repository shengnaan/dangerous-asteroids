import pygame

from config import Settings

from src.classes.rocket import SpaceRocket
from src.utils import helpers
from src.utils import resources


def game():
    LIVES = Settings.LIVES
    SCORE = Settings.SCORE
    running = True
    space_rocket = SpaceRocket([Settings.WIDTH / 2, Settings.HEIGHT / 2], [0, 0], 0, resources.img_rocket,
                               resources.img_accelerating_rocket,
                               resources.img_info_rocket)
    asteroids_group = set([])
    missile_group = set([])
    explosion_group = set([])

    ROCK_SPAWN = pygame.USEREVENT + 1
    pygame.time.set_timer(ROCK_SPAWN, 1000)

    screen = pygame.display.set_mode((Settings.WIDTH, Settings.HEIGHT))

    if not helpers.show_intro(screen, resources.img_background, resources.img_intro, resources.img_info_intro):
        return

    while running:

        screen.blit(resources.img_background, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

            if event.type == ROCK_SPAWN:
                if LIVES > 0:
                    helpers.asteroid_spawner(asteroids_group, running, space_rocket)

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

        if helpers.group_collide(asteroids_group, space_rocket, explosion_group):
            LIVES -= 1
            space_rocket.reset([Settings.WIDTH / 2, Settings.HEIGHT / 2])

        if LIVES > 0:
            space_rocket.draw(screen)
            space_rocket.update()

        helpers.process_sprite_group(asteroids_group, screen)
        helpers.process_sprite_group(missile_group, screen)
        SCORE += helpers.group_group_collide(asteroids_group, missile_group, explosion_group)
        helpers.process_sprite_group(explosion_group, screen)

        if LIVES <= 0:
            helpers.draw_on_screen(screen, resources.img_intro, resources.img_info_intro.get_center(),
                                   resources.img_info_intro.get_size(), [Settings.WIDTH / 2, Settings.HEIGHT / 2],
                                   resources.img_info_intro.get_size())

            for asteroid in list(asteroids_group):
                asteroids_group.remove(asteroid)

        score_render = resources.font.render("Score: " + str(SCORE), True, (255, 255, 255))
        screen.blit(score_render, (10, 15))
        lives_render = resources.font.render("Lives: " + str(LIVES), True, (255, 255, 255))
        screen.blit(lives_render, (1660, 15))

        pygame.display.update()
