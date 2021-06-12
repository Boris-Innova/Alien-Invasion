import pygame
import pygame.font
from pygame.sprite import Sprite
from pygame.sprite import Group

class Number(Sprite):
	"""Класс, представляющий изображения номера астероида."""
	
	def __init__(self, settings, screen, i):
		"""Инициализация атрибутов астероида."""
		super(Number, self).__init__()
		self.settings = settings
		self.screen = screen
		self.i = i
		self.numbers_1 = Group()
		
		# Загрузка изображения астероида и назначения атрибута rect.
		self.image = pygame.image.load('Finished_image/numerals/numeral' + str(i) + '.png')
		self.image = pygame.transform.scale(self.image, (50, 50))
		self.image.set_colorkey((0, 0, 0))
		self.rect = self.image.get_rect()
		
		# Задает координаты астероиду.
		self.rect.x = self.rect.left + (1/6)*settings.screen_width
		self.rect.y = self.rect.top  + 200
	
	def blitme(self):
		self.screen.blit(self.image, self.rect)
