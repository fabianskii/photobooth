import argparse

from Photobooth import Photobooth

parser = argparse.ArgumentParser(description='Photobooth by Fabian Isele & Philipp Schmitt')

parser.add_argument('--picam', action='store_true', help='use PiCam instead of USB camera')

parser.add_argument('--res', action="store", help='Camera resolution for PiCam width height e.g. 800x600')

parser.add_argument('--fullscreen', action='store_true', help='enable fullscreen')

args = parser.parse_args()

resolution = args.res

if resolution:
    res_list = resolution.split("x")
    photobooth = Photobooth(resolution=(int(res_list[0]), int(res_list[1])), use_pi_camera=args.picam,
                            fullscreen=args.fullscreen)
else:
    photobooth = Photobooth(use_pi_camera=args.picam, fullscreen=args.fullscreen)

photobooth.run()
