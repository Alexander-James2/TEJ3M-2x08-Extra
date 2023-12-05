# Alexander James
# Dec. 2023
# Uses a potentiometer to control a servo 

import time
import board
import pwmio
from adafruit_motor import servo
from analogio import AnalogIn 

potentiometer = AnalogIn(board.A0)
pwm = pwmio.PWMOut(board.A1, frequency=50)
ServoNumber1 = servo.Servo(pwm)
scale = 65535 / 180   # Takes the input from potentiometer and scales it to degrees.

while True:
    angle = potentiometer.value / scale
    print (f"Angle: {angle}")
    ServoNumber1.angle = angle 
    time.sleep(0.1)
    