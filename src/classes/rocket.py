from config import Settings
from src.classes.sprite import Sprite
from src.utils.helpers import draw_on_screen, angle_to_vector
from src.utils.resources import msc_rocket_thrust, img_missile, img_info_missile, msc_missile_shot


class SpaceRocket:
    """
    Класс, представляющий космическую ракету, которая может двигаться, вращаться и стрелять.

    Атрибуты:
        pos (list[float]): Позиция ракеты на экране в координатах [x, y].
        vel (list[float]): Скорость ракеты в координатах [vx, vy].
        thrust (bool): Флаг, указывающий, активен ли двигатель ракеты.
        angle (float): Угол ориентации ракеты в радианах.
        angle_vel (float): Угловая скорость ракеты.
        image (Surface): Изображение ракеты без тяги.
        image_thrust (Surface): Изображение ракеты с тягой.
        image_center (tuple[int, int]): Центр изображения ракеты.
        image_size (tuple[int, int]): Размер изображения ракеты (ширина, высота).
        radius (int): Радиус коллизии ракеты.
    """

    def __init__(self, pos, vel, angle, image, image_thrust, info):
        """
        Инициализирует объект ракеты.

        :param pos: Позиция ракеты на экране.
        :param vel: Скорость ракеты.
        :param angle: Угол ориентации ракеты.
        :param image: Изображение ракеты без тяг.
        :param image_thrust: Изображение ракеты с тягой.
        :param info: Объект, содержащий информацию о ракетах (центр, размер, радиус).
        """
        self.pos = [pos[0], pos[1]]
        self.vel = [vel[0], vel[1]]
        self.thrust = False
        self.angle = angle
        self.angle_vel = 0
        self.image = image
        self.image_thrust = image_thrust
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()

    def draw(self, screen):
        """
        Рисует ракету на экране, в зависимости от состояния тяги.

        :param screen: Поверхность экрана, на которой будет рисоваться ракета.
        """
        if Settings.LIVES > 0:
            if self.thrust:
                draw_on_screen(screen, self.image_thrust, self.image_center, self.image_size, self.pos, self.image_size,
                               self.angle)
            else:
                draw_on_screen(screen, self.image, self.image_center, self.image_size, self.pos, self.image_size,
                               self.angle)

    def update(self):
        """
        Обновляет состояние ракеты: движение, вращение и тягу.

        :return: None
        """
        self.angle += self.angle_vel

        self.pos[0] = (self.pos[0] + self.vel[0]) % Settings.WIDTH
        self.pos[1] = (self.pos[1] + self.vel[1]) % Settings.HEIGHT

        if self.thrust:
            acc = angle_to_vector(-self.angle)
            self.vel[0] += acc[0] * .07
            self.vel[1] += acc[1] * .07

        self.vel[0] *= .98
        self.vel[1] *= .98

    def set_thrust(self, on):
        """
        Включает или выключает тягу ракеты.

        :param on: Флаг, указывающий, включить ли тягу.
        """
        self.thrust = on
        if on:
            msc_rocket_thrust.play()
        else:
            msc_rocket_thrust.stop()

    def increment_angle_vel(self):
        """
        Увеличивает угловую скорость ракеты.

        :return: None
        """
        self.angle_vel -= .05

    def decrement_angle_vel(self):
        """
        Уменьшает угловую скорость ракеты.

        :return: None
        """
        self.angle_vel += .05

    def shoot(self, missile_group):
        """
        Стреляет ракетой из ракеты в направлении её ориентации.

        :param missile_group: Группа, в которую будет добавлена новая ракета.
        """
        forward = angle_to_vector(-self.angle)
        missile_pos = [self.pos[0] + self.radius * forward[0], self.pos[1] + self.radius * forward[1]]
        missile_vel = [self.vel[0] + 12 * forward[0], self.vel[1] + 12 * forward[1]]
        a_missile = Sprite(missile_pos, missile_vel, self.angle, 0, img_missile, img_info_missile, msc_missile_shot)
        missile_group.add(a_missile)

    def get_position(self):
        """
        Возвращает текущую позицию ракеты.

        :return: Позиция ракеты в виде списка [x, y].
        """
        return self.pos

    def get_radius(self):
        """
        Возвращает радиус ракеты.

        :return: Радиус ракеты.
        """
        return self.radius

    def reset(self, new_position):
        """
        Сбрасывает состояние ракеты в начальное, устанавливая новую позицию.

        :param new_position: Новая позиция ракеты.
        """
        self.pos = new_position
        self.vel = [0, 0]
        self.angle = 0
        self.angle_vel = 0
        self.thrust = False
        self.set_thrust(self.thrust)
