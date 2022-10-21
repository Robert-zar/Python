import numpy as np
import cv2


def get_photo(path=r'.\01.jpg'):
    img = cv2.imread(path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return img


def print_photo(img):
    cv2.namedWindow('Display window', cv2.WINDOW_NORMAL)
    cv2.imshow('Display window', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# def print_photo(img):
    #   cv2.namedWindow('Display window', cv2.WINDOW_NORMAL)
    #   cv2.imshow('Display window'," hh", img)
    #   cv2.waitKey(0)
#       cv2.destroyAllWindows()

def get_blur_img(img, n=5):
    blur_img = cv2.GaussianBlur(img, (n, n), 1.4)
    return blur_img


def canny_algorithm(img):
    mGx = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    mGy = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])

    Gx = np.zeros((len(img), len(img[0])))
    Gy = np.zeros((len(img), len(img[0])))
    G = np.zeros((len(img), len(img[0])))

    phi = np.zeros((len(img), len(img[0])))
    flag = np.zeros((len(img), len(img[0])))

    for i in range(1, len(img)-1):
        for j in range(1, len(img[0])-1):

            submatrix = img[i-1:i+2, j-1:j+2]
            Gx[i, j] = np.sum(np.multiply(submatrix, mGx))
            Gy[i, j] = np.sum(np.multiply(submatrix, mGy))
            G[i, j] = np.sqrt(Gx[i, j]**2 + Gy[i, j]**2)

            if Gx[i, j] != 0:
                phi[i, j] = np.arctan2(Gy[i, j], Gx[i, j])

            if Gx[i, j] > 0 and Gy[i, j] < 0 and phi[i, j] < -2.414 or Gx[i, j] < 0 and Gy[i, j] < 0 and phi[i, j] > 2.414:
                flag[i, j] = 0
            elif Gx[i, j] > 0 and Gy[i, j] < 0 and phi[i, j] < -0.414:
                flag[i, j] = 1
            elif Gx[i, j] > 0 and Gy[i, j] < 0 and phi[i, j] > -0.414 or Gx[i, j] > 0 and Gy[i, j] > 0 and phi[i, j] < 0.414:
                flag[i, j] = 2
            elif Gx[i, j] > 0 and Gy[i, j] > 0 and phi[i, j] < 2.414:
                flag[i, j] = 3
            elif Gx[i, j] > 0 and Gy[i, j] > 0 and phi[i, j] > 2.414 or Gx[i, j] < 0 and Gy[i, j] > 0 and phi[i, j] < -2.414:
                flag[i, j] = 4
            elif Gx[i, j] < 0 and Gy[i, j] > 0 and phi[i, j] < -0.414:
                flag[i, j] = 5
            elif Gx[i, j] < 0 and Gy[i, j] > 0 and phi[i, j] > -0.414 or Gx[i, j] < 0 and Gy[i, j] < 0 and phi[i, j] < 0.414:
                flag[i, j] = 6
            elif Gx[i, j] < 0 and Gy[i, j] < 0 and phi[i, j] < 2.414:
                flag[i, j] = 7

    max_grad = np.max(G)
    low_level = 20
    high_level = 60

    low_level = max_grad // 25
    high_level = max_grad // 15

    for i in range(1, len(img)-1):
        for j in range(1, len(img[0])-1):
            if flag[i, j] == 0 or flag[i, j] == 4:
                if G[i, j] > G[i+1, j] and G[i, j] > G[i-1, j]:
                    img[i, j] = 255
                else:
                    img[i, j] = 0
            elif flag[i, j] == 1 or flag[i, j] == 5:
                if G[i, j] > G[i-1, j+1] and G[i, j] > G[i+1, j-1]:
                    img[i, j] = 255
                else:
                    img[i, j] = 0
            elif flag[i, j] == 2 or flag[i, j] == 6:
                if G[i, j] > G[i, j+1] and G[i, j] > G[i, j-1]:
                    img[i, j] = 255
                else:
                    img[i, j] = 0
            elif flag[i, j] == 3 or flag[i, j] == 7:
                if G[i, j] > G[i-1, j-1] and G[i, j] > G[i+1, j+1]:
                    img[i, j] = 255
                else:
                    img[i, j] = 0

            if img[i, j] == 255:
                img[i, j] = 0
                submatrix = img[i-1:i+2, j-1:j+2]
                max_el = np.max(submatrix)

                if G[i, j] < low_level:
                    img[i, j] = 0
                elif G[i, j] > high_level:
                    img[i, j] = 255
                elif max_el == 255:
                    img[i, j] = 255

    return img


def main():
    shrek = get_photo()
    print_photo(shrek)

    blur = get_blur_img(shrek)
    res = canny_algorithm(blur)
    print_photo(res)
    c = cv2.Canny(get_blur_img(shrek), 20, 50)
    print_photo(c)

    cv2.namedWindow('Display window', cv2.WINDOW_NORMAL)
    cv2.namedWindow('Display window1', cv2.WINDOW_NORMAL)
    cv2.namedWindow('Display window2', cv2.WINDOW_NORMAL)

    cv2.imshow('Display window', shrek)
    cv2.imshow('Display window1', res)
    cv2.imshow('Display window2', c)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

main()
