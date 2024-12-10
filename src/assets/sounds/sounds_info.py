import os

import pygame

from config import Settings

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