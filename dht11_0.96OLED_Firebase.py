import network
import urequests
import time
import random
import dht
from machine import Pin, SoftI2C
import ssd1306
from time import sleep

# WIFI Setup
WIFI_SSID = " "  # Enter WIFI Name
WIFI_PASSWORD = " " # Enter WIFI Password

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

# Initialize DHT11 sensor on Pin 2
dataPin = Pin(2, Pin.OUT)
sensor = dht.DHT11(dataPin)

def dht_data():
    sensor.measure()  # Must measure before reading
    return {
        'temperature': sensor.temperature(),
        'humidity': sensor.humidity()
    }

# Pin assignment for OLED
i2c = SoftI2C(scl=Pin(9), sda=Pin(8))
oled_width = 128
oled_height = 64
print("I2C Scan: ", i2c.scan())
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

# Firebase configuration
firebase_url = 'PUT YOU FIREBASE URL HERE'

auth_data = {
    "email": "cybrin101@gmail.com",
    "password": "Sacho3280.",
    "returnSecureToken": True
}

# Authenticate with Firebase
auth_response = urequests.post("https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key=YOU API KEY", json=auth_data)
auth_response_data = auth_response.json()
print(auth_response_data)
auth_response.close()
local_id = auth_response_data.get('localId')
id_token = auth_response_data.get('idToken')  # FIXED: Added this line - was missing!
print(local_id)

# Main loop to read and send DHT data
while True:
    # Read sensor data
    dhtData = dht_data()
    tempC = dhtData['temperature']
    hum = dhtData['humidity']
    
    print(dhtData)
    
    # Update OLED display
    oled.fill(0)  # Clear display
    oled.text('DHT Sensor data', 0, 0)
    oled.text("Temp: " + str(tempC) + ' C', 0, 20)
    oled.text("Hum: " + str(hum) + ' %', 0, 40)
    oled.show()
    
    # Send data to Firebase with authentication
    authenticated_url = firebase_url + "?auth=" + id_token
    response = urequests.post(authenticated_url, json=dhtData)
    data = response.json()
    response.close()
    print(data)
    
    time.sleep(5)  # Changed to 5 seconds - better for DHT11 and Firebase
