class GameStats():
	"""Класс для отслеживания статистики игры Alien Invasion."""
	
	def __init__(self, settings):
		"""Инициализирует статистику."""
		self.settings = settings
		self.reset_stats()
		
		# Игра Alien Invasion запускается в активном состоянии.
		self.game_active = False
		self.select_active = False
		self.pause_active = False
		
		# Рекорд не должен сбрасываться.
		#self.high_score = 0
		
	
	def reset_stats(self):
		"""Инициализирует статистику, изменяющуюся в ходе игры."""
		self.ship_left = self.settings.ship_limit
		self.score = 0
		
