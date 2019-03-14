import cv2
import os, errno


def create_folder(name):
    try:
        os.makedirs(name)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise


class SnapshotTrigger:
    def __init__(self, folder):
        self.image_count = 0
        self.folder = folder
        create_folder(self.folder)

    def save_snapshot(self, rgb_image):
        cv2.imwrite('{0}/image_{1}.jpg'.format(self.folder, self.image_count), rgb_image)
        print('captured image_{0}'.format(self.image_count))
        self.image_count += 1
