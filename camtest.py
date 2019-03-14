from time import sleep
import cv2

cv2.namedWindow("Photobooth")
cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 4)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 3)
sleep(2)

while True:
    _, image = cam.read()
    cv2.imshow("Photobooth", image)
    key = cv2.waitKey(1)
    if key == 27:
        # Exit on esc
        break

cv2.destroyAllWindows()
