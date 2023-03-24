""" Note: The value of Ro will be varying, allow the sensor to pre-heat at least for 10 hours and then use the value of Ro. """

import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# Initialize I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Initialize ADS1115
ads = ADS.ADS1115(i2c)

# Set up analog input pin
chan = AnalogIn(ads, ADS.P0)

# Define RL value
RL = 4.7 # in kilo-ohms

while True:
    analog_value = 0.0
    for i in range(500):
        analog_value += chan.value
        time.sleep(0.001) # delay 1ms between readings
    analog_value /= 500.0 # take average
    VRL = analog_value * 0.0001875 # convert analog value to voltage (5V / 2^15)
    # RS = ((Vc/VRL)-1)*RL is the formula we obtained from datasheet
    Rs = ((5.0 / VRL) - 1) * RL
    # RS/RO is 1 as we obtained from graph of datasheet
    Ro = Rs / 1
    print("Ro at fresh air =", Ro)
    time.sleep(1) # delay 1 second