import pygame

import os

from config import Settings
from src.utils.image_info import ImageInfo


font = pygame.font.Font(os.path.join(Settings.FONT_DIR, 'Kenney Space.ttf'), 35)


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


mscBackgroundTheme = pygame.mixer.Sound(os.path.join(Settings.SOUNDS_DIR, 'mscBackgroundTheme.wav'))
mscBackgroundTheme.set_volume(0.2)
if mscBackgroundTheme:
    mscBackgroundTheme.play(100)

mscSpaceRocketThrust = pygame.mixer.Sound(os.path.join(Settings.SOUNDS_DIR, "mscSpaceRocketThrust.wav"))
mscSpaceRocketThrust.set_volume(0.9)

mscMissileShot = pygame.mixer.Sound(os.path.join(Settings.SOUNDS_DIR, 'mscMissileShot.wav'))
mscMissileShot.set_volume(0.2)

mscExplosion = pygame.mixer.Sound(os.path.join(Settings.SOUNDS_DIR, "mscExplosion.wav"))
mscExplosion.set_volume(0.8)