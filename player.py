import pygame
import math
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from bullet import Bullet
from matematika import calculate_angle



class Player:
    width = 50
    height = 50
    speed = 5
    x = 100
    y = 100
    hp = 100

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
        width = screen.get_width()
        height = screen.get_height()

        if self.x < -50:
            self.x = width + 50
        elif self.x > width + 50:
            self.x = - 50
        if self.y < -50:
            self.y = width + 50
        elif self.y > width + 50:
            self.y = - 50


        self.rect.center = (self.x, self.y)
        screen.blit(self.surface,self.rect)
        
    def movement(self):
            # Управление 
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.x += self.speed
        elif keys[pygame.K_a]:
            self.x -= self.speed
        if keys[pygame.K_w]:
            self.y  -= self.speed
        elif keys[pygame.K_s]:
            self.y  += self.speed
        if keys[pygame.K_LSHIFT]:
            self.speed = 4
        else:
            self.speed = 2



    def showHP(self, screen:pygame.Surface,x,y):
        pygame.draw.rect(screen,(0,0,0),(20,20,100,50))
        pygame.draw.rect(screen,(0,200,100),(20,20,self.hp,50))





    def shoot(self,mouse_x,mouse_y):
        direction_x = mouse_x - self.x
        direction_y = mouse_y - self.y
        lenght = math.hypot(direction_x,direction_y)
        if lenght == 0:
            return None
        direction_x /= lenght
        direction_y /= lenght

        angle = calculate_angle(mouse_x,mouse_y,self.x,self.y)
        return Bullet("./image.png",width=80,height=40,x=self.x,y=self.y,direction=(direction_x,direction_y),speed=6,rotation=angle-90)


pygame.quit()