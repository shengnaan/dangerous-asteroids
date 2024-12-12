import os


class Settings:
    """
    Класс, содержащий глобальные настройки игры, такие как размеры экрана, начальный счет, количество жизней и астероидов.

    Атрибуты:
        WIDTH (int): Ширина экрана игры.
        HEIGHT (int): Высота экрана игры.
        SCORE (int): Текущий счет игрока.
        LIVES (int): Количество жизней игрока.
        MAX_ASTEROIDS (int): Максимальное количество астероидов на экране.
        WORK_DIR (str): Рабочая директория (директория, в которой находится скрипт).
        FONT_DIR (str): Путь к директории, где хранятся шрифты игры.
        IMAGES_DIR (str): Путь к директории, где хранятся изображения игры.
        SOUNDS_DIR (str): Путь к директории, где хранятся звуковые файлы игры.
    """
    WIDTH = 1920
    HEIGHT = 1080
    SCORE = 0
    LIVES = 3
    MAX_ASTEROIDS = 15

    WORK_DIR = os.path.dirname(__file__)
    FONT_DIR = os.path.join(WORK_DIR, 'src/assets/fonts')
    IMAGES_DIR = os.path.join(WORK_DIR, 'src/assets/images')
    SOUNDS_DIR = os.path.join(WORK_DIR, 'src/assets/sounds')
