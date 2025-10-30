import network
import time
import urequests
import dht
from machine import Pin

# WiFi credentials
ssid = ' '
password = ' '

# Initialize DHT22 sensor on pin 2
sensor = dht.DHT22(Pin(2))

def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('Connecting to WiFi...')
        wlan.connect(ssid, password)
        while not wlan.isconnected():
            time.sleep(1)
    print('WiFi connected:', wlan.ifconfig())

# Function to send data to Flask API
def send_data_to_api(temperature, humidity):
    url = 'http://192.168.100.11:5000/api/dht22'  # Flask endpoint for DHT22
    headers = {'Content-Type': 'application/json'}
    payload = {
        'temperature': temperature,
        'humidity': humidity
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
            sensor.measure()
            temperature = round(sensor.temperature(), 2)
            humidity = round(sensor.humidity(), 2)
            
            print(f"Temperature: {temperature} °C, Humidity: {humidity} %")
            
            send_data_to_api(temperature, humidity)
            
            time.sleep(5)
        except OSError as os_err:
            print(f"Sensor error: {os_err}")
        except Exception as err:
            print(f"General error: {err}")

main()
