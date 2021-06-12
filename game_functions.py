import sys

import pygame

from background import Background
from bullet import Bullet
from alien import Alien
from ship import Ship
from asteroid import Asteroid
from numbers_1 import Number
from time import sleep

from random import randint
import random


########################################################################
"""Фунции обрабатывающие нажатие клавиш."""
########################################################################

def check_keydown_events(event, settings, screen, stats, ship, bullets):   
	"""Реагирует на нажатие клавиш."""
	
	if event.key == pygame.K_RIGHT:
		# Переместить корабль вправо.
		ship.moving_right = True
					
	elif event.key == pygame.K_LEFT:
		# Переместить корабль влево.
		ship.moving_left = True
	
	elif event.key == pygame.K_UP:
		# Переместить корабль вверх.
		ship.moving_top = True
	
	elif event.key == pygame.K_DOWN:
		# Переместить корабль вниз.
		ship.moving_bottom = True
		
	if event.key == pygame.K_d:
		# Переместить корабль вправо.
		ship.moving_right = True
					
	elif event.key == pygame.K_a:
		# Переместить корабль влево.
		ship.moving_left = True
	
	elif event.key == pygame.K_w:
		# Переместить корабль вверх.
		ship.moving_top = True
	
	elif event.key == pygame.K_s:
		# Переместить корабль вниз.
		ship.moving_bottom = True	
		
	if event.key == pygame.K_SPACE:
		if stats.pause_active == False:
			# Создание новой пули и включение ее в группу bullets.
			create_bullet(event,settings,screen,ship,bullets)
	
	if event.key == pygame.K_p:
		if stats.game_active == True:
			index = 0
			if (stats.pause_active == False) and (index == 0):
				stats.pause_active = True
				index += 1
				pygame.mouse.set_visible(True)
			
			if (stats.pause_active == True) and (index == 0):
				stats.pause_active = False
				pygame.mouse.set_visible(False)
		
	if event.key == pygame.K_q:
		sys.exit()
		
		
def check_keyup_events(event, settings, screen, ship, bullets):
	"""Реагирует на отпускание клавиш."""
	
	if event.key == pygame.K_RIGHT:
		# Переместить корабль вправо.
		ship.moving_right = False
					
	elif event.key == pygame.K_LEFT:
		# Переместить корабль влево.
		ship.moving_left = False	

	elif event.key == pygame.K_UP:
		# Переместить корабль вверх.
		ship.moving_top = False
		
	elif event.key == pygame.K_DOWN:
		# Переместить корабль вниз.
		ship.moving_bottom = False
	
	if event.key == pygame.K_d:
		# Переместить корабль вправо.
		ship.moving_right = False
					
	elif event.key == pygame.K_a:
		# Переместить корабль влево.
		ship.moving_left = False
	
	elif event.key == pygame.K_w:
		# Переместить корабль вверх.
		ship.moving_top = False
	
	elif event.key == pygame.K_s:
		# Переместить корабль вниз.
		ship.moving_bottom = False

		
def check_events(settings, screen, stats, score_b, buttons, ship, aliens, bullets, asteroids, pause):
	"""Обрабатывает нажатия клавиш и события мыши."""	
	
	for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			
			elif event.type == pygame.KEYDOWN:
				check_keydown_events(event, settings, screen, stats, ship, bullets)
			
			elif event.type == pygame.KEYUP:
				check_keyup_events(event, settings, screen, ship, bullets)
				
			elif event.type == pygame.MOUSEBUTTONDOWN:
				mouse_x, mouse_y = pygame.mouse.get_pos()
				if stats.pause_active == True:
					check_pause(settings, screen, stats, score_b, buttons, ship, aliens, bullets, asteroids, pause, mouse_x, mouse_y)
					
				if (stats.game_active == False) and (stats.select_active == True):
					check_level_button(settings, screen, stats, score_b, buttons, ship, aliens, bullets, asteroids, mouse_x, mouse_y)
					
				if (stats.game_active == False) and (stats.select_active == False):
					check_button(settings, screen, stats, score_b, buttons, ship, aliens, bullets, mouse_x, mouse_y)
				
							
def check_button(settings, screen, stats, score_b, buttons, ship, aliens, bullets, mouse_x, mouse_y):
	"""Обрабатывает нажатие одной из кнопок главного меню."""
	
	button_clicked = buttons[0].button_rect.collidepoint(mouse_x, mouse_y)
	if (button_clicked == True):
		stats.select_active = True

	button_settings = buttons[1].button_rect.collidepoint(mouse_x, mouse_y)
	if (button_settings == True):
		sys.exit()
			
	button_develop = buttons[2].button_rect.collidepoint(mouse_x, mouse_y)
	if (button_develop == True):
		sys.exit()
		
	button_exit = buttons[3].button_rect.collidepoint(mouse_x, mouse_y)
	if (button_exit == True):
		sys.exit()


def check_level_button(settings, screen, stats, score_b, buttons, ship, aliens, bullets, asteroids, mouse_x, mouse_y):
	"""Обрабатывает нажатие одной из кнопок уровня."""
	for item in asteroids.sprites():
		level_clicked = item.rect.collidepoint(mouse_x, mouse_y)
		if (level_clicked == True):
			stats.select_active = False
			stats.game_active = True
			print('ЗАПУСК УРОВНЯ ' + str(item.level) + ' ПРОШЕЛ  УСПЕШНО')
			# Скрывается указатель мыши.
			pygame.mouse.set_visible(False)
			# Сброс игровой статистики.
			stats.reset_stats()
			# Сброс изображений счетов и уровней.
			score_b.create_score()
			score_b.create_level(item.level)
			score_b.health_of_ship()	
			# Очистка списков пришельцев и пуль.
			aliens.empty()
			bullets.empty()
			# Создание нового флота.
			units = number_units(item.level)
			print("Количество пришельцев: " + str(units))
			create_fleet(settings, screen, ship, aliens, units, i)
			# Размещение корабля в центре.
			ship.center_ship()

def check_pause(settings, screen, stats, score_b, buttons, ship, aliens, bullets, asteroids, pause, mouse_x, mouse_y):
	"""Проверяет нажатие на кнопку 'Pause'."""
	pause_clicked = pause.rect.collidepoint(mouse_x, mouse_y)
	if pause_clicked == True:
		stats.pause_active = False
		pygame.mouse.set_visible(False)
		
			
########################################################################
"""Функции, создающие флот пришельцев и создание пули."""
########################################################################
def create_bullet(event, settings, screen, ship, bullets):
	"""Создание новой пули и включение ее в группу bullets."""
	if len(bullets) < settings.bullet_allowed:
		new_bullet = Bullet(settings, screen, ship)
		bullets.add(new_bullet)

def get_x(settings, alien_width):
	"""Получение координаты x для пришельца."""
	free_space = settings.screen_width
	return(randint(alien_width, free_space - alien_width))		
	
def create_alien(settings, screen, aliens, i):
	"""Создает одного пришельца."""
	alien = Alien(settings, screen, i)
	alien_width = alien.rect.width
	alien.x = get_x(settings, alien_width)
	alien.rect.x = alien.x
	aliens.add(alien)

def create_fleet(settings, screen, ship, aliens, units, i):
	"""Создание флота пришельцев."""
	alien = Alien(settings,screen, i)
	for i in range(1,units):
		create_alien(settings, screen, aliens, i)	
	
		
########################################################################
"""Функция, проверяющая достиг ли пришелец нижнего края экрана."""
########################################################################		

def check_bottom(settings, screen, stats, score_b, ship, aliens, bullets):
	"""Проверяет, добрались ли пришельцы до нижнего края экрана."""
	screen_rect = screen.get_rect()
	for alien in aliens.sprites():
		if alien.rect.bottom >= screen_rect.bottom:
			# Происходит тоже, что и при столкновении пришельца с кораблем.
			aliens.remove(alien)
			ship_hit(settings, screen, stats, score_b, ship, aliens, bullets)
			break


def check_high_score(stats, score_b):
	"""Проверяет появился ли новый рекорд."""
	if stats.score > stats.high_score:
		stats.high_score = stats.score
		score_b.prep_high_score()
		
			
########################################################################
"""Функции, отвечающие за обновление экрана."""
########################################################################	
							
def update_screen(settings, screen, stats, score_b, ship, aliens, bullets, buttons, backgrounds, main_menu, asteroids, numbers_1, select_level, pause):
	"""Обновляет изображения на экране и отображает новый экран."""
	
	# Отображается игра в активном состоянии.
	if (stats.game_active == True) and (stats.select_active == False):
		screen.fill(settings.rgb_color)
		backgrounds[0].draw_background()
		# Вывод счёта.
		score_b.show_score()
		for bullet in bullets.sprites():
			bullet.draw_bullet()	
		ship.blitme()
		aliens.draw(screen)
		if stats.pause_active == True:
			pause.blitme(3)
	
	# Отображается главное меню.
	if (stats.game_active == False) and (stats.select_active == False):
		backgrounds[1].draw_background()
		main_menu.blitme(1)
		for button in buttons:
			button.draw_button()
	
	# Отображается окно с выбором уровней.
	if (stats.game_active == False) and (stats.select_active == True):
		backgrounds[2].draw_background()
		select_level.blitme(2)
		asteroids.draw(screen)
		numbers_1.draw(screen)
		
	# Отображение последнего прорисованного экрана.
	pygame.display.flip()
	
	
def update_bullets(settings, screen, stats, score_b, ship, aliens, bullets):
	"""Обработка событий, связанных с пулей."""
	
	# Обновление позиции пули.
	bullets.update()

	# Удаление пуль, вышедших за край экрана.
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)
			
	check_collisions(settings, screen, stats, score_b, ship, aliens, bullets)


def check_collisions(settings, screen, stats, score_b, ship, aliens, bullets):
	"""Обработка коллизий пуль с пришельцами."""	
	
	# При обнаружении попадания пули в пришельца, удаляет пулю и пришельца.
	collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
	if collisions:
		for aliens in collisions.values():
			stats.score += settings.alien_points
			score_b.create_score()
			#check_high_score(stats, score_b)
	if len(aliens) == 0:
		# Если весь флот уничтожен, игра переходит в неактивное состояние.
		bullets.empty()
		stats.game_active = False
		stats.select_active = True
		pygame.mouse.set_visible(True)


def update_aliens(settings, screen, stats, score_b, ship, aliens, bullets):
	"""Обработка событий, связанных с пришельцами."""
	
	# Обновление позиции пришельца.
	aliens.update()
	
	# Проверка пришельцев, добравшихся до нижнего края экрана.
	check_bottom(settings, screen, stats, score_b, ship, aliens, bullets)
	
	# Проверка коллизий "пришелец-корабль".
	if pygame.sprite.spritecollide(ship, aliens, True):
		ship_hit(settings, screen, stats, score_b, ship, aliens, bullets)
			
			
def ship_hit(settings, screen, stats, score_b, ship, aliens, bullets):
	"""Обрабатывает столкновение корабля с пришельцем."""
	
	# Уменьшение ship_left.
	if stats.ship_left >= 1:
		stats.ship_left -= 1
		
	# Обновление игровой информации об оставшихся жизней корабля.
	score_b.health_of_ship()
	
	if stats.ship_left == 0:
		stats.game_active = False
		pygame.mouse.set_visible(True)
	
def create_asteroids(settings, screen, stats, asteroids, number_level):
	"""Cоздает астероид."""
	
	delta_y = 150
	global i
	for i in range(1,4):
		delta_x = -150
		for item in range(1,6):
			
			level_number = item
			
			if i == 2:
				level_number = item + 5
				
			if i ==3:
				level_number = item + 10
				
			asteroid = Asteroid(settings, screen, level_number)
			asteroid_width = asteroid.rect.width
			delta_x += 2*asteroid_width
			asteroid.rect.x = asteroid.rect.x + delta_x
			if i == 2:
				asteroid.rect.y = asteroid.rect.y + delta_y
				item = item + 5
			if i ==3:
				asteroid.rect.y = asteroid.rect.y + 2*delta_y
				item = item + 10
				
			number = Number(settings, screen, item)
			number.rect.centerx = asteroid.rect.centerx
			number.rect.centery = asteroid.rect.centery
			
			asteroids.add(asteroid)
			number_level.add(number)
			del asteroid
			del number

def number_units(level):
	"""Возвращает число юнитов."""
	if level == 1:
		return 16
		
	if level > 1:
		return (16 + (level - 1)*5)
		

