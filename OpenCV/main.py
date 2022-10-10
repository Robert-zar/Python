import cv2

# Объект захвата
input_cam = cv2.VideoCapture(0)

# Параметры для записи
frame_width = int(input_cam.get(3))
frame_height = int(input_cam.get(4))
frame_size = (frame_width, frame_height)
fps = 30

# Объект записи видео
output = cv2.VideoWriter('detected.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), fps, frame_size)

while input_cam.isOpened():  # Пока объект захвата открыт
    ret, frame1 = input_cam.read()  # Берём два фрейма
    ret, frame2 = input_cam.read()  # Метод input_cam.read() возвращают кортеж (логическое значение, кадр)

    diff = cv2.absdiff(frame1, frame2)  # Абсолютная разница помогает определить те области, что двигаются
    gray = cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY)  # Переводим в чб
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    ret, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)

    # Выделяем контуры. Аргументы - (image, mode, method)
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour) < 300:
            continue
        cv2.drawContours(frame1, contours, -1, (156, 58, 227), 2)

        # Записываю фрейм без наложений
        output.write(frame2)

    cv2.imshow('Cam', frame1)
    cv2.imshow('Countours', frame2)

    if cv2.waitKey(10) == 27:
        break

output.release()
input_cam.release()
cv2.destroyAllWindows()