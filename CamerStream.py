from imutils.pivideostream import PiVideoStream

class CameraStream:
    def __init__(self, src=0, use_pi_camera=False, resolution=(800, 600),
        framerate=32):
        if use_pi_camera:
            self.stream = PiVideoStream(resolution=resolution,
                framerate=framerate)

        else:
            from imutils import WebcamVideoStream
            self.stream = WebcamVideoStream(src=src)
            
    def start(self):
        return self.stream.start()
 
    def update(self):
        self.stream.update()
 
    def read(self):
        return self.stream.read()
 
    def stop(self):
        self.stream.stop()