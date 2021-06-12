import pygame.font

class Picture():
	
	def __init__(self, settings, screen, i):
		"""Инициализрует атрибуты кнопки и задает положение."""
		self.screen = screen
		self.settings = settings
		self.i = i
		
		
		# Загрузка изображения и получение прямоугольника.
		if i == 1:
			self.menu = pygame.image.load('Finished_image/Interface/main_menu.bmp')
			self.menu = pygame.transform.scale(self.menu, (500, 700))
			self.menu.set_colorkey((255, 255, 255))
			self.menu.set_colorkey((0, 0, 0))
			self.rect = self.menu.get_rect()
			self.screen_rect = screen.get_rect()
			
			# Задает координаты изображению.
			self.rect.centerx = self.screen_rect.centerx
			self.rect.centery = self.screen_rect.centery
		
		if i == 2:
			self.select_level = pygame.image.load('Finished_image/Interface/select_level.jpg')
			self.select_level = pygame.transform.scale(self.select_level, (500, 125))
			self.select_level.set_colorkey((255, 255, 255))
			self.rect = self.select_level.get_rect()
			self.screen_rect = screen.get_rect()
			
			# Задает координаты изображению.
			self.rect.centerx = self.screen_rect.centerx
			self.rect.centery = self.screen_rect.top + 100
			
		if i == 3:
			self.image_pause = pygame.image.load('Finished_image/Interface/pause.jpg')
			self.image_pause = pygame.transform.scale(self.image_pause, (640, 360))
			self.rect = self.image_pause.get_rect()
			self.screen_rect = screen.get_rect()
			
			# Задает координаты изображению.
			self.rect.centerx = self.screen_rect.centerx
			self.rect.centery = self.screen_rect.centery
			
		
	
	def blitme(self, i):
	 """Рисует изображение в нужной позиции."""
	 if i == 1:
		 self.screen.blit(self.menu, self.rect)
	 if i == 2:
		 self.screen.blit(self.select_level, self.rect)	 
	 if i == 3:
		 self.screen.blit(self.image_pause, self.rect)
