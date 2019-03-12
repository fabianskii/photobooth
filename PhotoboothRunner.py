import argparse

parser = argparse.ArgumentParser(description='Photobooth by Fabian Isele & Philipp Schmitt')

parser.add_argument('camera_resolution', type=int, nargs=2,
                    help='Camera resolution width height e.g. 800 600')

parser.add_argument('--picam', action='store_true',
                    help='use PiCam instead of USB camera')

parser.add_argument('--fullscreen', action='store_true',
                    help='enable fullscreen')

args = parser.parse_args()

print(args.picam)
print(args.fullscreen)
print(str(tuple(args.camera_resolution)))
