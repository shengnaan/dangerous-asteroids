import os

import pygame

from config import Settings


class ImageInfo:
    def __init__(self, center, size, radius=0, lifespan=None, animated=False):
        self.center = center
        self.size = size
        self.radius = radius
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float('inf')
        self.animated = animated

    def get_center(self):
        return self.center

    def get_size(self):
        return self.size

    def get_radius(self):
        return self.radius

    def get_lifespan(self):
        return self.lifespan

    def get_animated(self):
        return self.animated


img_info_background = ImageInfo([400, 300], [800, 600])
img_background = pygame.image.load(os.path.join(Settings.IMAGES_DIR, "background.jpeg"))

img_info_intro = ImageInfo([200, 150], [400, 300])
img_intro = pygame.image.load(os.path.join(Settings.IMAGES_DIR, "intro.png"))

img_info_rocket = ImageInfo([30, 30], [60, 60], 35)
img_rocket = pygame.image.load(os.path.join(Settings.IMAGES_DIR, "rocket.png"))
img_accelerating_rocket = pygame.image.load(os.path.join(Settings.IMAGES_DIR, "acceleratingRocket.png"))

img_info_asteroid = ImageInfo([45, 45], [90, 90], 40)
img_asteroid = pygame.image.load(os.path.join(Settings.IMAGES_DIR, "asteroid.png"))

img_info_missile = ImageInfo([5, 5], [10, 10], 3, 50)
img_missile = pygame.image.load(os.path.join(Settings.IMAGES_DIR, "missile.png"))

img_info_explosion = ImageInfo([64, 64], [128, 128], 17, 24, True)
img_explosion = pygame.image.load(os.path.join(Settings.IMAGES_DIR, "explosion.png"))

icon = pygame.image.load(os.path.join(Settings.IMAGES_DIR, "icon.png"))
