import cv2

# Create the cascade
faceCascade = cv2.CascadeClassifier("model.xml")

cv2.namedWindow("Photobooth")

# Open cam stream
cam = cv2.VideoCapture(0)

if cam.isOpened(): # try to get the first frame
    rval, image = cam.read()
else:
    rval = False


while rval:
    # Convert to grey
    grayImg = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Detect faces in the image
    faces = faceCascade.detectMultiScale(
        grayImg,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )
    # print("Found {0} faces!".format(len(faces)))
    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow("Photobooth", image)

    #Read new image
    rval, frame = cam.read()
    key = cv2.waitKey(20)
    if key == 27:
        # Exit on esc
        break

cv2.destroyWindow("Photobooth")
