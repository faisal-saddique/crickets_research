import sht3x

if __name__ == '__main__':
    sht3x_obj = sht3x.SHT3x()
    temperature, humidity = sht3x_obj.read_temperature_humidity()
    print("Temperature: {:.2f} C, Humidity: {:.2f} %".format(
        temperature, humidity))