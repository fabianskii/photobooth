import cv2


class StreamDisplay:

    def update_display(self, image, faces):
        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv2.imshow("Photobooth", image)
