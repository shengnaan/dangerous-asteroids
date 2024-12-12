
if __name__ == "__main__":
    import pygame
    pygame.init()
    pygame.mixer.init()

    from src.utils.resources import icon
    pygame.display.set_caption("Asteroids")
    pygame.display.set_icon(icon)

    from src.game import game
    game()
