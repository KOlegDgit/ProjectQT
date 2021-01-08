import cv2
import keyboard
from PyQt5 import uic,  QtGui
from PyQt5.QtGui import QPixmap

class Detect_cam:

    def detect(self, cam_label):
        faceCascade = cv2.CascadeClassifier(r'data\\haarcascade_russian_plate_number.xml')
        video_capture = cv2.VideoCapture(0)  # Выбираем устройство видеозахвата

        while True:
            ret, frame = video_capture.read()

            # Получаем серую картинку
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            plaques = faceCascade.detectMultiScale(gray, 1.3, 5)
            for i, (x, y, w, h) in enumerate(plaques):
                roi_color = frame[y:y + h, x:x + w]
                cv2.putText(frame, str(x) + " " + str(y) + " " + str(w) + " " + str(h), (480, 220),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255))
                r = 400.0 / roi_color.shape[1]
                dim = (400, int(roi_color.shape[0] * r))
                resized = cv2.resize(roi_color, dim, interpolation=cv2.INTER_AREA)
                w_resized = resized.shape[0]
                h_resized = resized.shape[1]

                # Собираем в основную картинку
                frame[100:100 + w_resized, 100:100 + h_resized] = resized

            # Отображаем в окне вебку с выделенным frame-номером
            qImage = QtGui.QImage(frame, frame.shape[1], frame.shape[0],
                                  QtGui.QImage.Format_RGB888)
            cam_label.setPixmap(QPixmap.fromImage(qImage))

            if keyboard.is_pressed('q'):
                break
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        video_capture.release()