#!/bin/bash
workon cv
wait
python PhotoboothRunner.py --picam --res 1280x720 --fullscreen
