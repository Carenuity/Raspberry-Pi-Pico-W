from machine import Pin, SoftI2C
import network
import urequests
from time import sleep
import dht
import ssd1306


# Settin up OLED and I2C
i2c = SoftI2C(scl=Pin(9), sda=Pin(8))
oled_width = 128
oled_height = 64
print("I2C Scan: ", i2c.scan())
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

#dht setup
dataPin = Pin(2,Pin.OUT)
sensor = dht.DHT11(dataPin)

#WIFI Setup
WIFI_SSID = " " #Enter wifi
WIFI_PASSWORD = " " #Enter Password

def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print("Connecting to WiFi...")
        wlan.connect(WIFI_SSID, WIFI_PASSWORD)
        while not wlan.isconnected():
            time.sleep(1)
            print("Trying to connect...")
    print("Connected to WiFi:", wlan.ifconfig())

connect_wifi()

# ssid = constants.INTERNET_NAME
# password = constants.INTERNET_PASSWORD
# wlan = network.WLAN(network.STA_IF)
# wlan.active(True)
# wlan.connect(ssid, password)
# while not wlan.isconnected():
# pass

api_key = ' '#Enter your Write API key here
base_url = 'https://api.thingspeak.com/update'


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
        
        #Send sensor data to Thingspeak        
        url = f"{base_url}?api_key={api_key}&field1={tempC}&field2={hum}"
        response = urequests.get(url)
        print(response.text)
        
    except OSError as e:
        print('Error')
        oled.fill(0)
        oled.text('Sensor Error!', 5, 25)
        oled.show()
        
time.sleep(15)
