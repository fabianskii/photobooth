class CameraStream:
    def __init__(self, src=0, use_pi_camera=False, resolution=(800, 600),
                 framerate=25):
        if use_pi_camera:
            from imutils.video.pivideostream import PiVideoStream
            self.stream = PiVideoStream(resolution=resolution,
                                        framerate=framerate)

        else:
            from video.webcamvideostream import WebcamVideoStream
            self.stream = WebcamVideoStream(src=src, resolution=resolution)

    def start(self):
        return self.stream.start()

    def update(self):
        self.stream.update()

    def read(self):
        return self.stream.read()

    def stop(self):
        self.stream.stop()
