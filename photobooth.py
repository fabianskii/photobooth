import cv2
import copy

from recognition.FaceRecognizer import FaceRecognizer
from recognition.SmileRecognizer import SmileRecognizer
from video.CameraStream import CameraStream
from output.StreamDisplay import StreamDisplay
from output.SnapshotTrigger import SnapshotTrigger

from time import sleep

ESC = 27

facerecognizer = FaceRecognizer()
smilerecognizer = SmileRecognizer()

trigger = SnapshotTrigger("images")
display = StreamDisplay("Photobooth")

camstream = CameraStream(use_pi_camera=True, resolution=(1280, 720)).start()
sleep(2)

while True:
    image = camstream.read()

    faces = facerecognizer.recognize(image)
    smiles = []
    if len(faces) > 0:
        smiles = smilerecognizer.recognize(image)
        if len(smiles) > 0:
            trigger.save_snapshot(copy.deepcopy(image))

    display.add_bounding_box_for_objects(image, faces, color=(0, 0, 255))
    display.add_bounding_box_for_objects(image, smiles, color=(255, 0, 0))
    display.update_display(image)

    key = cv2.waitKey(20)
    if key == ESC:
        break

cv2.destroyAllWindows()
camstream.stop()
