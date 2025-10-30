import network
import time
import urequests
from machine import Pin
from machine import UART
from ld2410 import LD2410

uart = UART(1, baudrate=256000, tx=4, rx=5)
sensor = LD2410(uart)

ssid = ' ' #Put your WIFI SSID here
password = ' '#Put you WIFI Password here


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
def send_data_to_api(target, moving_distance, stationary_distance, detection_distance):
    url = 'http://192.168.100.11:5000/api/dht' # IP Address of the machine runninig the server code ie. 'http://192.168.100.11:5000/api/dht'
    headers = {'Content-Type': 'application/json'}
    payload = {'target': sensor.target_state, 'moving_distance': sensor.moving_distance, 'stationary_distance': sensor.stationary_distance, 'detection_distance': sensor.detection_distance,}
    response = urequests.post(url, json=payload, headers=headers)
    
    if response.status_code == 201:
        print('Data successfully sent:', response.json())
    else:
        print('Failed to send data:', response.status_code, response.text)

def main():
    connect_wifi()
    while True:
        try:
            sensor.update()
            
            target = sensor.target_state
            moving_distance = sensor.moving_distance
            stationary_distance = sensor.stationary_distance
            detection_distance = sensor.detection_distance 
            
            print("Target:", sensor.target_state) # 0 = No target detected, 1 = Moving target detected, 2 = Stationary target detected, 3= both stationary and moving object detected
            print("Moving Distance:", sensor.moving_distance, "cm") #How far away a moving object
            print("Stationary Distance:", sensor.stationary_distance, "cm") #Distance to a still object
            print("Detection Distance:", sensor.detection_distance, "cm") # The farthest distance at which the sensor is currently detecting anything
                        
            send_data_to_api(target, moving_distance, stationary_distance, detection_distance)
            
            time.sleep(1)
            
        except OSError as os_err:
            print(f"Error: {os_err}")

main()


