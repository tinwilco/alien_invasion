import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """an alien in the fleet"""

    def __init__(self, ai_game) -> None:
        super().__init__()
        self.screen = ai_game.screen

        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # start at top left
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # exact horizontal
        self.x = float(self.rect.x)

        self.settings = ai_game.settings

    def update(self):
        self.x += (self.settings.alien_speed*self.settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
