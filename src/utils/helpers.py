import importlib
import math
import random

import pygame

from config import Settings
from src.assets.images.img_info import img_info_asteroid, img_asteroid, img_explosion, \
    img_info_explosion
from src.assets.sounds.sounds_info import mscExplosion


def draw_on_screen(screen, image, center_source, width_height_source, center_dest, width_height_dest, rotation=0,
                   issprite=False):
    if issprite:
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
    return [math.cos(ang), math.sin(ang)]


def dist(p, q):
    return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)


def asteroid_spawner(asteroids_group, running, spaceRocket):
    if running and len(asteroids_group) < Settings.MAX_ASTEROIDS:
        rock_pos = [random.randrange(0, Settings.WIDTH), random.randrange(0, Settings.HEIGHT)]
        rock_vel = [random.random() * .6 - .3, random.random() * .6 - .3]
        rock_avel = random.random() * .2 - .1
        module_sprite = importlib.import_module("src.sprite")
        a_rock = module_sprite.Sprite(rock_pos, rock_vel, 0, rock_avel, img_asteroid, img_info_asteroid)

        if not a_rock.collide(spaceRocket):
            asteroids_group.add(a_rock)


def group_collide(sp_group, sprite, explosion_group):
    collision_happended = False

    for sp in list(sp_group):
        if sp.collide(sprite):
            sp_group.remove(sp)
            collision_happended = True
            module_sprite = importlib.import_module("src.sprite")
            an_explosion = module_sprite.Sprite(sprite.get_position(), [0, 0], 0, 0, img_explosion, img_info_explosion,
                                                mscExplosion)
            explosion_group.add(an_explosion)
    return collision_happended


def process_sprite_group(sprite_group, screen):
    for sprite in list(sprite_group):
        if sprite.update():
            sprite_group.remove(sprite)
        sprite.draw(screen)


def group_group_collide(sp_group1, sp_group2, explosion_group):
    no_of_collisions = 0
    for sp1 in list(sp_group1):
        if group_collide(sp_group2, sp1, explosion_group):
            no_of_collisions += 1
            sp_group1.discard(sp1)
    return no_of_collisions
