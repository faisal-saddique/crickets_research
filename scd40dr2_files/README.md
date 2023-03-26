# Sensirion Raspberry Pi I2C SCD4x Driver

This document explains how to set up the SCD4x sensor to run on a Raspberry Pi
using the provided code.

[<center><img src="images/SCD41_Development_Board.png" width="300px"></center>](https://sensirion.com/my-scd-ek)

Click [here](https://sensirion.com/my-scd-ek) to learn more about the SCD4x
sensor and the SCD41 Evaluation Kit Board.

## Setup Guide

### Connecting the Sensor

Your sensor has the four different connectors: VCC, GND, SDA, SCL. Use
the following pins to connect your SCD4x:

 *SCD4x*  |    *Raspberry Pi*    | *Jumper Wire*
 :------: | :------------------: | :-----------:
   VCC    |        Pin 1         |      Red
   GND    |        Pin 6         |     Black
   SDA    |        Pin 3         |     Green
   SCL    |        Pin 5         |     Yellow

<center><img src="images/GPIO-Pinout-Diagram.png" width="900px"></center>

To check the address of connected I2C devices, you can use the i2cdetect command. Open a terminal window and enter the following command:

`sudo i2cdetect -y 1`

Sure, here are the instructions:

To check the address of connected I2C devices, you can use the i2cdetect command. Open a terminal window and enter the following command:

Copy code
sudo i2cdetect -y 1
This will show a table of addresses of all I2C devices connected to bus 1, which is the bus typically used by the Raspberry Pi. Look for an address that matches the address of your SCD4x sensor. By default, the SCD4x sensor has an I2C address of 0x61, but this may have been changed if you have multiple sensors connected to the same bus.

Once you have identified the address of your SCD4x sensor, replace the value 0x34 in the Scd4xI2cDevice constructor with the correct address. For example, if the address of your sensor is 0x61, the line of code should be:

`scd4x = Scd4xI2cDevice(I2cConnection(i2c_transceiver, 0x61))`

Also, ensure that the SDA and SCL pins of the Raspberry Pi are connected to the corresponding pins of the SCD4x sensor, as per the table in the setup guide.