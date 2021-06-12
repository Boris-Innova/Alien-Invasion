import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
	
 def __init__(self, settings, screen ):
	 """Инициализирует корабль и задает его начальную позицию."""
	 super(Ship, self).__init__()
	 self.screen = screen
	 self.settings = settings
	 
	 # Загрузка изображения корабля и получение прямоугольника.
	 self.image = pygame.image.load('Finished_image/Ships/ship_0.bmp')
	 self.image.set_colorkey((255,255,255))
	 self.rect = self.image.get_rect()
	 self.screen_rect = screen.get_rect()
	 
	 # Задает координаты кораблю.
	 self.rect.centerx = self.screen_rect.centerx
	 self.rect.centery = self.screen_rect.bottom - 40
	 
	 # Сохранение вещественной координаты центра корабля.
	 self.centerx = float(self.rect.centerx)
	 self.centery = float(self.rect.centery)
	 # Флаг перемещения
	 self.moving_right = False
	 self.moving_left = False
	 self.moving_top = False
	 self.moving_bottom = False
	  
	 
 def update(self):
	 """Обновляет позицию корабля с учетом флага."""
	 
	 # Обновляется атрибут centerx и centery, не rect.
	 if (self.moving_left == True) and (self.rect.left > self.screen_rect.left):
		 self.centerx -= self.settings.speed_ship
		 
	 if (self.moving_right == True) and (self.rect.right < self.screen_rect.right):
		 self.centerx += self.settings.speed_ship
		 
	 if (self.moving_top == True) and (self.rect.top > self.screen_rect.top):
		 self.centery -= self.settings.speed_ship
	 
	 if (self.moving_bottom == True) and (self.rect.bottom < self.screen_rect.bottom):
		 self.centery += self.settings.speed_ship
	 # Обновление атрибута rect на основании self.center
	 self.rect.centerx = self.centerx
	 self.rect.centery = self.centery
		
 def blitme(self):
	 """Рисует корабль в текущей позиции."""
	 self.screen.blit(self.image, self.rect)
	 	 
	 
 def center_ship(self):
	 """Перемещает корабль в центр."""
	 self.centerx = self.screen_rect.centerx
	 self.centery = self.screen_rect.bottom -40
