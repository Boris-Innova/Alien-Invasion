import pygame

from pygame.sprite import Sprite
from pygame.sprite import Group

class Bullet(Sprite):
	"""Класс для управления пулями, выпущенными кораблем."""
	def __init__(self, settings, screen, ship):
		"""Создает объект пули в текущей позиции корабля."""
		super(Bullet, self).__init__()
		self.screen = screen
		self.bullets = Group()
		
		# Загрузка изображения пули и назначение координат.
		self.bullet = pygame.image.load('Finished_image/Bullets/laserRed.png')
		self.bullet.set_colorkey((255, 255, 255))
		self.rect = self.bullet.get_rect()
		
		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top
		
		# Позиция пули хранится в вещественном формате.
		self.y = float(self.rect.y)
		self.b_speed = settings.bullet_speed
		
	
	def update(self):
		"""Перемещает пулю вверх по экрану."""
		
		# Обновление позиции пули в вещественном формате.
		self.y -= self.b_speed
		
		# Обновление позиции прямоугольника.
		self.rect.y = self.y
			
			
	def draw_bullet(self):
		"""Вывод пули на экран."""
		self.screen.blit(self.bullet, self.rect)
