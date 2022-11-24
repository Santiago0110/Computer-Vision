# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 10:33:27 2022

@author: LASSODS
"""

import cv2
import numpy as np

imagen_prueba = cv2.imread('C:/Users/LASSODS/Cursos/ComputerVision_DeepLearning/1. Procesamiento de Imagenes/2.jpg')

b = imagen_prueba[:,:,0]
g = imagen_prueba[:,:,1]
r = imagen_prueba[:,:,2]

# Imagen en escala de grises
img_gray = cv2.cvtColor(imagen_prueba,cv2.COLOR_BGR2GRAY)

# Imagen binaria
img_bin = np.uint8((img_gray<135)*255)

# Imagen segmentada sobre escala de grises
img_seg = np.uint8(img_gray*(img_bin/255))

# Método Otsu para umbralizar
th_otsu,_ = cv2.threshold(img_gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
ima_bin_otsu = np.uint8((img_gray<th_otsu)*255)

# Imagen segmentada a color
seg_color = imagen_prueba.copy()
seg_color[:,:,0] = np.uint8(b*(ima_bin_otsu/255))
seg_color[:,:,1] = np.uint8(g*(ima_bin_otsu/255))
seg_color[:,:,2] = np.uint8(r*(ima_bin_otsu/255))

# Mostrar la imagen
cv2.imshow('',seg_color)
cv2.waitKey(0)
cv2.destroyAllWindows()

import matplotlib.pyplot as plt

plt.hist(img_gray.flatten(), bins=15)
plt.show()