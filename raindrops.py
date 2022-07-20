import sys
import pygame
from raindrop import Rain


class Raindrop:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

        pygame.display.set_caption("Raindrops")

        # rain
        self.rain_drops = pygame.sprite.Group()

        self._create_raindrops()
        # self._check_raindrops_edges()

    def let_it_rain(self):

        while True:

            self._check_events()
            self.rain_drops.update()
            self._check_raindrops_edges()

            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        self.screen.fill((230, 230, 230))
        self.rain_drops.draw(self.screen)
        pygame.display.flip()

    def _create_raindrops(self):
        """Create the group of raindrops"""
        rain = Rain(self)
        rain_width, rain_height = rain.rect.size
        available_space_x = self.screen.get_rect().width - rain_width
        self.number_rain_x = available_space_x // rain_width

        available_space_y = self.screen.get_rect().height - (5 * rain_height)
        num_rows = available_space_y // (rain_height)

        # Create the full group of raindrops
        for row_number in range(num_rows):
            for rain in range(self.number_rain_x):
                self._create_raindrop(rain, row_number)

    # In order for me to fix the raindrop number 2 problem i need to create a still grid of raindrops to make sure theres space between the top and the bottom of the screen
    # so when the new row comes it has space to fill in and it doesnt overlap
    def _create_raindrop(self, rain_number, row_number):
        """Create the raindrop"""

        rain = Rain(self)
        rain_width, rain_height = rain.rect.size
        rain.x = rain_width*2  * rain_number
        rain.y = rain_height + 2 * rain_height * row_number
        rain.rect.x = rain.x
        rain.rect.y = rain.y
        self.rain_drops.add(rain)

    def _check_raindrops_edges(self):
        """respond if raindrop falls below screen"""
        for rain in self.rain_drops.copy():
            if rain._check_edges():
                self.rain_drops.remove(rain)
                self._create_single_row()
                break;

    def _create_single_row(self):

        for rain in range(self.number_rain_x):
            self._create_raindrop(rain, 0)
            print('new')


if __name__ == '__main__':
    # Make a game instance, and run the game
    rain = Raindrop()
    rain.let_it_rain()
