import pygame.font
from pygame.sprite import Group
from ship import Ship

class ScoreBoard():
	"""Класс для вывода игровой информации."""
	def __init__(self, settings, screen, stats, asteroids):
		"""Инициализирует атрибуты подсчета очков."""
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.settings = settings
		self.stats = stats
		self.asteroids = asteroids
		
		# Настройки шрифта для вывода счета.
		self.text_color = (255, 255, 255)
		self.font = pygame.font.SysFont(None, 48)
		
		# Создает изображения счета очков, уровня и жизней.
		self.create_score()
		self.create_level(0)
		self.health_of_ship()
		
	def create_score(self):
		"""Преобразует счет(число) в графическое изображение."""
		rounded_score = int(round(self.stats.score, -1))
		score_str = "{:,}".format(rounded_score)
		self.score_image = self.font.render(score_str, True, self.text_color, self.settings.rgb_color)
		
		# Вывод счета в правой верхней части экрана.
		self.score_rect = self.score_image.get_rect()
		self.score_rect.right = self.screen_rect.right
		self.score_rect.top = self.screen_rect.top
	
		
	def create_level(self, number):
		"""Преобразует уровень(число) в графическое изображение."""
		self.level_image = self.font.render(str(number), True, self.text_color, self.settings.rgb_color)
		# Уровень выводится под текущим счетом.
		self.level_rect = self.level_image.get_rect()
		self.level_rect.right = self.score_rect.right
		self.level_rect.top = self.score_rect.bottom
	
		
	def health_of_ship(self):
		"""Сообщает количество оставшихся кораблей."""
		self.ships = Group()
		for ship_number in range(self.stats.ship_left):
			ship = Ship(self.settings, self.screen)
			ship.rect.x = 10 + ship_number * ship.rect.width
			ship.rect.y = 10
			self.ships.add(ship)
			del ship

	
	def show_score(self):
		"""Выводит изображение счета, уровня и жизней корабля на экран."""
		self.screen.blit(self.score_image, self.score_rect)
		self.screen.blit(self.level_image, self.level_rect)
		self.ships.draw(self.screen)	
		
