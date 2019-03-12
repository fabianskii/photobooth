import cv2


class SmileRecognizer:
    def __init__(self):
        self.smile_cascade = cv2.CascadeClassifier("recognition/haarcascades/smile.xml")

    def recognize(self, image):
        image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        smiles = self.smile_cascade.detectMultiScale(
            image_gray,
            scaleFactor=1.5,
            minNeighbors=5,
            minSize=(50, 50),
            maxSize=(100,100)
        )
        return smiles
