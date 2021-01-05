import re
import os
import numpy as np
import pytesseract
import cv2

faceCascade = cv2.CascadeClassifier(r'haarcascade_russian_plate_number.xml')
pytesseract.pytesseract.tesseract_cmd = 'Tesseract-OCR\\tesseract.exe'




class Detect:
    def __init__(self, frame):
        self.frame = cv2.imread(os.path.basename(frame))


    def Scalling(self):
        gray = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)  # convert to grey scale
        gray = np.array(gray, dtype='uint8')
        gray = cv2.bilateralFilter(gray, 11, 17, 17)  # Blur to reduce noise
        gray = cv2.GaussianBlur(gray, (3, 3), 0)
        return gray

    def get_image(self):
        plaques = faceCascade.detectMultiScale(self.Scalling(), 1.4, 4)
        for i, (x, y, w, h) in enumerate(plaques):
            roi_color = self.frame[y:y + h, x:x + w]
            r = 400.0 / roi_color.shape[1]
            dim = (400, int(roi_color.shape[0] * r))  # для изменения изображения
            resized = cv2.resize(roi_color, dim, interpolation=cv2.INTER_AREA)
            cv2.imwrite("frame.jpg", resized)


            # text = pytesseract.image_to_string(resized, lang="eng", config='--psm 9')
            # text1 = "".join(
            #     [c for c in text if
            #      c.isupper() or c.isdigit() or c.islower()]).upper()  # регулярка для выделения букв и цифр
            #
            # pattern = re.findall(r"[A-Z]{1}\d{3}[A-Z]{2}\d{2,3}", text1)
            #
            # if pattern:
            #     print(*pattern)  # вывод номера тс
