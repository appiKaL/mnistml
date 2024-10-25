import pygame, sys
from pygame.locals import *
import numpy as np
from keras.models import load_model
import cv2

WINDOWSIZEX = 640
WINDOWSIZEY = 480


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

IMAGESAVE = False
MODEL = load_model("/home/appikal/LGG-Thomas4-Kyllian/projects/Mnist ML/best_model.keras")
LABELS = {0:"Zero", 1:"One", 2:"Two", 3:"Three", 4:"Four", 5:"Five", 6:"Six", 7:"Seven", 8:"Eight", 9:"Nine"}
# Initialize Pygame
pygame.init()

FONT = pygame.font.Font("freesansbold.ttf", 18)

pygame.display.set_mode((WINDOWSIZEX, WINDOWSIZEY))
#WHILE_INT = DISPLAYSURF.mp_rgb(WHITE)
pygame.display.set_caption("Digit Board")

iswriting

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

            if event.