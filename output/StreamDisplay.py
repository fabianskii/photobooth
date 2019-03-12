import cv2


class StreamDisplay:

    def __init__(self, window_name):
        self.window_name = window_name
        cv2.namedWindow(self.window_name, cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty(self.window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    def update_display(self, image):
        cv2.imshow(self.window_name, image)

    @staticmethod
    def add_bounding_box_for_objects(image, objects, color):
        for (x, y, w, h) in objects:
            cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)
