import sys
import pygame

from settings import settings

def run_game():
	#Initialize game and create a screen object
	pygame.init()
	
	ai_settings = Settings()

	# screen = pygame.display.set_mode((1200, 800)) but we pull from Class:
	screen = pygame.display.set_mode(
		(ai_settings.screen_width, ai_settings.screen_height))
	
	pygmae.display.set_caption("Alien Invasion")

	# Start the main loop for the game
	while True:

		# Watch for keywobard andmouse events
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

		# Redraw the screen during each pass through the loop
		screen.fill(ai_settings.bg_color)


		# Make the most recently drawn screen visible
		pygame.display.flip()

run_game()
