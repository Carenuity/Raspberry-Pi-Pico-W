from machine import UART, Pin, SoftI2C
from ld2410 import LD2410
import ssd1306
from time import sleep
import time



#Pin assignment 
i2c = SoftI2C(scl=Pin(9), sda=Pin(8))

oled_width = 128
oled_height = 64
print("I2C Scan: ", i2c.scan())
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)


uart = UART(1, baudrate=256000, tx=4, rx=5)
sensor = LD2410(uart)

while True:
    sensor.update()
    # 0 = No target detected, 1 = Moving target detected, 2 = Stationary target detected, 3= both stationary and moving object detected
    print("Target:", sensor.target_state)
    oled.text(f'Target: {sensor.target_state}', 0, 0)
    #oled.text('Target:'+ str(sensor.target_state), 0, 0)
    
    #How far away a moving object
    print("Moving Distance:", sensor.moving_distance, "cm")
    oled.text(f'M.D: {sensor.moving_distance}', 0, 15)
    
    #Distance to a still object
    print("Stationary Distance:", sensor.stationary_distance, "cm") 
    oled.text(f'S.D: {sensor.stationary_distance}', 0, 30)
    
    # The farthest distance at which the sensor is currently detecting anything
    print("Detection Distance:", sensor.detection_distance, "cm")
    oled.text(f'D.D: {sensor.detection_distance}', 0, 45)
    
    oled.show()
    
    time.sleep(1)





        


