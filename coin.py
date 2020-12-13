import RPi.GPIO as GPIO
import time
import os
import subprocess
import pygame

# define GPIO behavior
GPIO.setmode(GPIO.BOARD)
GPIO.setup(40, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# set up sound to play
pygame.mixer.init()
pygame.mixer.music.load("smb_coin.wav")

# command to run
start = "emulationstation"
end = "kill $(pidof emulationstation"
# set terminal environment variable
os.environ['TERM'] = 'xterm-256color'


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
    GPIO.cleanup()