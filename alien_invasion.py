import pygame

from settings import Settings
from ship import Ship
from pygame.sprite import Group
from background import Background
import game_functions as gf
from game_stats import GameStats
from button import Button
from picture import Picture
from scoreboard import ScoreBoard
from asteroid import Asteroid

def start_game():
	# Инициализирует  pygame, settings и объект экрана.
	pygame.init()
	settings = Settings()
	screen = pygame.display.set_mode( (settings.screen_width, settings.screen_height))
	pygame.display.set_caption("Space battle")
	
	# Создание экземпляра фона игры.
	background_1 = Background(settings, screen, 1)
	background_2 = Background(settings, screen, 2)
	background_3 = Background(settings, screen, 3)
	backgrounds = [background_1, background_2, background_3]
	
	# Установка FPS.
	FPS = pygame.time.Clock()
	pygame.mixer.music.load('Голая.mp3')
	pygame.mixer.music.play()
	
	# Создание экземпляра Picture.
	main_menu = Picture(settings, screen, 1)
	select_level = Picture(settings, screen, 2)
	pause = Picture(settings, screen, 3)
	
	# Создание кнопки Play, Settings, Developers, Exit.
	play_button = Button(settings, screen, 1, "Play")
	settings_button = Button(settings, screen, 2, "Settings")
	develop_button = Button(settings, screen, 3, "Developers")
	exit_button = Button(settings, screen, 4, "Exit")
	buttons = [play_button, settings_button, develop_button, exit_button]
		
	# Создание корабля.
	ship = Ship(settings,screen)
	
	# Создание групп для хранения пуль, пришельцев, астероидов, чисел.
	bullets = Group()
	aliens = Group()
	asteroids = Group()
	number_level = Group()
	
	# Создание экземпляров GameStats и ScoreBoard.
	stats = GameStats(settings)	
	score_b = ScoreBoard(settings, screen, stats, asteroids)
	
	
	# Создание группы астероидов.	
	gf.create_asteroids(settings, screen, stats, asteroids, number_level)
	
	# Запуск основного цикла игры.
	while True:
		# Отслеживание событий клавиатуры и мыши.
		gf.check_events(settings, screen, stats, score_b, buttons, ship, aliens, bullets, asteroids, pause)
		# При каждом проходе цикла перерисовывается экран.
		# Отображение последнего прорисованного экрана.
		gf.update_screen(settings, screen, stats, score_b, ship, aliens, bullets, buttons, backgrounds, main_menu, asteroids, number_level, select_level, pause)
		FPS.tick(100)	
		if (stats.game_active == True) and (stats.select_active == False) and (stats.pause_active == False):
			ship.update()
			# Изменение позиции пули и удаление пуль, вышедших за край экрана.
			gf.update_bullets(settings, screen, stats, score_b, ship, aliens, bullets)
			gf.update_aliens(settings, screen, stats, score_b,  ship, aliens, bullets)	

start_game()
