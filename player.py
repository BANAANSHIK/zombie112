import pygame
class Player:
    width = 50
    height = 50
    x = 100
    y = 100
    image = ""

    surface = ""
    rect = ""

    def __init__(self, image, width=50,height=50, x=100,y=100):
        self.image = image
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.surface = pygame.image.load(image)


        self.surface = pygame.transform.scale(self.surface, (self.width, self.height))


        self.rect = self.surface.get_rect(center=(x,y))


    def draw(self,screen:pygame.Surface):
        self.rect.center = (self.x, self.y)
        screen.blit(self.surface,self.rect)
        