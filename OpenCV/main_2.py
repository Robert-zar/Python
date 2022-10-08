from copy import deepcopy, copy

import numpy as np
import cv2

n = 0  # int(input('N -> '))
center = (n - 1) // 2
sigma = 0  # int(input('Sigma -> '))


# x и y - это i,j, a и b - также координаты


def getMatrix():
    _matrix = []
    for i in range(n):
        _vector = []
        for j in range(n):
            _vector.append(gauss(i, j))
        _matrix.append(_vector)
    return _matrix


def gauss(x, y, a=center, b=center):
    return 1 / (2 * np.pi * (sigma ** 2)) * \
           np.exp(-((x - a) ** 2 + (y - b) ** 2) / (2 * sigma * sigma))


matrix = getMatrix()


def getSum():
    _sum = 0
    for i in range(n):
        for j in range(n):
            _sum += matrix[i][j]
    return _sum


sum = getSum()


def getNormMatrix():
    _matrix = []
    for i in range(n):
        _vector = []
        for j in range(n):
            _vector.append(matrix[i][j] / sum)
        _matrix.append(_vector)
    return _matrix


# matrix = getNormMatrix()
sum = 0
for i in range(n):
    for j in range(n):
        sum += matrix[i][j]

print(sum)


def getPicture(path=r'.\fruit.jpg'):
    _img = cv2.imread(path, cv2.IMREAD_ANYDEPTH)
    # cv2.namedWindow('Display window', cv2.WINDOW_NORMAL)
    # cv2.imshow('Display window', _img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    return _img


def getBlurPicture(img=getPicture()):
    imgNew = img

    len1 = len(img)
    len2 = len(img[0])

    for i in range(center, len1 - center):
        for j in range(center, len2 - center):
            _sum = 0
            for q in range(n):
                for w in range(n):
                    _sum += matrix[q][w] * img[q + i - center][w + j - center]
            imgNew[i][j] = _sum

    # cv2.namedWindow('Display window', cv2.WINDOW_NORMAL)
    # cv2.imshow('Display window', imgNew)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    return imgNew


# out1 = getBlurPicture()
blur = cv2.GaussianBlur(getPicture(), (11, 11), 3.3)
#blur = cv2.blur(getPicture(), (7, 7))
# cv2.imshow("ress", getPicture())
# cv2.imshow("result1", out1)
# cv2.imshow("result2", out2)

# cv2.waitKey(0)
# cv2.destroyAllWindows()


# ЛР3 - границы объектов
# если в пикселе сильно (быстро) меняется цвет (функция) -> производная, значит это граница
# градиент: (di/dx; di/dy)
# большой градиент - граница
# алгоритм Канни
# 1. ч.б.
# 2. Gauss Blur
# 3. Градиенты
# 4. (тоже 3 пункт) Численные методы (матан для натуральных чисел, производная двух переменных)
# Метод Собеля
# две матрицы свёртки к каждому пикселю 2 раза
# находим длину вектора для каждого пикселя и сравниваем с другими
# считаем tg=Gy/Gx = 45 град
# 4. Подавление немаксимумов
# если величина градиента больше чем у соседей, то это граница
# все что граница - черным, не граница - белым
# 5. Двойная пороговая фильтрация (применяем только к границам)
# если градиент больше high - точно граница, меньше чем low - Точно не граница
# если попали по-середине, смотрим, есть ли вокруг него граница
# если да, то текущий граница, иначе нет
# 6. контуры надо замкнуть, разбирать не будем

img = blur
print(img[0][0])
n, m = img.shape[:2]
print(n, m)

# for i in range(n):
#     line = copy(img[i])
#     for j in range(m):
#         if i < 11:
#             line[j] = 255
#         elif i > n - 12:
#             line[j] = 255
#         elif j < 11:
#             line[j] = 255
#         elif j > m - 12:
#             line[j] = 255
#         else:
#             line[j] = img[i][j]
#     img[i] = copy(line)



# def gradient():
#    gradx = []
#   grady = []
#   for i in range(1, n - 1):
#      linex = []
#     liney = []
#     for j in range(1, m - 1):
#      linex.append(svertkax(i, j))
#      liney.append(svertkay(i, j))
#  gradx.append(linex)
#   grady.append(liney)


def some_x():
    gx = [
        [-1, 0, 1],
        [-2, 0, 2],
        [-1, 0, 1],
    ]

    imgNew = img

    for _i in range(1, n - 1):
        for _j in range(1, m - 1):
            _sum = 0
            for q in range(3):
                for w in range(3):
                    _sum += (gx[q][w] * img[q + _i - 1][w + _j - 1])
            imgNew[_i][_j] = _sum

    return imgNew


def some_y():
    gy = [
        [-1, -2, -1],
        [0, 0, 0],
        [1, 2, 1],
    ]

    imgNew = img

    for _i in range(1, n - 1):
        for _j in range(1, m - 1):
            _sum = 0
            for q in range(3):
                for w in range(3):
                    _sum += (gy[q][w] * img[q + _i - 1][w + _j - 1])
            imgNew[_i][_j] = _sum

    return imgNew


def some_xy():
    gx = [
        [-1, 0, 1],
        [-2, 0, 2],
        [-1, 0, 1],
    ]

    gy = [
        [-1, -2, -1],
        [0, 0, 0],
        [1, 2, 1],
    ]

    imgNew1 = deepcopy(img)
    imgNew2 = deepcopy(img)

    for _i in range(1, n - 1):
        for _j in range(1, m - 1):
            _sum1 = 0
            _sum2 = 0
            for q in range(3):
                for w in range(3):
                    img_el = img[q + _i - 1][w + _j - 1]
                    _sum1 += (gx[q][w] * img_el)
                    _sum2 += (gy[q][w] * img_el)
            imgNew1[_i][_j] = _sum1
            imgNew2[_i][_j] = _sum2

            # print(_sum1, _sum2)

    return imgNew1, imgNew2


def gradient():
    # count = 0
    # gx = some_x()
    # gy = some_y()
    gx, gy = some_xy()

    # for i in range(1, n - 1):
    #     for j in range(1, m - 1):
    #         print(gx[i][j] - gy[i][j])

    matrix_length = deepcopy(img)  # значения градиентов
    matrix_atan = deepcopy(img)  # тангенсы (направления от 0 до 7)

    for i in range(1, n - 1):
        line_length = copy(img[i])
        line_atan = copy(img[i])
        for j in range(1, m - 1):
            x = int(gx[i][j])
            y = int(gy[i][j])
            line_length[j] = (x ** 2 + y ** 2) ** 0.5
            # print(line_length[j])
            tg = y / x if x != 0 else y
            # print(tg)
            value = -1
            if x > 0 and y < 0 and tg < -2.414 or \
                    x < 0 and y < 0 and tg > 2.414:
                value = 0
            elif x > 0 and y < 0 and tg < -0.414:
                value = 1
            elif x > 0 and y < 0 and tg > -0.414 or \
                    x > 0 and y > 0 and tg < 0.414:
                value = 2
            elif x > 0 and y > 0 and tg < 2.414:
                value = 3
            elif x > 0 and y > 0 and tg > 2.414 or \
                    x < 0 and y > 0 and tg < -2.414:
                value = 4
            elif x < 0 and y > 0 and tg < -0.414:
                value = 5
            elif x < 0 and y > 0 and tg > -0.414 or \
                    x < 0 and y < 0 and tg < 0.414:
                value = 6
            elif x < 0 and y < 0 and tg < 2.414:
                value = 7
            else:
                value = -1

            # if value == -1:
            #    count += 1

            line_atan[j] = value
        matrix_length[i] = copy(line_length)
        matrix_atan[i] = copy(line_atan)

    list_max_matrix_length = []
    for i in matrix_length:
        list_max_matrix_length.append(max(i))
    max_matrix_length = max(list_max_matrix_length)

    low_level = max_matrix_length // 25
    high_level = max_matrix_length // 10

    matrix_border = deepcopy(img)  # границы
    for i in range(1, n - 1):
        line_border = copy(img[i])
        for j in range(1, m - 1):
            way_plus = [[-1, -1], [-1, -1]]
            some = matrix_atan[i][j]
            # [y, x] logic
            if some == 0 or some == 4:
                way_plus = [[-1, 0], [1, 0]]
            elif some == 2 or some == 6:
                way_plus = [[0, -1], [0, 1]]
            elif some == 1:
                way_plus = [[1, 1], [0, 0]]
            elif some == 3:
                way_plus = [[-1, 1], [0, 0]]
            elif some == 5:
                way_plus = [[-1, -1], [0, 0]]
            elif some == 7:
                way_plus = [[1, -1], [0, 0]]
            else:
                way_plus = [[-1, -1], [-1, -1]]

            grad = matrix_length[i][j]

            if some == -1:
                line_border[j] = 255
            else:
                if some % 2 == 0:
                    if grad >= matrix_length[i + way_plus[0][0]][j + way_plus[0][1]] \
                            and grad >= matrix_length[i + way_plus[1][0]][j + way_plus[1][1]]:
                        line_border[j] = 0
                    else:
                        line_border[j] = 255
                else:
                    if grad >= matrix_length[i + way_plus[0][0]][j + way_plus[0][1]]:
                        line_border[j] = 0
                    else:
                        line_border[j] = 255

                if grad < low_level:
                    line_border[j] = 255
                elif grad > high_level:
                    line_border[j] = 0

        matrix_border[i] = copy(line_border)

    for i in range(1, n - 1):
        for j in range(1, m - 1):
            center_el = matrix_border[i][j]
            found_border = False
            for q in range(3):
                for w in range(3):
                    if q == 1 and w == 1:
                        continue
                    el = matrix_border[q + i - 1][w + j - 1]
                    if center_el == 0 and el == 0:
                        found_border = True
                        break
                if found_border:
                    break
            if not found_border:
                matrix_border[i][j] = 255


    # print(count)

    cv2.imshow("nameee", matrix_border)
    cv2.waitKey(0)



gradient()


# import matplotlib.pyplot as plt
#
# im = cv2.imread(r".\fruit.jpg")
# edges = cv2.Canny(im, 25, 255, L2gradient=False)
# plt.imshow(edges, cmap="gray")
# plt.show()


# def svertkax(x, y):
#  dx = img[x + 1][y + 1] - img[x - 1][y - 1] + \
#      img[x + 1, y - 1] - img[x - 1, y + 1] + \
#     2 * (img[x + 1, y] - img[x - 1, y])
# return dx


# def svertkay(x, y):
#   dy = img[x + 1][y + 1] - img[x - 1][y - 1] + \
#      img[x - 1, y + 1] - img[x + 1, y - 1] + \
#    2 * (img[x, y + 1] - img[x, y - 1])
# return dy
