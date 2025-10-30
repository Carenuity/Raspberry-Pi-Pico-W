import network
import time
import urequests
from machine import Pin, SoftI2C
import bmp180

# WiFi credentials
ssid = ' '
password = '  '

# Initialize BMP180 (SCL = Pin 9, SDA = Pin 8 — change if needed)
i2c = SoftI2C(scl=Pin(9), sda=Pin(8))
sensor = bmp180.BMP180(i2c)
sensor.oversample_sett = 2  # optional for better accuracy
sensor.sea_level_pressure = 101325  # standard sea-level pressure in Pa

# Connect to WiFi
def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('Connecting to WiFi...')
        wlan.connect(ssid, password)
        while not wlan.isconnected():
            time.sleep(1)
    print('WiFi connected:', wlan.ifconfig())

# Send data to Flask API
def send_data_to_api(temperature, pressure, altitude):
    url = 'http://192.168.100.11:5000/api/bmp180'  # Flask endpoint for BMP180
    headers = {'Content-Type': 'application/json'}
    payload = {
        'temperature': temperature,
        'pressure': pressure,
        'altitude': altitude
    }
    
    try:
        response = urequests.post(url, json=payload, headers=headers)
        if response.status_code == 201:
            print('Data successfully sent:', response.json())
        else:
            print('Failed to send data:', response.status_code, response.text)
        response.close()
    except Exception as e:
        print('Error sending data:', e)

# Main loop
def main():
    connect_wifi()
    while True:
        try:
            temp = round(sensor.temperature, 2)
            pres = round(sensor.pressure, 2)
            alt = round(sensor.altitude, 2)
            
            print(f"Temperature: {temp} °C, Pressure: {pres} Pa, Altitude: {alt} m")
            send_data_to_api(temp, pres, alt)
            
            time.sleep(5)
        except OSError as os_err:
            print(f"Error reading sensor: {os_err}")

main()
