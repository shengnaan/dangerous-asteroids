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


msc_background_theme = pygame.mixer.Sound(os.path.join(Settings.SOUNDS_DIR, 'mscBackgroundTheme.wav'))
msc_background_theme.set_volume(0.2)
if msc_background_theme:
    msc_background_theme.play(100)

msc_rocket_thrust = pygame.mixer.Sound(os.path.join(Settings.SOUNDS_DIR, "mscRocketThrust.wav"))
msc_rocket_thrust.set_volume(0.9)

msc_missile_shot = pygame.mixer.Sound(os.path.join(Settings.SOUNDS_DIR, 'mscMissileShot.wav'))
msc_missile_shot.set_volume(0.2)

msc_explosion = pygame.mixer.Sound(os.path.join(Settings.SOUNDS_DIR, "mscExplosion.wav"))
msc_explosion.set_volume(0.8)