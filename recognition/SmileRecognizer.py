import cv2


class SmileRecognizer:
    def __init__(self):
        self._smile_cascade = cv2.CascadeClassifier("recognition/haarcascades/smile.xml")

    def recognize(self, faces, gray, img):
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = img[y:y + h, x:x + w]

            smile = self._smile_cascade.detectMultiScale(
                roi_gray,
                scaleFactor=1.5,
                minNeighbors=25,
                minSize=(25, 25),
            )

            for (xx, yy, ww, hh) in smile:
                cv2.rectangle(roi_color, (xx, yy), (xx + ww, yy + hh), (0, 0, 255), 2)
            if len(smile) > 0:
                return True
        return False
