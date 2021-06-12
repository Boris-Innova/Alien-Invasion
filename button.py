import pygame.font

class Button():
	"""Класс, представляющий изображение кнопки."""
	
	def __init__(self, settings, screen, i, message):
		"""Инициализирует атрибуты кнопки."""
		self.settings = settings
		self.screen = screen
		self.message = message
		self.i = i
		
		# Загрузка изображения кнопки и назначение атрибуты rect.
		self.button = pygame.image.load('Finished_image/Interface/buttonBlue.png')
		self.button = pygame.transform.scale(self.button, (300, 75))
		self.button.set_colorkey((0, 0, 0))
		self.button_rect = self.button.get_rect()
		self.screen_rect = screen.get_rect()
		
		# Атрибуты текста.
		self.text_color = (0, 0, 0)
		self.font = pygame.font.SysFont(None, 48)
		
		# Задает координаты кнопке.
		self.button_rect.centerx = self.screen_rect.centerx 
		self.button_rect.centery = self.screen_rect.centery + i*100 - 108
		
		# Сообщение кнопки.
		self.create_message(message)
	
	def create_message(self, message):
		"""Преобразует message в прямоугольник и выравнивает по центру."""
		self.message = self.font.render(message, True, self.text_color)
		self.message_rect = self.message.get_rect()
		self.message_rect.center = self.button_rect.center
	
	def draw_button(self):
		"""Рисует кнопку в нужной позиции."""
		self.screen.blit(self.button, self.button_rect)
		self.screen.blit(self.message, self.message_rect)
