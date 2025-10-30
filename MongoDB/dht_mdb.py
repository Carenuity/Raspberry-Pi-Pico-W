import network
import time
import urequests
import dht
from machine import Pin

ssid = ' ' #Put your WIFI SSID here
password = ' '#Put your WIFI Passowrd here

sensor = dht.DHT11(Pin(2))

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
def send_data_to_api(temperature, humidity):
    url = 'http://192.168.100.11:5000/api/dht' # IP Address of the machine runninig the server code
    headers = {'Content-Type': 'application/json'}
    payload = {'temperature': temperature, 'humidity': humidity}
    response = urequests.post(url, json=payload, headers=headers)
    
    if response.status_code == 201:
        print('Data successfully sent:', response.json())
    else:
        print('Failed to send data:', response.status_code, response.text)

def main():
    connect_wifi()
    while True:
        try:
            sensor.measure()  
            temperature = sensor.temperature()  
            humidity = sensor.humidity() 
            
            print('Temperature:', temperature, 'C', 'Humidity:', humidity, '%')
            
            send_data_to_api(temperature, humidity)
            
            time.sleep(5)
        except OSError as os_err:
            print(f"Error: {os_err}")

main()

