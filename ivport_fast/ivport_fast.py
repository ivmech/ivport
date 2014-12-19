import RPi.GPIO as gp
import os
import time

os.chdir(os.getcwd())

gp.setwarnings(False)
gp.setmode(gp.BOARD)

gp.setup(7, gp.OUT)
gp.setup(11, gp.OUT)
gp.setup(12, gp.OUT)

def main():
    start = "./ivport_fast.sh start"
    stop = "./ivport_fast.sh stop"
    do = "./ivport_fast.sh capture"

    os.system(start)
    time.sleep(1)

    gp.output(7, False)
    gp.output(11, False)
    gp.output(12, True)
    capture()

    gp.output(7, True)
    gp.output(11, False)
    gp.output(12, True)
    capture()

    gp.output(7, False)
    gp.output(11, True)
    gp.output(12, False)
    capture()

    gp.output(7, True)
    gp.output(11, True)
    gp.output(12, False)
    capture()

    time.sleep(1)
    os.system(stop)

def capture():
    do = "./ivport_fast.sh capture"
    #time.sleep(0.7)
    os.system(do)
    time.sleep(0.3)

if __name__ == "__main__":
    main()

    gp.output(7, False)
    gp.output(11, False)
    gp.output(12, True)
