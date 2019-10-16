import numpy as np
import cv2
from matplotlib import pyplot as plt

#ler uma imagem em escala de cinzentos
img = cv2.imread('fb.jpg',0)


#mostrar a imagem
#cv2.imshow('imagem',img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#mostrar a imagem usando o matplotlibz
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()