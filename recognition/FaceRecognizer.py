import cv2


class FaceRecognizer:
    def __init__(self):
        self.face_cascade = cv2.CascadeClassifier("recognition/haarcascades/face_frontal.xml")

    def recognize(self, image_gray):

        faces = self.face_cascade.detectMultiScale(
            image_gray,
            scaleFactor=1.3,
            minNeighbors=3,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE
        )
        return faces
