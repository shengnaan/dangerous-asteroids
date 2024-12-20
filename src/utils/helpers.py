import importlib
import math
import random

import pygame

from config import Settings
from src.utils.resources import img_asteroid, img_info_asteroid, msc_explosion, img_explosion, img_info_explosion


def draw_on_screen(screen, image, center_source, width_height_source, center_dest, width_height_dest, rotation=0,
                   is_sprite=False):
    """
    Отображает изображение на экране с возможностью вращения и использования спрайтов.

    :param screen: Экран Pygame, на котором рисуется изображение.
    :param image: Изображение для отображения.
    :param center_source: Центр исходного изображения.
    :param width_height_source: Размер исходного изображения.
    :param center_dest: Центр изображения на экране.
    :param width_height_dest: Размер изображения на экране.
    :param rotation: Угол вращения изображения.
    :param is_sprite: Флаг для отображения спрайта.
    """
    if is_sprite:
        left_dest = center_dest[0] - (width_height_dest[0] / 2)
        top_dest = center_dest[1] - (width_height_dest[1] / 2)
        width_dest = width_height_dest[0]
        height_dest = width_height_dest[1]
        rect_dest = pygame.Rect(left_dest, top_dest, width_dest, height_dest)

        left_src = center_source[0] - (width_height_source[0] / 2)
        top_src = center_source[1] - (width_height_source[1] / 2)
        width_src = width_height_source[0]
        height_src = width_height_source[1]
        rect_src = pygame.Rect(left_src, top_src, width_src, height_src)
        screen.blit(image, rect_dest, rect_src)
    else:

        rotation_degrees = math.degrees(rotation)
        rotation_degrees %= 360
        rotated = pygame.transform.rotate(image, rotation_degrees)
        rect_dest = rotated.get_rect(center=(center_dest[0], center_dest[1]))
        screen.blit(rotated, rect_dest)


def angle_to_vector(ang):
    """
    Преобразует угол в вектор.

    :param ang: Угол в радианах.
    :return: Список из двух элементов — компоненты вектора (x, y).
    """
    return [math.cos(ang), math.sin(ang)]


def dist(p, q):
    """
    Вычисляет расстояние между двумя точками.

    :param p: Первая точка (x, y).
    :param q: Вторая точка (x, y).
    :return: Расстояние между точками.
    """
    return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)


def asteroid_spawner(asteroids_group, running, spaceRocket):
    """
    Спавнит астероиды в игре, если они ещё не достигли максимального количества.

    :param asteroids_group: Группа астероидов.
    :param running: Статус игры (игра идет или нет).
    :param spaceRocket: Ракета игрока.
    """
    if running and len(asteroids_group) < Settings.MAX_ASTEROIDS:
        rock_pos = [random.randrange(0, Settings.WIDTH), random.randrange(0, Settings.HEIGHT)]
        rock_vel = [random.random() * .6 - .3, random.random() * .6 - .3]
        rock_avel = random.random() * 0.06 - 0.03
        module_sprite = importlib.import_module("src.classes.sprite")
        a_rock = module_sprite.Sprite(rock_pos, rock_vel, 0, rock_avel, img_asteroid, img_info_asteroid)

        if not a_rock.collide(spaceRocket):
            asteroids_group.add(a_rock)


def group_collide(sp_group, sprite, explosion_group):
    """
    Проверяет на столкновение объекта с группой спрайтов.

    :param sp_group: Группа спрайтов.
    :param sprite: Спрайт, с которым проверяется столкновение.
    :param explosion_group: Группа взрывов, в случае столкновения добавляется новый взрыв.
    :return: Возвращает True, если произошло столкновение.
    """
    collision_happended = False

    for sp in list(sp_group):
        if sp.collide(sprite):
            sp_group.remove(sp)
            collision_happended = True
            module_sprite = importlib.import_module("src.classes.sprite")
            an_explosion = module_sprite.Sprite(sprite.get_position(), [0, 0], 0, 0, img_explosion, img_info_explosion,
                                                msc_explosion)
            explosion_group.add(an_explosion)
    return collision_happended


def process_sprite_group(sprite_group, screen):
    """
    Обрабатывает группу спрайтов: обновляет и рисует их.

    :param sprite_group: Группа спрайтов.
    :param screen: Экран для рисования.
    """
    for sprite in list(sprite_group):
        if sprite.update():
            sprite_group.remove(sprite)
        sprite.draw(screen)


def group_group_collide(sp_group1, sp_group2, explosion_group):
    """
    Проверяет столкновения между двумя группами спрайтов.

    :param sp_group1: Первая группа спрайтов.
    :param sp_group2: Вторая группа спрайтов.
    :param explosion_group: Группа взрывов.
    :return: Количество столкновений.
    """
    no_of_collisions = 0
    for sp1 in list(sp_group1):
        if group_collide(sp_group2, sp1, explosion_group):
            no_of_collisions += 1
            sp_group1.discard(sp1)
    return no_of_collisions


def show_intro(screen, img_background, img_intro, img_info_intro):
    """
    Отображает вступительный экран игры.

    :param screen: Экран для отображения.
    :param img_background:
    :param img_intro:
    :param img_info_intro:
    """
    intro_running = True

    while intro_running:
        screen.blit(img_background, (0, 0))

        draw_on_screen(screen, img_intro, img_info_intro.get_center(),
                       img_info_intro.get_size(), [Settings.WIDTH / 2, Settings.HEIGHT / 2],
                       img_info_intro.get_size())

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                intro_running = False

        pygame.display.flip()

    return True
