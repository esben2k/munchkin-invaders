#game_stats.py

class GameStats():
	"""Track stats for invaders from Python"""
	def __init__(self, infrompy_settings):
		#init
		self.infrompy_settings = infrompy_settings
		self.reset_stats()

		#Start the game in an inactive state
		self.game_active = False

		#high scpre should never be reset
		self.high_score = 0

	def reset_stats(self):
		#init stats that can change during game
		self.ships_left = self.infrompy_settings.ship_limit
		self.score = 0
		self.level = 1
