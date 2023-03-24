## Reading Analog Sensors Using Raspberry Pi

It is possible to read analog inputs with Raspberry Pi using an analog-to-digital converter (ADC) chip. The Raspberry Pi does not have an onboard ADC, which is why an external ADC is required to convert analog signals to digital signals that can be processed by the Raspberry Pi.

One popular ADC chip for use with Raspberry Pi is the ADS1115, which is a 16-bit ADC with four channels. 

First, we'll need to enable I2C on RPI. Here are the instructions to enable I2C on Raspberry Pi:
1.	Open the terminal on your Raspberry Pi and type the following command to open the Raspberry Pi configuration tool:
`sudo raspi-config`
2.	Use the arrow keys to navigate to Interfacing Options and press Enter.
3.	Navigate to I2C and press Enter.
4.	When prompted to enable I2C, select Yes and press Enter.
5.	Reboot the Raspberry Pi by typing the following command in the terminal:
`sudo reboot`
6.	After the Raspberry Pi has rebooted, open the terminal and type the following command to check if I2C is enabled:
`ls /dev/*i2c*`
You should see the output /dev/i2c-1, which indicates that I2C is enabled on the Raspberry Pi.

Now we can proceed with the instructions to set up the ADS1115 with the Raspberry Pi:


1. First, connect the ADS1115 to the Raspberry Pi using the I2C interface. The ADS1115 has four pins: VDD, GND, SDA, and SCL. Connect VDD to 3.3V, GND to ground, SDA to SDA1, and SCL to SCL1. You can type this command to see if the ADS1115 is successfully connected or not:

`sudo i2cdetect -y 1`

2. Install the necessary software libraries by opening the terminal on your Raspberry Pi and typing the following commands:

```
sudo apt-get update
sudo apt-get install build-essential python-dev python-smbus python-pip
sudo pip install RPI.GPIO
sudo pip install Adafruit-Blinka
```

3. Next, install the Adafruit Python ADS1x15 library by typing the following command in the terminal:

`sudo pip install adafruit-circuitpython-ads1x15`

4. Now you can write a Python script to read the analog inputs. Here's an example script that reads from the first channel of the ADS1115:

```
import time
import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create the ADC object using the I2C bus
ads = ADS.ADS1015(i2c,address=0x49)

chan0 = AnalogIn(ads, ADS.P0)
#chan1 = AnalogIn(ads, ADS.P1)

# Create differential input between channel 0 and 1
#chan = AnalogIn(ads, ADS.P0, ADS.P1)

print("{:>5}\t{:>5}".format('raw', 'v'))

while True:
    print("{:>5}\t{:>5.3f}".format(chan0.value, chan0.voltage))
 #   print("{:>5}\t{:>5.3f}".format(chan1.value, chan1.voltage))
    time.sleep(0.5)
```

This script uses the adafruit_ads1x15 library to read from the first channel of the ADS1115 and print the voltage to the terminal every half second.

5. Save the script to a file, for example ads1115.py, and run it by typing the following command in the terminal:

`python ads1115.py`

You should see the voltage readings printed to the terminal.