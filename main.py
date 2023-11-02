# Created by Alex James (guide from arduino site) 
# Created on Oct. 2023
# rotates a servo with a potentiometer 

import time
import board
import pwmio
from adafruit_motor import servo

Servo servoNumber1;  // create servo object 

int potentiometer = 1;  // Sets potentiometer to analog pin1
int value;    // variable to read the value from the analog pin

void setup() {
  servoNumber1.attach(2);  
}

void loop() {
  value = analogRead(potentiometer);      // reads the value of the potentiometer 
  value = map(value, 0, 1000, 0, 180);    // uses the map fucntion to change scale to degrees
  servoNumber1.write(value);                  
  delay(15);                        
}
