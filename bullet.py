import pygame

class Bullet(pygame.sprite.Sprite):
    speed = 8
    damage = 10
    x = 200
    y = 200
    width = 10  # Уменьшим размер пули
    height = 10
    surface = ""
    rect = ""
    isFriendlyFire = True

    def __init__(self, image, width=10, height=10, x=200, y=200, direction=(0, 0), speed=1, rotation=0):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.direction = direction  # Направление движения пули
        # передаем путь до картинки и создаем surface
        self.surface = pygame.image.load(image)
        # убираем цвет
        self.surface.set_colorkey((255, 255, 255))
        # трансформируем surface
        self.surface = pygame.transform.scale(self.surface, (width, height))
        self.surface = pygame.transform.rotate(self.surface, rotation)
        # Создаем холст, на котором будет наша картинка и задаем ему центр
        self.rect = self.surface.get_rect(center=(self.x, self.y))

    def draw(self, screen: pygame.Surface):
        self.rect.center = (self.x, self.y)
        # рисуем картинку на холсте
        screen.blit(self.surface, self.rect)
        
    def move(self):
        # Двигаем пулю в заданном направлении
        self.x += self.direction[0] * self.speed
        self.y += self.direction[1] * self.speed
    
    def is_off_screen(self, screen_width, screen_height):
        # Проверяем, вышла ли пуля за пределы экрана
        return (self.x < 0 or self.x > screen_width or
                self.y < 0 or self.y > screen_height)