from machine import Pin, SoftI2C
from time import sleep
import dht
import ssd1306 

# OLED Display Setup (128x64 pixels)
i2c = SoftI2C( scl=Pin(9), sda=Pin(8))
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c,)

# DHT11 Sensor Setup
dataPin = Pin(2, Pin.OUT)
sensor = dht.DHT11(dataPin)

print('DHT11 Sensor data')

while True:
    try:
        #read sensor data        
        sensor.measure()
        tempC = sensor.temperature()
        hum = sensor.humidity()

        #Display Title
        oled.text('DHT Sensor data', 0, 0)
        
        #Display Temperature
        oled.text("Temp: "+str(tempC) + ' C', 0, 20)
        
        #Display Humidity
        oled.text("Hum: "+str(hum) + ' %', 0, 40)

        # Update display
        oled.show()
        
        # Print to console as well
        print(f'Temperature: {tempC}°C')
        print(f'Humidity: {hum}%')
        
        
    except OSError as e:
        print(f'Failed to read sensor: {e}')
        oled.fill(0)
        oled.text('Sensor Error!', 5, 25)
        oled.text('Check wiring', 5, 40)
        oled.show()
    
    # Wait 2 seconds before next reading
    sleep(2)
