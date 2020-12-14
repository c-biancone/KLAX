import RPi.GPIO as GPIO
import time
from time import sleep
import os
import subprocess
import pygame

# define GPIO behavior
GPIO.setmode(GPIO.BCM)
GPIO.setup(40, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# set up sound to play
pygame.mixer.init()
pygame.mixer.music.load("smb_coin.wav") # load coin sound effect file

# command to run
start = "emulationstation"
end = "kill $(pidof emulationstation)"
# set terminal environment variable
os.environ['TERM'] = 'xterm-256color'

emulation = None

try:
        while True:
            if GPIO.input(40):
                if emulation is None:
                    # call emulationstation to run as a subprocess within the loop
                    emulation = subprocess.Popen("emulationstation",
                                                shell=True,
                                                preexec_fn=os.setsid)

            else:
                if emulation is not None:
                    os.killpg(emulation.pid)
                    emulation = None
            sleep(0.2)


finally:
    GPIO.cleanup()



"""
try:
    while True:
        #button_state = GPIO.input(40)
        #if button_state == True:
        GPIO.wait_for_edge(40, GPIO.RISING)
        print("HIGH")

        pygame.mixer.music.play()

        subprocess.call(start.split())

        #while GPIO.input(40) == True:
            #time.sleep(5)
        break

except KeyboardInterrupt:
    GPIO.cleanup()

try:
    while True:
        GPIO.wait_for_edge(40, GPIO.RISING)

        pygame.mixer.music.play()

        subprocess.call(end.split())

        #while GPIO.input(40) == True:
            #time.sleep(5)

except KeyboardInterrupt:
    GPIO.cleanup()"""


