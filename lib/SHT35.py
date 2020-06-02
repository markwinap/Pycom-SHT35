import time
from machine import I2C


class SHT35:
    def __init__(self, i2c, address=0x45):
        self.address = address
        self.i2c = i2c

    def readData(self):
        self.i2c.writeto_mem(self.address, 0x24, 0x00)
        time.sleep(0.016)
        self.data = self.i2c.readfrom(self.address, 6)
        self.temperature = self.data[0] * 256 + self.data[1]
        self.celsius = -45 + (175 * self.temperature / 65535.0)
        self.humidity = 100 * (self.data[3] * 256 + self.data[4]) / 65535.0
        return self.celsius, self.humidity

    def getCelsius(self):
        return self.celsius

    def getFahrenheit(self):
        return ((self.celsius * 9) / 5) + 32

    def getHumidity(self):
        return self.humidity
