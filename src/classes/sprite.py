from config import Settings
from src.utils.helpers import draw_on_screen, dist


class Sprite:
    def __init__(self, pos, vel, ang, ang_vel, image, info, sound=None):
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
        return self.pos

    def get_radius(self):
        return self.radius

    def collide(self, object2):
        r1 = self.get_radius()
        r2 = object2.get_radius()

        pos1 = self.get_position()
        pos2 = object2.get_position()
        return dist(pos1, pos2) < (r1 + r2)

    def draw(self, screen):
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
        self.angle += self.angle_vel

        self.pos[0] = (self.pos[0] + self.vel[0]) % Settings.WIDTH
        self.pos[1] = (self.pos[1] + self.vel[1]) % Settings.HEIGHT

        self.age += 1

        return self.age >= self.lifespan
