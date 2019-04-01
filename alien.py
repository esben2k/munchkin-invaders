#alien.py

import pygame

from pygame.sprite import Sprite

class Alien(Sprite):
	"""A class to represent a single alien"""

	def __init__(self,infrompy_settings, screen):
		"""initialize the alien and its starting position"""
		super(Alien, self).__init__()
		self.screen = screen
		self.infrompy_settings = infrompy_settings

		#load the alien image and set its rect
		self.image = pygame.image.load('images\\alien5.png').convert_alpha()
		self.image.set_colorkey((255,255,255))

		self.rect = self.image.get_rect()

		#start each new alien near the top left of the screen
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		#store the aliens exact position
		self.x = float(self.rect.x)

	def blitme(self):
		"""draw the alien at its current position"""
		self.screen.blit(self.image, self.rect)
		
	def check_edges(self):
		"""Return true if alien is at the edge of the screen"""
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right:
			return True
		elif self.rect.left <= 0:
			return True


	def update(self):
		"""Move the aliens right or left"""
		self.x += (self.infrompy_settings.alien_speed_factor * self.infrompy_settings.fleet_direction)
		self.rect.x = self.x
