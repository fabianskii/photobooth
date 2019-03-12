import cv2


class FaceRecognizer:
    def __init__(self):
        self.face_cascade = cv2.CascadeClassifier("recognition/haarcascades/face_frontal.xml")

    def recognize(self, image):
        image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        faces = self.face_cascade.detectMultiScale(
            image_gray,
            scaleFactor=1.5,
            minNeighbors=5,
            minSize=(30, 30)
        )
        return faces
