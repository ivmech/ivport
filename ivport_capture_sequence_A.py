#!/usr/bin/python
#
# This file is part of Ivport.
# Copyright (C) 2015 Ivmech Mechatronics Ltd. <bilgi@ivmech.com>
#
# Ivport is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ivport is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

#title           :ivport_capture_sequence_A.py
#description     :the closest approach to simultaneous capturing
#author          :Caner Durmusoglu
#date            :20150425
#version         :0.1
#usage           :python ivport_capture_sequence_A.py
#notes           :A indicates that Ivport jumper setting
#python_version  :2.7
#==============================================================================

import time
import picamera

import RPi.GPIO as gp

gp.setwarnings(False)
gp.setmode(gp.BOARD)

JUMPER_SETTING = 'A'

# Jumper Pin assignment
IVJP = {'A': (11, 12), 'C': (21, 22), 'B': (15, 16), 'D': (23, 24)}
pins = list(reduce(lambda x,y: x+y, IVJP.values()))
pins.sort()
DIVJP = {i+1 : x for i,x in enumerate(pins)}
f1Pin, f2Pin = IVJP[JUMPER_SETTING]
ePin = 7

gp.setup(ePin, gp.OUT)
gp.setup(f1Pin, gp.OUT)
gp.setup(f2Pin, gp.OUT)

gp.output(ePin, False)
gp.output(f1Pin, False)
gp.output(f2Pin, True)

frames = 90

cam = 1

def cam_change():
    global cam
    gp.setmode(gp.BOARD)
    if cam == 1:
        # CAM 1 for A Jumper Setting
        gp.output(ePin, False)
        gp.output(f1Pin, False)
        gp.output(f2Pin, True)

    elif cam == 2:
        # CAM 2 for A Jumper Setting
        gp.output(ePin, True)
        gp.output(f1Pin, False)
        gp.output(f2Pin, True)

    elif cam == 3:
        # CAM 3 for A Jumper Setting
        gp.output(ePin, False)
        gp.output(f1Pin, True)
        gp.output(f2Pin, False)

    elif cam == 4:
        # CAM 4 for A Jumper Setting
        gp.output(ePin, True)
        gp.output(f1Pin, True)
        gp.output(f2Pin, False)

    cam += 1
    if cam > 4:
        cam = 1

def filenames():
    frame = 0
    while frame < frames:
        time.sleep(0.007)   # SD Card Bandwidth Correction Delay
        cam_change()        # Switching Camera
        time.sleep(0.007)   # SD Card Bandwidth Correction Delay
        yield 'image%02d.jpg' % frame
        frame += 1

with picamera.PiCamera() as camera:
    camera.resolution = (640, 480)
    camera.framerate = 90
    camera.start_preview()

    # Optional Camera LED OFF
    #gp.setmode(gp.BCM)
    #camera.led = False

    time.sleep(2)    # Camera Initialize
    start = time.time()
    camera.capture_sequence(filenames(), use_video_port=True)
    finish = time.time()

print('Captured %d frames at total %.2ffps' % (frames, frames / (finish - start)))
