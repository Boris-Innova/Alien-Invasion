import pygame
from pygame.sprite import Sprite
from pygame.sprite import Group


class Alien(Sprite):
	"""Класс, представляющий одного пришельца."""
	
	def __init__(self, settings, screen, i):
		"""Инициализирует пришельца и задает его начальную позицию."""
		super(Alien, self).__init__()
		self.screen = screen
		self.settings = settings
		self.i =  i
		self.aliens = Group()
		
		# Загрузка изображения пришельца и назначение атрибута rect.
		self.image = pygame.image.load('Finished_image/Ships_of_Alien/alien_0.bmp')
		self.image.set_colorkey((255,255,255))
		self.rect = self.image.get_rect()
		
		# Задает координаты пришельцу.
		self.rect.x = self.rect.width
		self.rect.y = self.rect.top - 300*i

		# Сохранение точной позиции пришельца.
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)
		
	def blitme(self):
		"""Выводит пришельца в текущем положении"""
		self.screen.blit(self.image, self.rect)
		


	def update(self):
		"""Изменяет позицию пришельца."""
		#self.x += 10
		#self.rect.x = self.x
		
		self.y += self.settings.alien_speed
		self.rect.y = self.y


	def check_edges(self):
		"""Возвращает True, если пришелец находится у края экрана."""
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right:
			return True
		elif self.rect.left <= 0:
			return True
