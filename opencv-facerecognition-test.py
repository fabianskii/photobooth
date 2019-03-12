import cv2
import copy
from CameraStream import CameraStream
from time import sleep
# Create the cascade
faceCascade = cv2.CascadeClassifier("model.xml")

cv2.namedWindow("Photobooth")
cam = CameraStream(use_pi_camera=True, resolution=(1280,720)).start()
sleep(3)
image = cam.read()
image_count = 0
while True:
    # Convert to grey
    grayImg = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Detect faces in the image
    faces = faceCascade.detectMultiScale(
        grayImg,
        scaleFactor=1.5,
        minNeighbors=5,
        minSize=(30, 30)
    )
    source_image = copy.deepcopy(image)
    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow("Photobooth", image)
    if (len(faces)) > 0:
        # TODO generate image folder if not exists
            
        if image_count == 0:
            print('image_{0}'.format(image_count))      
            cv2.imwrite('images/image_{0}.jpg'.format(image_count), source_image)
            image_count += 1

    # Read new image
    image = cam.read()
    key = cv2.waitKey(20)
    if key == 27:
        # Exit on esc
        break

cv2.destroyWindow("Photobooth")
