import network
import time
import urequests
from machine import Pin, SoftI2C
import bh1750

# WiFi credentials
ssid = ' '
password = ' '

# Initialize BH1750 (SCL = Pin 9, SDA = Pin 8 — change if needed)
i2c = SoftI2C(scl=Pin(9), sda=Pin(8))
sensor = bh1750.BH1750(i2c)

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
def send_data_to_api(lux):
    url = 'http://192.168.100.11:5000/api/bh1750'  # Flask endpoint for BH1750
    headers = {'Content-Type': 'application/json'}
    payload = {'lux': lux}
    
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
            lux = sensor.luminance(bh1750.BH1750.CONT_HIRES_1)  # Read lux value
            print('Light Intensity:', lux, 'lx')
            send_data_to_api(lux)
            time.sleep(5)
        except OSError as os_err:
            print(f"Error reading sensor: {os_err}")

main()
