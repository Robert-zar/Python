import cv2
import numpy as np
import requests
import imutils

# Вывод картинки на экран

def print_img():
    img1 = cv2.imread(r'01.jpg')

    cv2.namedWindow('Display Window', cv2.WINDOW_AUTOSIZE)
    cv2.imshow("Display Window", img1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Вывод видео на экран
    
def print_video():
 cap = cv2.VideoCapture(r'C:\Users\rzarg\OneDrive\Рабочий стол\сек.mp4', cv2.CAP_ANY)

# Пока файл открыт
 while True:
    # поочередно считываем кадры видео
    ret, frame  = cap.read()
    # если кадры закончились, совершаем выход
    if not (ret):
        break
    # выводим текущий кадр на экран
    cv2.imshow("frame", frame)
    # при нажатии клавиши "q", совершаем выход
    if cv2.waitKey(25) & 0xFF == 27:
        break
# освобождаем память от переменной cap
 cap.release()
# закрываем все открытые opencv окна
 cv2.destroyAllWindows()


# Вывод изображения с камеры телефона на экран
    
def print_cam():
 url = "http://192.168.1.103:8080/shot.jpg"

 while True:
        imgResp = requests.get(url)
        imgArr = np.array(bytearray(imgResp.content), dtype=np.uint8)
        img = cv2.imdecode(imgArr, -1)
        img = imutils.resize(img, width=1000, height=1800)
        cv2.imshow("Camera", img)

        cv2.imshow('Camera', img)

        if cv2.waitKey(1) & 0xFF == 27:
            break
            cv2.destroyAllWindows()



# Вывод изображения с веб-камеры на экран
            
def reabWebCamera():
        cv2.namedWindow("Camera")
        vc = cv2.VideoCapture(0)

        if vc.isOpened():
            rval, frame = vc.read()
        else:
            rval = False

        while rval:
            cv2.imshow("Camera", frame)
            rval, frame = vc.read()
            key = cv2.waitKey(20)
            if key == 27:
                break

        cv2.destroyWindow("preview")
        vc.release()


#print_img()
#print_video()
#print_cam()
#reabWebCamera()

