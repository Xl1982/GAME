import pygame
from pygame.locals import *

pygame.init() #инициализации фун pygame

SCREEN_WIDTH = 800 # размеры экрана
SCREEN_HEIGHT = 600

BG = 52,78,91 # фоновый цвет
TEXT_COLOR = 255,255,255 #  цвет текста
font = pygame.font.SysFont('arialblack',30) #настройки шрифта

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT)) #создание экрана
pygame.display.set_caption('Меню и окна') # создание описания

class Button: # класс кнопки
    def __init__(self,x,y,image,scale): # в него мы передаем координаты, саму картинку, масштаб
        width = image.get_width()
        height = image.get_height()

        self.image = pygame.transform.scale(image,(int(width*scale),int(height*scale)))# масштабирование изображения кнопки
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False

    def draw(self,surface):
        action = False
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos) == True: #находится ли указатель над кнопкой
            if pygame.mouse.get_pressed()[0] == True and self.clicked == False: # проверяем на нажатие левой кнопки мыши
                self.clicked = True
                action = True
        if pygame.mouse.get_pressed()[0]==False:
            self.clicked = False

        surface.blit(self.image,(self.rect.x,self.rect.y))
        return action




def draw_text(string,font,text_color,x,y): #функция для отображения текста на экране
    text = font.render(string,True,text_color)
    screen.blit(text,(x,y))


resume_img = pygame.image.load('buttons/button_resume.png')
options_img = pygame.image.load('buttons/button_options.png')
quit_img = pygame.image.load('buttons/button_quit.png')
audio_img = pygame.image.load('buttons/button_audio.png')
keys_img = pygame.image.load('buttons/button_keys.png')
video_img = pygame.image.load('buttons/button_video.png')
back_img = pygame.image.load('buttons/button_back.png')

resume_button = Button(304,125,resume_img,1)
options_button = Button(297,250,options_img,1)
quit_button = Button(336,375,quit_img,1)

audio_button = Button(226,75,audio_img,1)
video_button = Button(225,200,video_img,1)
keys_button = Button(246,325,keys_img,1)
back_button = Button(332,450,back_img,1)

menu_state = 'main'
game_pause = False
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                game_pause = True

    screen.fill(BG)
    if game_pause:
        if menu_state=='main':
            if resume_button.draw(screen) == True:
                game_pause = False
            elif options_button.draw(screen):
                menu_state = 'options'
            elif quit_button.draw(screen):
                running = False

        elif menu_state =='options':
            if video_button.draw(screen):
                print('Video options')
            elif audio_button.draw(screen):
                print('Audio options')
            elif keys_button.draw(screen):
                print('Keys options')
            elif back_button.draw(screen):
                menu_state = 'main'
    else:
        draw_text('Окно игры, пробел - пауза',font,TEXT_COLOR,SCREEN_WIDTH /5,SCREEN_HEIGHT /2)
    pygame.display.update()
pygame.quit()