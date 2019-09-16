import sys
import pygame

def run_game():
	#Initialize game and create a screen object
	pygame.init()
	screen = pygame.display.set_mode((1200,800))
	pygmae.display.set_caption("Alien Invasion")

	# Start the main loop for the game
	while True:

		# Watch for keywobard andmouse events
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

		# Make the most recently drawn screen visible
		pygame.display.flip()

run_game()
