import time
import math
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn


RL = 4.7  # The value of resistor RL is 47K
m = -0.3219  # Enter calculated Slope
b = -0.1932  # Enter calculated intercept
Ro = 20  # Enter found Ro value from measure_ro.py after running it for 10 hours

i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(i2c, 0x34)
chan = AnalogIn(ads, ADS.P0)

while True:
    VRL = chan.voltage  # Voltage drop across the MQ sensor
    Rs = ((5.0*RL)/VRL)-RL  # Use formula to get Rs value
    ratio = Rs/Ro  # find ratio Rs/Ro
    ppm = pow(10, ((math.log10(ratio)-b)/m))  # use formula to calculate ppm

    print("NH3 (ppm) = ", ppm)  # Display ammonia in ppm on serial monitor
    print("Voltage = ", VRL, "V")  # Display voltage on serial monitor

    time.sleep(0.2)