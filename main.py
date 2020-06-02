# main.py -- put your code here!
import time
from machine import I2C
from SHT35 import SHT35

sensor = SHT35(I2C(0, I2C.MASTER, baudrate=20000))


while True:
    time.sleep(5)
    c, h = sensor.readData()
    print('C:{} - H:{}'.format(c, h))
    # Or
    # sensor.readData()
    # print(sensor.getCelsius())
    # print(sensor.getFahrenheit())
    # print(sensor.getHumidity())
