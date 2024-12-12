class ImageInfo:
    """
    Класс, представляющий информацию об изображении.

    :param center: Центр изображения (x, y).
    :param size: Размер изображения (ширина, высота).
    :param radius: Радиус изображения (по умолчанию 0).
    :param lifespan: Продолжительность жизни изображения (по умолчанию бесконечность).
    :param animated: Флаг, указывающий, является ли изображение анимированным (по умолчанию False).
    """
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
        """Возвращает центр изображения."""
        return self.center

    def get_size(self):
        """Возвращает размер изображения."""
        return self.size

    def get_radius(self):
        """Возвращает радиус изображения."""
        return self.radius

    def get_lifespan(self):
        """Возвращает продолжительность жизни изображения."""
        return self.lifespan

    def get_animated(self):
        """Возвращает флаг, указывающий, является ли изображение анимированным."""
        return self.animated
