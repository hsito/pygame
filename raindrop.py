import pygame
from pygame.sprite import Sprite


class Rain(Sprite):
    """A class that represents a single raindrop"""

    def __init__(self, raindrops):
        """Initialize the raindrop and set its starting position"""
        super().__init__()
        self.screen = raindrops.screen

        self.image = pygame.image.load('images/raindrop.jpg')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.y = float(self.rect.y)

    def update(self):
        """Make it rain!!!"""
        self.y += .5
        self.rect.y = self.y

    def _check_edges(self):
        """Return True if raindrop is at edge of screen"""

        if self.rect.top > self.screen.get_rect().bottom:

            print('rain out')
            self.reset_drop()
        else:
            return False

    def reset_drop(self):
        self.rect.y = self.rect.height
        self.y = float(self.rect.y)