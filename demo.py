from gpiozero import AngularServo
from time import sleep

gpio = 12
servo=AngularServo(gpio, min_angle=0, max_angle=180, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000)

def set_angle(angle):
    servo.angle=angle
    sleep(1)

try: 
    while True:
        angle=int(input("Enter Angle 0 to 180: "))
        set_angle(angle)
except KeyboardInterrupt:
    print("Program Stopped")