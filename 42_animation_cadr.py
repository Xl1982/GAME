import pygame
from constant import *
from pygame.locals import *

class SpriteSheet(): # определяем класс
    def __init__(self, image): #создаем конструктор класс
        self.sheet = image # сохраняем переданное изображения в экземпляре класса

    def get_image(self, frame, width, height, scale, color): #метод класса для получения изображения из спрайт листа
        image = pygame.Surface((width, height)).convert_alpha()# создаем поверхность заданнаого размера
        image.blit(self.sheet, (0, 0), ((frame * width),0, width, height)) # отрисовываем на холсте слой
        image = pygame.transform.scale(image, (width * scale, height * scale)) # меняем размер изображения
        image.set_colorkey(color) #устанавливаем прозрачный цвет для пикчи
        return image #возвращаем все в функцию

pygame.init() # инициализируем библиотеку pygame

SCREEN_WIDTH = 500 #ширина
SCREEN_HEIGHT = 500 #длина

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #создаем пер окна
pygame.display.set_caption('ggg')

BG = GRAY
animation_list = [] # пустой список анимаций
animation_steps = [4, 6, 3, 4, 7] # список определяющий число кадров в каждой анимации
last_update = pygame.time.get_ticks() # время в милисек

animation_cooldown = 500 #время в милисекундах между кадрами анимации
frame = 0 # начальный кадр анимации
action = 0 # начальная анимация

srite_sheet_image = pygame.image.load('dino1.png').convert_alpha() #загружаем изображение спрайт листа
sprite_sheet = SpriteSheet(srite_sheet_image) # создаем объект класса SpriteSheer на основе загруженного изо

step_counter = 0 #count
for animation in animation_steps: # проходимся по списку количества кадров для каждой анимации
    temp_img_list = [] #создаем пустой список для временного хранения кажров
    for _ in range(animation): # проходимся по каждому кадру в анимации
        temp_img_list.append(sprite_sheet.get_image(step_counter, 24, 24, 3, BLACK)) # добавляем текущий кадр в список
        step_counter += 1 # счетчик для перехода к селдующему кадру
    animation_list.append(temp_img_list) #добавляем список кадров текущей анимации в общий список анимайция
running = True # оосновной игровй цикл
while running:

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
                if event.key == K_DOWN and action > 0: #если  нажата клавиша вниз и анимация не первая в списке
                    action -= 1 # переключаемся на предыдущую анимацию
                    frame = 0 # сбрасываем номер текущего кадра
                if event.key == K_UP and action < len(animation_list) - 1:# елси нажата кл вниж и анимация не последняя в списке
                    action += 1 # переключаемся на след анимацию
                    frame = 0 #сбрасываем номер текущего кадр

    screen.fill(BG)
    screen.blit(animation_list[action][frame], (0,0)) # отображаем текущий кадр в левом углу экрана

    current_time = pygame.time.get_ticks()# получаем текущее время
    if current_time - last_update >= animation_cooldown: # если времени прошло достаточно (с отоборжания посл кадра)
        frame += 1 # тогда переходим на след кадр
        if frame >= len(animation_list[action]): # если список анимаций закончился
            frame = 0 # переходим на первый кадр
            last_update = current_time  # время последнего кадр обновляем

    pygame.display.update() # обновляем экран чтобы отобразить новый кадр
pygame.quit