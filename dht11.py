from machine import Pin
from time import sleep
import dht

dataPin = Pin(2, Pin.OUT) #Connect the dht's data pin to GPIO2 of the pico w 

sensor = dht.DHT11(dataPin)

print('DHT11 Sensor data')

while True:
    try:
        sensor.measure()
        tempC = sensor.temperature()
        hum = sensor.humidity()
        print(f'Temperature: {tempC}°C')
        print(f'Humidity: {hum}%')
    except OSError as e:
        print(f'Failed to read sensor: {e}')
    
    sleep(2) #delay for 2 seconds before reading data again
