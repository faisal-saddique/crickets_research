import time
import math
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
from sensirion_i2c_driver import LinuxI2cTransceiver, I2cConnection
from sensirion_i2c_scd import Scd4xI2cDevice
import sht3x
import RPi.GPIO as GPIO

# Set the GPIO pins for the relay control
relay1_pin, relay2_pin = 17, 18

# Set the GPIO mode and pins as output
GPIO.setmode(GPIO.BCM)
GPIO.setup((relay1_pin, relay2_pin), GPIO.OUT, initial=GPIO.LOW)

# Functions to toggle relays


def toggle_relay(pin):
    GPIO.output(pin, not GPIO.input(pin))


# Values for MQ-137 Sensor
RL = 4.7  # The value of resistor RL is 4.7K
m = -0.3219  # Enter calculated Slope
b = -0.1932  # Enter calculated intercept
Ro = 20  # Enter found Ro value from measure_ro.py after running it for 10 hours

# Setup SHT3x and SCD4x sensors
sht3x_obj = sht3x.SHT3x()

with LinuxI2cTransceiver('/dev/i2c-1') as i2c_transceiver:
    # Please refer to instructions in scd40dr2_files\README.md to find the address of your sensor
    scd4x = Scd4xI2cDevice(I2cConnection(i2c_transceiver, 0x34))

while True:
    # Measure from MQ-137 Sensor
    i2c = busio.I2C(board.SCL, board.SDA)
    ads = ADS.ADS1115(i2c,address=0x49) # Please make sure to replace 0x49 with the correct I2C address
    chan = AnalogIn(ads, ADS.P0)
    VRL = chan.voltage  # Voltage drop across the MQ sensor
    Rs = ((5.0*RL)/VRL)-RL  # Use formula to get Rs value
    ratio = Rs/Ro  # find ratio Rs/Ro
    ppm = pow(10, ((math.log10(ratio)-b)/m))  # use formula to calculate ppm
    print("NH3 (ppm) = ", ppm)  # Display ammonia in ppm on serial monitor
    print("Voltage = ", VRL, "V")  # Display voltage on serial monitor

    # Measure from SCD4x and SHT3x sensors
    # Make sure measurement is stopped, else we can't read serial number or start a new measurement
    scd4x.stop_periodic_measurement()
    print("scd4x Serial Number: {}".format(scd4x.read_serial_number()))
    scd4x.start_periodic_measurement()

    co2, temperature, humidity = scd4x.read_measurement()
    sht_temperature, sht_humidity = sht3x_obj.read_temperature_humidity()

    # use default formatting for printing output:
    print("CO2: {}, Temperature: {:.2f} C, SHT Temperature: {:.2f} C, Humidity: {:.2f} %, SHT Humidity: {:.2f} %".format(
        co2, temperature, sht_temperature, humidity, sht_humidity))
    

    # Prompt the user to toggle a relay
    choice = input("Enter '1' to toggle relay 1, '2' to toggle relay 2, or 'q' to quit.\n> ")

    # Toggle the selected relay or quit the program
    if choice == '1':
        toggle_relay(relay1_pin)
    elif choice == '2':
        toggle_relay(relay2_pin)
    elif choice == 'q':
        GPIO.cleanup()
        break
    time.sleep(1)