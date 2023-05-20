import time
from random import randint
import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((640,320))


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('player.png') #
        self.rect = self.image.get_rect() # получение прямоуг вокруг изображения
        self.rect.centerx = 100 #установка горизонтальной по икс позиции центра спрайта
        self.rect.bottom = 100 #установка вертикальной позиции нижнией границы спрайта



class Item(pygame.sprite.Sprite): # создаем класс для фонарика
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self) #
        self.image = pygame.image.load('light.png') #загрузка изо
        self.rect = self.image.get_rect() #получение прямоугольника вокруг изо
        self.rect.x = x # установка горизонтальной позиции  спрайта
        self.rect.y = y # установка вертикальной позиции спрайта

light = pygame.image.load('light.png')#
light = pygame.transform.scale(light, (100, 100)) #контроль размера изо
player = Player() # создание экземпляра класса Player
light_on = False # свет
running = True # флаг работы цикла
score = 0#
lives = 3#
brick = pygame.rect.Rect(200, 200, 50, 50)# прямоугольник
start = time.time()# получение текушего времени в секундах
items = []# список хранения предметов

item = Item(130,50)# создание экземпляра класса Items
items.append(item)# добавление предмета в список item

while running:
    for i in pygame.event.get():
        if i.type == QUIT:
            running = False
        if i.type == KEYDOWN and i.key == K_SPACE:
            light_on =True

        if i.type == KEYUP and i.key == K_SPACE:
            light_on = False

        if i.type == KEYUP and i.key == K_RIGHT:
            player.rect.x += 10

        if i.type == KEYUP and i.key == K_LEFT:
            player.rect.x -= 10

        if i.type == KEYUP and i.key == K_UP:
            player.rect.y -= 10


        if i.type == KEYUP and i.key == K_DOWN:
            light_on = False
            player.rect.y += 10



    screen.fill(pygame.color.Color('Red')) #
    filter = pygame.surface.Surface((640, 320)) #создание поверхности фильтр
    filter.fill(pygame.color.Color('Gray')) # заполнение поверхности серым цветом

    if light_on:
        filter.blit(light, (player.rect.x - 25, player.rect.y - 25))
        # отрисовка изображения света на поверхности filter на экране


    pygame.display.set_caption(f'health = {lives}') #
    screen.blit(filter, (0,0), special_flags=pygame.BLEND_RGBA_SUB)
    # отрисовка поверхности filter на экране с флагом BLEND_RGBA_SUB

    for p in items:
        screen.blit(item.image, item.rect)
        #  отрисовка изображения на экране в соотв с его прямоуглоьником

    if player.rect.colliderect(brick):# если спрайт игрока сталкивается с brick
        player.rect.x = 20# возвращаем игрока в начало координат по икс
        player.rect.y = 20# возвращаем игрока в начало координат по игрек
        lives -= 1 # отбираем жизнь

    if lives == 0:# если жизней 0
        running = False# игровой процес все
        print('game over')#

    end = time.time()# получение текцщего времени в секундах
    if (end - start) >= 100:# если их больше 100
        running = 0# прекращаем игровой цикл
        print('game over')#

    screen.blit(player.image, player.rect) #отрисовка игрока
    pygame.draw.rect(screen,(0, 255, 0), brick) #отрисовка кирпича

    pygame.display.update()

pygame.quit()