import cv2
import copy
from video.CameraStream import CameraStream
from output.StreamDisplay import StreamDisplay
from output.SnapshotTrigger import SnapshotTrigger
from recognition.FaceRecognizer import FaceRecognizer
from time import sleep

ESC = 27

facerecognizer = FaceRecognizer()
trigger = SnapshotTrigger("images")
display = StreamDisplay()

camstream = CameraStream(use_pi_camera=False, resolution=(1280, 720)).start()
sleep(3)

while True:
    image = camstream.read()

    faces = facerecognizer.recognize(image)
    if len(faces) > 0:
        trigger.save_snapshot(copy.deepcopy(image))

    display.update_display(image, faces)

    key = cv2.waitKey(20)
    if key == ESC:
        break

cv2.destroyAllWindows()
