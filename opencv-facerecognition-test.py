from time import sleep
import cv2
import copy

# Create the cascade
cv2.namedWindow("Photobooth")
#cam = CameraStream(use_pi_camera=True, resolution=(1920,1080),framerate=32).start()
from imutils.video.pivideostream import PiVideoStream
cam = PiVideoStream(resolution=(1920,1080), framerate=32).start()


sleep(2)
image = cam.read()
image_count = 0
cv2.imshow("Photobooth", image)
while True:
    
    # Read new image
    image = cam.read()
    key = cv2.waitKey(1)
    if key == 27:
        # Exit on esc
        break

cv2.destroyWindow("Photobooth")
