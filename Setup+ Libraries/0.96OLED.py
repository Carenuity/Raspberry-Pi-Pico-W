from machine import Pin, SoftI2C
import ssd1306
from time import sleep

#Pin assignment 
i2c = SoftI2C(scl=Pin(9), sda=Pin(8))

oled_width = 128
oled_height = 64
print("I2C Scan: ", i2c.scan())
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

oled.text('Sensor data!', 0, 0)
oled.text('Sensor data!', 0, 10)
oled.text('Sensor data!', 0, 20)
        
oled.show()
