import pygame

from src.assets.images.img_info import icon


if __name__ == "__main__":
    pygame.init()
    pygame.mixer.init()

    pygame.display.set_caption("Asteroids")
    pygame.display.set_icon(icon)

    from src.game import game
    game()
