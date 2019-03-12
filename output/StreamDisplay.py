import cv2


class StreamDisplay:

    def __init__(self, window_name):
        self.window_name = window_name
        cv2.namedWindow(self.window_name, cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty(self.window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    def update_display(self, image, faces, text=None):
        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

        if text:
            image = self.draw_text_on_image(image, text)
        cv2.imshow(self.window_name, image)

    def draw_text_on_image(self, image, text):
        height, width, channels = image.shape

        font = cv2.FONT_HERSHEY_TRIPLEX
        scale_factor = 6.0
        thickness = 2
        lineType = cv2.LINE_AA
        font_color = (255, 255, 255)
        size = cv2.getTextSize(text, cv2.FONT_HERSHEY_TRIPLEX, scale_factor, thickness)
        center_text_height = size[0][1] / 2
        center_text_width = size[0][0] / 2
        text_location_horizontal = int(width / 2 - center_text_width)
        text_location_vertical = int(height / 2 + center_text_height)
        image = cv2.putText(image, text, (text_location_horizontal, text_location_vertical),
                            font, scale_factor, font_color, lineType=lineType)

        return image
