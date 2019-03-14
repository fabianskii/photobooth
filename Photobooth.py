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
        loop_durations_start = []
        loop_durations_stop = []
        while not self._stopped:
            loop_durations_start.append(time.time())

            image = self._camstream.read()

            faces = self._facerecognizer.recognize(image)
            smiles = []
            if len(faces) > 0:
                smiles = self._smilerecognizer.recognize(image)
                if len(smiles) > 0 and not countdown_active:
                    countdown_active = True
                    timer = time.time()

            if countdown == 0:
                self._trigger.save_snapshot(copy.deepcopy(image))
                countdown = 3
                countdown_active = False

            self._display.add_bounding_box_for_objects(image, faces, color=(0, 255, 0))
            self._display.add_bounding_box_for_objects(image, smiles, color=(0, 0, 255))

            if countdown_active:
                self._display.draw_text_on_image(image, text=countdown)

            self._display.update_display(image)

            key = cv2.waitKey(20)
            if key == self._ESC:
                self._stopped = True

            if countdown_active and time.time() - timer >= 1:
                countdown -= 1
                timer = time.time()

            loop_durations_stop.append(time.time())

        average = 0
        averages = []
        overall = 0
        for idx, duration_start in enumerate(loop_durations_start):
            average = loop_durations_stop[idx] - duration_start
            averages.append(average)
            overall += average
        print(str(overall / len(loop_durations_stop)))
        print(averages)
