#invaders_from_python.py

import sys
import pygame
from pygame.sprite import Group

#import class 'Settings' from settings.py
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard 
from button import Button


#import class 'Ship' from ship.py
from ship import Ship
from alien import Alien 


#import game_functions.py
import game_functions as gf


def run_game():
	"""Initialize game and create a screen object"""
	pygame.init()
	infrompy_settings = Settings()
	screen = pygame.display.set_mode((infrompy_settings.screen_width, infrompy_settings.screen_height))#1200,800 is a tuple
	pygame.display.set_caption("Munchkin Invaders")

	#make a play button
	play_button = Button(infrompy_settings, screen, "Play")

	#Create an instance to store game stats and create a scoreboard
	stats = GameStats(infrompy_settings)
	sb = Scoreboard(infrompy_settings, screen, stats)

	#Make a ship, a group of bullets and a group of aliens
	# Create a ship, pass 'screen' parameter
	#create ship before main loop so that we dont create a new ship on each pass
	ship = Ship(infrompy_settings, screen)
	# Make a group to store bullets in
	bullets = Group()
	#Make an alien
	#alien = Alien(infrompy_settings, screen)
	aliens = Group()

	# create fleet of aliens
	gf.create_fleet(infrompy_settings, screen, ship, aliens)


	# Start main loop for the game.
	while True:
		#refactored from game_functions.py
		gf.check_events(infrompy_settings, screen, stats,sb, play_button, ship, aliens, bullets)

		if stats.game_active:
			ship.update()
			gf.update_bullets(infrompy_settings, screen, stats, sb, ship, aliens, bullets)
			gf.update_aliens(infrompy_settings, stats, sb, screen, ship, aliens, bullets)
		gf.update_screen(infrompy_settings, screen, stats, sb, ship, aliens, bullets, play_button)
	

run_game()
