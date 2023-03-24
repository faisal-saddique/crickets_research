## Connect MQ137 Sensor with Raspberry Pi through ADS1115

Here's a short guide on how to connect the MQ137 gas sensor to the ADS1115, which is connected to Raspberry Pi:

1. Connect the VCC pin of the MQ137 sensor to the 5V pin of the Raspberry Pi.
2. Connect the GND pin of the MQ137 sensor to the GND pin of the Raspberry Pi.
3. Connect the OUT pin of the MQ137 sensor to one of the analog input pins (A0 in our case) of the ADS1115.

Follow the instructions I provided in read_analog_inputs_rpi.md to set up the ADS1115 with the Raspberry Pi.