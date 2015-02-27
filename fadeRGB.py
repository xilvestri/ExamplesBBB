import Adafruit_BBIO.PWM as PWM
import time
red1 = "P9_16"
green1 = "P8_19"
blue1 = "P9_14"
red2 = "P9_22"
blue2 = "P9_21"
red3 = "P9_31"
blue3 = "P9_29"
PWM.start(red1, 0)
PWM.start(blue1, 0)
PWM.start(green1, 0)
PWM.start(red2, 0)
PWM.start(blue2, 0)
PWM.start(red3, 0)
PWM.start(blue3, 0)

def fade(colorA, colorB, ignore_color):
    PWM.set_duty_cycle(ignore_color, 0)
    for i in range(0, 100):
     PWM.set_duty_cycle(colorA, 100-i)
     PWM.set_duty_cycle(colorB, i)
     time.sleep(0.05)
while True:
    fade(blue1, red1, green1)
    fade(blue2, red2, green1)
    fade(blue3, red3, green1)
