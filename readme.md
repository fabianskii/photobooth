Photobooth by Fabian Isele & Philipp Schmitt for Autonome Systeme Labor at Hochschule Karlsruhe

usage: PhotoboothRunner.py [-h] [--picam] [--res RES] [--fullscreen]

optional arguments:
  -h, --help    show this help message and exit
  --picam       use PiCam instead of USB camera
  --res RES     Camera resolution for PiCam width height e.g. 800x600
  --fullscreen  enable fullscreen
  
examples:

Use with PiCam on raspberry:
python PhotoboothRunner --picam --res 1280x800 

Use with USB webcam (or PiCam mounted as videodevice)
python PhotoboothRunner

Images are always saved in /images folder