import pygame

class Background():
	"""Класс, представляющий изображение фона."""

	def __init__(self, settings, screen, i):
		"""Инициализирует атрибуты."""
		self.settings = settings
		self.screen = screen
		self.i = i
		
		# Загрузка изображения и изменение его размеров.
		if self.i == 1:
			filename = 'Finished_image/Backgrounds/space.jpg'
			
		if self.i == 2:
			filename = 'Finished_image/Backgrounds/background_1.jpg'
			
		if self.i == 3:
			filename = 'Finished_image/Backgrounds/background_2.jpg'
			
		self.background = pygame.image.load(filename)	
		self.background = pygame.transform.scale(self.background, (settings.screen_width, settings.screen_height))
		self.background_rect = self.background.get_rect()
		
		
	def draw_background(self):
		"""Прорисовка фона."""
		self.screen.blit(self.background, self.background_rect)
