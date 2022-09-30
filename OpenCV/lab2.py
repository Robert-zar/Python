import cv2
import numpy as np
import math

#Перекрашивает изображение в чёрно-белое

def print_img():
 img1 = cv2.imread(r'01.jpg', cv2.IMREAD_ANYDEPTH)

 cv2.namedWindow('Display Window', cv2.WINDOW_AUTOSIZE)
 cv2.imshow("Display Window", img1)
 cv2.waitKey(0)
 cv2.destroyAllWindows()
 
 
#Матрица гаусса

def matr(n, m):
 matrix = np.array([[(1 / (2 * math.pi * m * m) * math.exp(-((j - n // 2) * (j - n // 2) + (i - n // 2) * (i - n // 2)) / 2 * m * m)) for j in range(n)] for i in range(n)])
 print(matrix.sum())
 print(matrix)
 matrix = (matrix/matrix.sum())
 print(matrix.sum())
 print(matrix)

 
 #Размытие изображения по гауссу
 
def gauss():
 img = cv2.imread(r'01.jpg')
 gaussian = cv2.GaussianBlur(img, (9, 9), 0)

 imgR = cv2.resize(img, (760, 340))
 gaussianR = cv2.resize(gaussian, (760, 340))
 cv2.imshow('Display Window', imgR)
 cv2.imshow('Gaussian blur', gaussianR)
 cv2.waitKey()
 cv2.destroyAllWindows()


#matr(3,1)
#print_img()
#gauss()
