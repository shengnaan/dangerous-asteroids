from config import Settings
from src.utils.helpers import draw_on_screen, dist


class Sprite:
    """
    Класс, представляющий спрайт в игре.

    Атрибуты:
        pos (list[float]): Позиция спрайта на экране в координатах [x, y].
        vel (list[float]): Скорость спрайта в координатах [vx, vy].
        angle (float): Угол поворота спрайта в радианах.
        angle_vel (float): Угловая скорость вращения спрайта.
        image (Surface): Изображение спрайта.
        image_center (tuple[int, int]): Центр изображения спрайта.
        image_size (tuple[int, int]): Размер изображения спрайта (ширина, высота).
        radius (int): Радиус коллизии спрайта.
        lifespan (int): Продолжительность жизни спрайта в кадрах.
        animated (bool): Флаг, указывающий, является ли спрайт анимационным.
        age (int): Текущий возраст спрайта.
    """

    def __init__(self, pos, vel, ang, ang_vel, image, info, sound=None):
        """
        Инициализирует спрайт с заданными параметрами.

        :param pos: Позиция спрайта на экране.
        :param vel: Скорость спрайта.
        :param ang: Начальный угол поворота спрайта.
        :param ang_vel: Начальная угловая скорость.
        :param image: Изображение спрайта.
        :param info: Объект, содержащий информацию о спрайте (центр, размер, радиус и т.д.).
        :param sound: Звук, который будет воспроизведен при создании спрайта (по умолчанию None).
        """
        self.pos = [pos[0], pos[1]]
        self.vel = [vel[0], vel[1]]
        self.angle = ang
        self.angle_vel = ang_vel
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.lifespan = info.get_lifespan()
        self.animated = info.get_animated()
        self.age = 0
        if sound:
            sound.play()

    def get_position(self):
        """
        Возвращает текущую позицию спрайта.

        :return: Позиция спрайта [x, y].
        """
        return self.pos

    def get_radius(self):
        """
        Возвращает радиус спрайта.

        :return: Радиус спрайта.
        """
        return self.radius

    def collide(self, object2):
        """
        Проверяет, сталкивается ли текущий спрайт с другим объектом.

        :param object2: Другой спрайт для проверки столкновения.
        :return: True, если спрайты столкнулись, иначе False.
        """
        r1 = self.get_radius()
        r2 = object2.get_radius()

        pos1 = self.get_position()
        pos2 = object2.get_position()
        return dist(pos1, pos2) < (r1 + r2)

    def draw(self, screen):
        """
        Рисует спрайт на экране.

        :param screen: Поверхность экрана, на которой будет рисоваться спрайт.
        """
        factor = 1
        if self.animated:
            factor *= self.age
            draw_on_screen(screen, self.image,
                           [self.image_center[0] + (factor * self.image_size[0]), self.image_center[1]],
                           self.image_size, self.pos, self.image_size, self.angle, True)
        else:
            draw_on_screen(screen, self.image, self.image_center, self.image_size, self.pos, self.image_size,
                           self.angle)

    def update(self):
        """
        Обновляет состояние спрайта: поворот, движение, возраст.

        :return: True, если спрайт достиг своей продолжительности жизни, иначе False.
        """
        self.angle += self.angle_vel

        self.pos[0] = (self.pos[0] + self.vel[0]) % Settings.WIDTH
        self.pos[1] = (self.pos[1] + self.vel[1]) % Settings.HEIGHT

        self.age += 1

        return self.age >= self.lifespan
