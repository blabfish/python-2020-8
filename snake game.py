#snake game

import math
import random
import pygame
import tkinter as tk
from tkinter import massagebox

class cube(object):
    rows = 0
    w = 0
    def _init_(self,start,dirnx=1,dirny=0,color=(255,0,0)):
        pass
    def move(self, dirnx, dirny):
        pass
    def draw(self, surface,eyes=False):
        pass

class snake(object):
    body = []
    turns = {}
    def _init_(self, color, pos):
        self.color = color
        self.head = cube(pos)
        self.body.append(self.head)
        self.dirnx = 0
        self.dirny = 1
    def move(self):
        for evenin pygame.event.get():
            if event.type == pygame.quit:
                pygame.quit()
                
            keys = pygame.key.get_pressed()
            
            for key in keys:
                if keys[pygame.K_LEFT]:
                    self.dirnx = -1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx,]
                if keys[pygame.K_RIGHT]:
                    
                if keys[pygame.K_UP]:
                    
                if keys[pygame.K_DOWN]:
    def reset(self, pos):
        pass
    def addCube(self):
        pass
    def draw(self, surface):
        pass
def drawGrid(w, rows, surface):
    sizeBtwn = w // rows
    
    x = 0
    y = 0
    for i in range(rows):
        x = x + sizeBtwn
        y = y + sizeBtwn
        
        pygame.draw.line(surface, (255,255,255), (x,0), (x,w))
        pygame.draw.line(surface, (255,255,255), (0,y), (w,y))
        
def redrawWindow(surface):
    global rows, width
    surface.fill((0,0,0))
    drawGrid(width, rows, surface)
    pygame.display.update()
def randomSnack(rows, items):
    pass
def massage_box(subject, content):
    pass
def main():
    global width, rows
    width = 500
    rows = 20
    win = pygame.display.set_mode((width, width))
    s = snake((255,0,0), (10,10))
    flag = True
    
    clock = pygame.time.Clock()
    
    while flag:
        pygame.time.delay(50)
        clock.tick(10)
        redrawWindow(win)
    
    pass
    
    
    
    
    
    
    
    
    
    
    
    
    
    