import os


class Settings:
    WIDTH = 1920
    HEIGHT = 1080
    SCORE = 0
    LIVES = 3
    MAX_ASTEROIDS = 12

    WORK_DIR = os.path.dirname(__file__)
    FONT_DIR = os.path.join(WORK_DIR, 'src/assets/fonts')
    IMAGES_DIR = os.path.join(WORK_DIR, 'src/assets/images')
    SOUNDS_DIR = os.path.join(WORK_DIR, 'src/assets/sounds')
