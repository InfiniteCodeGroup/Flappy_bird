import pygame
from game_method import draw_footer, create_pipe, move_pipe, draw_pipes, check_collision,rotate_bird, bird_animation

def main():
	pygame.init()
	screen = pygame.display.set_mode((576,710))
	pygame.display.set_caption('Flappy Bird')

	clock = pygame.time.Clock()
	scale = 0.29
	bird_move = 0

	# background
	bg_image = pygame.image.load('background-night.png').convert()
	bg_image = pygame.transform.scale2x(bg_image)

	# footer
	footer_image = pygame.image.load('land.png').convert()
	footer_image = pygame.transform.scale2x(footer_image)

	# bird
	bird_image_midflap = pygame.image.load('b1.png').convert_alpha()
	bird_image_midflap = pygame.transform.scale2x(bird_image_midflap)
	
	bird_image_downflap = pygame.image.load('b2.png').convert_alpha()
	bird_image_downflap = pygame.transform.scale2x(bird_image_downflap)
	
	bird_image_upflap = pygame.image.load('b3.png').convert_alpha()
	bird_image_upflap = pygame.transform.scale2x(bird_image_upflap)
	

	bird_list = [bird_image_downflap, bird_image_midflap, bird_image_upflap]

	bird_index = 0
	bird_image = bird_list[bird_index]


	BIRDMAKKER = pygame.USEREVENT = 1
	pygame.time.set_timer(BIRDMAKKER,200)

	bird_rect = bird_image.get_rect(center=(100, 250))

	# Pipe - to'siq
	pipe_image = pygame.image.load('pipe_t.png')
	pipe_image = pygame.transform.scale2x(pipe_image)

	list_pipe = []
	PIPEMAKER = pygame.USEREVENT
	pygame.time.set_timer(PIPEMAKER,1200)
 

	# game variable
	footer_x_pos = 0
	pipe_height = [200,210,220,230,240,250,265,275,290,300,325]
	game_type = True

	while True:   
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					bird_move = 0
					bird_move -= 5   
				if event.key == pygame.K_SPACE and game_type == False:
					game_type = True
					list_pipe.clear()
					bird_rect.center = (100,250)
					bird_move = 0
			if event.type == PIPEMAKER:
				list_pipe.extend(create_pipe(pipe_image,pipe_height))
				# print(list_pipe)
			if event.type == BIRDMAKKER:
				if bird_index < 2:

					bird_index += 1
				else:
					bird_index = 0 
				bird_image, bird_rect = bird_animation(bird_list,bird_index,bird_rect)
		# background
		screen.blit(bg_image, (0, -350))

		if game_type:

			# bird
			bird_move += scale
			rotated_bird = rotate_bird(bird_image,bird_move)
			bird_rect.centery += bird_move
			screen.blit(rotated_bird, bird_rect)
			
			# Pipe = to'siqlar
			list_pipe = move_pipe(list_pipe)
			draw_pipes (screen,pipe_image,list_pipe)

		game_type=check_collision(bird_rect,list_pipe)

		# footer
		footer_x_pos -= 1
		draw_footer(screen,footer_image,footer_x_pos)
		if footer_x_pos <= -576:
			footer_x_pos = 0



		pygame.display.update()
		clock.tick(90)

if __name__ == '__main__':
	main()