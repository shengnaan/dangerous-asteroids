from config import Settings
from src.assets.images.img_info import imgMissile, imgInfoMissile
from src.assets.sounds.sounds_info import mscSpaceRocketThrust, mscMissileShot
from src.sprite import Sprite
from src.utils.helpers import draw_on_screen, angle_to_vector


class SpaceRocket:
    def __init__(self, pos, vel, angle, image, image_thrust, info):
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
        if self.thrust:
            draw_on_screen(screen, self.image_thrust, self.image_center, self.image_size, self.pos, self.image_size,
                           self.angle)
        else:
            draw_on_screen(screen, self.image, self.image_center, self.image_size, self.pos, self.image_size,
                           self.angle)

    def update(self):
        self.angle += self.angle_vel

        self.pos[0] = (self.pos[0] + self.vel[0]) % Settings.WIDTH
        self.pos[1] = (self.pos[1] + self.vel[1]) % Settings.HEIGHT

        if self.thrust:
            acc = angle_to_vector(-self.angle)
            self.vel[0] += acc[0] * .1
            self.vel[1] += acc[1] * .1

        self.vel[0] *= .98
        self.vel[1] *= .98

    def set_thrust(self, on):
        self.thrust = on
        if on:
            mscSpaceRocketThrust.play()
        else:
            mscSpaceRocketThrust.stop()

    def increment_angle_vel(self):
        self.angle_vel -= .05

    def decrement_angle_vel(self):
        self.angle_vel += .05

    def shoot(self, missile_group):
        forward = angle_to_vector(-self.angle)
        missile_pos = [self.pos[0] + self.radius * forward[0], self.pos[1] + self.radius * forward[1]]
        missile_vel = [self.vel[0] + 6 * forward[0], self.vel[1] + 6 * forward[1]]
        a_missile = Sprite(missile_pos, missile_vel, self.angle, 0, imgMissile, imgInfoMissile, mscMissileShot)
        missile_group.add(a_missile)

    def get_position(self):
        return self.pos

    def get_radius(self):
        return self.radius
