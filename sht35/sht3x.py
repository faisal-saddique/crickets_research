import smbus
import time
import numpy as np


class SHT3x:
    def __init__(self, i2c_addr=0x45, i2c_bus=1):
        self.i2c_addr = i2c_addr
        self.i2c_bus = i2c_bus
        self.bus = smbus.SMBus(self.i2c_bus)

        self.SHT3x_SS = 0x2C
        self.SHT3x_HIGH = 0x06
        self.SHT3x_READ = 0x00

    def read_temperature_humidity(self):
        # MS to SL
        self.bus.write_i2c_block_data(
            self.i2c_addr, self.SHT3x_SS, [self.SHT3x_HIGH])
        time.sleep(0.2)

        # Read out data
        data = self.bus.read_i2c_block_data(self.i2c_addr, self.SHT3x_READ, 6)

        # Devide data into counts Temperature
        t_data = data[0] << 8 | data[1]

        # Devide data into counts Humidity
        h_data = data[3] << 8 | data[4]

        # Convert counts to Temperature/Humidity
        humidity = 100.0*np.float(h_data)/65535.0
        temperature = -45.0 + 175.0*np.float(t_data)/65535.0

        return temperature, humidity