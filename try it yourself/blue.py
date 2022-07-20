import sys
import pygame

class Rocket:

	def __init__(self):
		"""Make a screenn"""
		pygame.init()
	
		#screen settings
		self.screen = pygame.display.set_mode((1200, 800))
		self.bg_color= (2, 2, 2)
		pygame.display.set_caption('Marlon head')
		self.screen_rect = self.screen.get_rect()

		#load ship
		self.image = pygame.image.load('images/marlon.bmp')
		self.rect = self.image.get_rect()
		#position ship
		self.rect.center = self.screen_rect.center
		#draw ship
		self.screen.blit(self.image, self.rect)
	def run_game(self):
		while True:
			self._check_events()
			self._update_screen()

	def _check_events_(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
					sys.exit()
			elif event.type == pygame.KEYDOWN:
					print(event.key)

	def _update_screen(self):
		"""Update images on the screen, and flip to the new screen"""	
		self.screen.fill(self.bg_color)
		self.screen.blit(self.image, self.rect)
			
		pygame.display.flip()
	def rocket(self, ai_game):
		self.screen = ai_game.screen
		self.screen_rect = ai_game.get_rect()
		self.settings = ai_game.settings 



if __name__ == '__main__':
	ai = Rocket()
	ai.run_game()
