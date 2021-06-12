import pygame
import pygame.font
from pygame.sprite import Sprite
from pygame.sprite import Group

class Asteroid(Sprite):
	"""Класс, представляющий один астероид."""
	
	def __init__(self, settings, screen, level_number):
		"""Инициализация атрибутов астероида."""
		super(Asteroid, self).__init__()
		self.settings = settings
		self.screen = screen
		self.level = level_number
		self.asteroids = Group()
		
		# Загрузка изображения астероида и назначения атрибута rect.
		self.image = pygame.image.load('Finished_image/Asteroids/asteroid_1.png')
		self.image = pygame.transform.scale(self.image, (100, 100))
		self.image.set_colorkey((255, 255, 255))
		self.rect = self.image.get_rect()
		
		# Задает координаты астероиду.
		self.rect.x = self.rect.left + (1/6)*settings.screen_width
		self.rect.y = self.rect.top  + 200
