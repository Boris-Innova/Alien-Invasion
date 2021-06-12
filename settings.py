import pygame

class Settings():
	"""Инициализирует статические настройки игры."""
	def __init__(self):
		
		# Размер и цвет экрана.
		self.screen_width = 1500
		self.screen_height = 750
		self.rgb_color = (0,0,0)
	
		# Скорость передвижения корабля и количество жизней.
		self.speed_ship = 7
		self.ship_limit = 3
	
		# Скорость пули.
		self.bullet_speed = 8
		self.bullet_allowed = 5
		
		# Настройки пришельцев.
		self.alien_speed = 3
		self.alien_points = 50
