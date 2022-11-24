# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 10:09:50 2022

@author: LASSODS
"""

import cv2
import numpy as np

imagen_prueba = cv2.imread('C:/Users/LASSODS/Cursos/ComputerVision_DeepLearning/2. Filtrado de imagenes/tarro2.jpg')
cv2.imshow('Original', imagen_prueba)

# Filtro 1: Kernel 3x3
kernel_3x3 = np.ones((3,3))/(3*3)
output3x3 = cv2.filter2D(imagen_prueba,-1,kernel_3x3)
cv2.imshow('Filtro 3x3', output3x3)

# Filtro 2: Kernel 11x11
kernel_11x11 = np.ones((11,11))/(11*11)
output11x11 = cv2.filter2D(imagen_prueba,-1,kernel_11x11)
cv2.imshow('Filtro 11x11', output11x11)

# Filtro 1: Kernel 31x31
kernel_31x31 = np.ones((31,31))/(31*31)
output31x31 = cv2.filter2D(imagen_prueba,-1,kernel_31x31)
cv2.imshow('Filtro 31x31', output31x31)