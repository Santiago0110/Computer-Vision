# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 10:33:27 2022

@author: LASSODS
"""

import cv2
import numpy as np

bananos = cv2.imread('C:/Users/LASSODS/Cursos/ComputerVision_DeepLearning/1. Procesamiento de Imagenes/copa.jpg')

b = bananos[:,:,0]
g = bananos[:,:,1]
r = bananos[:,:,2]

# Imagen en escala de grises
img_gray = cv2.cvtColor(bananos,cv2.COLOR_BGR2GRAY)

# Imagen binaria
img_bin = np.uint8((img_gray<160)*255)

# Imagen segmentada sobre escala de grises
img_seg = np.uint8(img_gray*(img_bin/255))

# Imagen segmentada a color
seg_color = bananos.copy()
seg_color[:,:,0] = np.uint8(b*(img_bin/255))
seg_color[:,:,1] = np.uint8(g*(img_bin/255))
seg_color[:,:,2] = np.uint8(r*(img_bin/255))

# Mostrar la imagen
cv2.imshow('',seg_color)
cv2.waitKey(0)
cv2.destroyAllWindows()