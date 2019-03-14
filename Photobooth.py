import cv2
import copy
import time
import sys

from recognition.FaceRecognizer import FaceRecognizer
from recognition.SmileRecognizer import SmileRecognizer
from video.CameraStream import CameraStream
from output.StreamDisplay import StreamDisplay
from output.SnapshotTrigger import SnapshotTrigger

from time import sleep


class Photobooth:
    def __init__(self, resolution=(800, 600), use_pi_camera=False, fullscreen=False):
        self._ESC = 27

        self._facerecognizer = FaceRecognizer()
        self._smilerecognizer = SmileRecognizer()

        self._trigger = SnapshotTrigger("images")
        self._display = StreamDisplay("Photobooth", fullscreen)

        self._camstream = CameraStream(use_pi_camera=use_pi_camera, resolution=resolution).start()
        self._stopped = False
        self._smile_cascade = cv2.CascadeClassifier('recognition/haarcascades/smile.xml')

        print("Using OpenCV: " + cv2.getVersionString())
        print("Using Python: " + sys.version)
        sleep(2)

    @property
    def stopped(self):
        return self._stopped

    @stopped.setter
    def stopped(self, value):
        self._stopped = value

    def run(self):
        countdown_active = False
        countdown = 3
        timer = time.time()

        self.loop(countdown, countdown_active, timer)

        cv2.destroyAllWindows()
        self._camstream.stop()

    def loop(self, countdown, countdown_active, timer):
        timeout = False
        timeout_timer = time.time()
        while not self._stopped:

            image = self._camstream.read()
            image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            original_image = copy.deepcopy(image)
            faces = self._facerecognizer.recognize(image_gray, image)
            smiles = []
            if len(faces) > 0:

                smile_detected, smiles = self._smilerecognizer.recognize(faces, image_gray, image)

                if smile_detected and not countdown_active and not timeout:
                    countdown_active = True
                    timer = time.time()

            if countdown == 0:
                self._trigger.save_snapshot(original_image)
                image[:, :, :] = 255
                self._display.update_display(image)
                countdown = 3
                countdown_active = False
                timeout_timer = time.time()
                timeout = True

            if countdown_active:
                self._display.draw_text_on_image(image, text=countdown)

            self._display.update_display(image)

            key = cv2.waitKey(20)
            if key == self._ESC:
                self._stopped = True

            if countdown_active and time.time() - timer >= 1:
                countdown -= 1
                timer = time.time()

            if timeout and time.time() - timeout_timer >= 3:
                timeout = False
