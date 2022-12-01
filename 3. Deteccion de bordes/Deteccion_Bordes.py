# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 14:55:32 2022

@author: LASSODS
"""

import cv2
import numpy as np

# Lectura de imagen
imagen_prueba = cv2.imread('C:/Users/LASSODS/Cursos/ComputerVision_DeepLearning/3. Deteccion de bordes/3.jpg')

# Imagen en escala de grises
img_gray = cv2.cvtColor(imagen_prueba,cv2.COLOR_BGR2GRAY)

# Calculo de componentes del vector gradiente
gx = cv2.Sobel(img_gray, cv2.CV_64F,1,0,5)
gy = cv2.Sobel(img_gray, cv2.CV_64F,0,1,5)

# Calculo de magnitud del vector gradiente
mag,_ = cv2.cartToPolar(gx,gy)

mag = np.uint8((255*mag) / (np.max(mag)))

# Mostrar la imagen
cv2.imshow('',mag)