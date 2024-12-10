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


imgInfoSpaceWorld = ImageInfo([400, 300], [800, 600])
imgSpaceWorld = pygame.image.load(os.path.join(Settings.IMAGES_DIR, "imgSpaceWorld.jpeg"))

imgInfoIntroUltimateAsteroids = ImageInfo([200, 150], [400, 300])
imgIntroUltimateAsteroids = pygame.image.load(os.path.join(Settings.IMAGES_DIR, "imgIntroUltimateAsteroids.png"))

imgInfoSpaceRocket = ImageInfo([30, 30], [60, 60], 35)
imgSpaceRocketNoThrust = pygame.image.load(os.path.join(Settings.IMAGES_DIR, "imgSpaceRocketNoThrust.png"))
imgSpaceRocketThrust = pygame.image.load(os.path.join(Settings.IMAGES_DIR, "imgSpaceRocketThrust.png"))

imgInfoAsteroidBlack = ImageInfo([45, 45], [90, 90], 40)
imgAsteroidBlack = pygame.image.load(os.path.join(Settings.IMAGES_DIR, "imgAsteroidBlack.png"))

imgInfoMissile = ImageInfo([5, 5], [10, 10], 3, 50)
imgMissile = pygame.image.load(os.path.join(Settings.IMAGES_DIR, "imgMissile.png"))

imgInfoSpriteExplosion = ImageInfo([64, 64], [128, 128], 17, 24, True)
imgSpriteExplosion = pygame.image.load(os.path.join(Settings.IMAGES_DIR, "imgSpriteExplosion.png"))

icon = pygame.image.load(os.path.join(Settings.IMAGES_DIR, "iconUltimateAsteroids.png"))
