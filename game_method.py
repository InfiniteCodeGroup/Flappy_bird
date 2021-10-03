import pygame, random
def draw_footer(screen,footer_image,footer_x_pos):
	screen.blit(footer_image, (footer_x_pos, 580))
	screen.blit(footer_image, (footer_x_pos + 576, 580))

def create_pipe(pipe_image,pipe_height):
	rand_pipe_y = random.choice(pipe_height)
	bottom_pipe = pipe_image.get_rect(midtop=(650,rand_pipe_y))
	top_pipe = pipe_image.get_rect(midbottom=(650,rand_pipe_y-180))
	return bottom_pipe, top_pipe

def move_pipe(pipes):
	for pipe in pipes:
		pipe.centerx -= 5
	return pipes

def draw_pipes(screen,pipe_image,pipes):
	for pipe in pipes:
		if pipe.centery >= 340:

			screen.blit(pipe_image,pipe)
		else:
			flip_pipe = pygame.transform.flip(pipe_image, False, True)
			screen.blit(flip_pipe,pipe)

def check_collision(bird_rect,pipes):
	for pipe in pipes:
		if bird_rect.colliderect(pipe):
			return False
	if bird_rect.top <= -100 or bird_rect.bottom >= 600:
		return False
	
	return True
def rotate_bird(bird_image,bird_move):
	new_bird = pygame.transform.rotozoom(bird_image, bird_move*3,1)
	return new_bird

def bird_animation(bird_list,bird_index,bird_rect):
	new_bird = bird_list[bird_index]
	bird_rect_new = new_bird.get_rect(center=(100,bird_rect.centery))

	return new_bird, bird_rect_new

	