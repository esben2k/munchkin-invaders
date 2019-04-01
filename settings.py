#settings.py
class Settings():
	""" """

	def __init__(self):
		"""initialize game and screen settings."""
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (135, 206, 250)

		#ship speed settings
		self.ship_limit = 3#numer of space ships per game

		# Bullet settings
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 60, 60, 60

		#Alien settings
		self.fleet_drop_speed = 10
		
		# How quickly the game speeds up
		self.speedup_scale = 1.2
		# How quickly the alien point value increases
		self.score_scale = 1.5
		self.initialize_dynamic_settings()

	def initialize_dynamic_settings(self):
		"""Init settings that change during the game"""

		self.ship_speed = 1.5#move 1.5 pixels per movement
		self.bullet_speed = 5
		self.alien_speed_factor = 1

		#fleet directior of 1 represents right, -1 represents left
		self.fleet_direction = 1

		#scoring
		self.alien_points = 100

	def increase_speed(self):
		"""Increase speed settings and alien point values"""
		self.ship_speed *= self.speedup_scale
		self.bullet_speed *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale
		self.alien_points = int(self.alien_points * self.score_scale)

