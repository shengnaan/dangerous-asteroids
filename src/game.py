

import pygame

from config import Settings
from src.assets.fonts.fonts_info import font
from src.assets.images.img_info import (imgInfoSpaceRocket, imgSpaceRocketNoThrust, imgSpaceRocketThrust, imgSpaceWorld,
                                        imgIntroUltimateAsteroids, imgInfoIntroUltimateAsteroids)
from src.assets.rocket import SpaceRocket
from src.utils.helpers import asteroid_spawner, group_collide, process_sprite_group, group_group_collide, draw_on_screen
def game():

    LIVES = Settings.LIVES
    SCORE = Settings.SCORE
    running = True
    spaceRocket = SpaceRocket([Settings.WIDTH / 2, Settings.HEIGHT / 2], [0, 0], 0, imgSpaceRocketNoThrust, imgSpaceRocketThrust,
                              imgInfoSpaceRocket)
    asteroids_group = set([])
    missile_group = set([])
    explosion_group = set([])

    ROCK_SPAWN = pygame.USEREVENT + 1
    pygame.time.set_timer(ROCK_SPAWN, 1000)

    screen = pygame.display.set_mode((Settings.WIDTH, Settings.HEIGHT))
    while running:
        screen.blit(imgSpaceWorld, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == ROCK_SPAWN:
                if LIVES > 0:
                    asteroid_spawner(asteroids_group, running, spaceRocket)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    spaceRocket.decrement_angle_vel()
                elif event.key == pygame.K_RIGHT:
                    spaceRocket.increment_angle_vel()
                elif event.key == pygame.K_UP:
                    spaceRocket.set_thrust(True)
                elif event.key == pygame.K_SPACE:
                    spaceRocket.shoot(missile_group)
                elif event.key == pygame.K_RETURN:
                    if LIVES <= 0:
                        LIVES = 3
                        SCORE = 0

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    spaceRocket.increment_angle_vel()
                elif event.key == pygame.K_RIGHT:
                    spaceRocket.decrement_angle_vel()
                elif event.key == pygame.K_UP:
                    spaceRocket.set_thrust(False)

        if group_collide(asteroids_group, spaceRocket, explosion_group):
            LIVES -= 1

        spaceRocket.draw(screen)
        process_sprite_group(asteroids_group, screen)
        process_sprite_group(missile_group, screen)
        SCORE += group_group_collide(asteroids_group, missile_group, explosion_group)
        process_sprite_group(explosion_group, screen)

        spaceRocket.update()

        if LIVES <= 0:
            draw_on_screen(screen, imgIntroUltimateAsteroids, imgInfoIntroUltimateAsteroids.get_center(),
                           imgInfoIntroUltimateAsteroids.get_size(), [Settings.WIDTH / 2, Settings.HEIGHT / 2],
                           imgInfoIntroUltimateAsteroids.get_size())

            for asteroid in list(asteroids_group):
                asteroids_group.remove(asteroid)

        score_render = font.render("Score: " + str(SCORE), True, (255, 255, 255))
        screen.blit(score_render, (10, 10))
        lives_render = font.render("Lives: " + str(LIVES), True, (255, 255, 255))
        screen.blit(lives_render, (685, 10))

        pygame.display.update()
