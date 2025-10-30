import network
import time
import urequests
from machine import Pin

# Wi-Fi credentials
ssid = '  '
password = '  '

# PIR sensor pin
pir = Pin(14, Pin.IN)   # change pin if needed

def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('Connecting to WiFi...')
        wlan.connect(ssid, password)
        while not wlan.isconnected():
            time.sleep(1)
    print('WiFi connected:', wlan.ifconfig())

# Send data to Flask API (to be stored in MongoDB)
def send_data_to_api(motion_detected):
    url = 'http://192.168.100.11:5000/api/pir'  # Flask endpoint
    headers = {'Content-Type': 'application/json'}
    payload = {'motion': motion_detected}
    try:
        response = urequests.post(url, json=payload, headers=headers)
        if response.status_code == 201:
            print('Data successfully sent:', response.json())
        else:
            print('Failed to send data:', response.status_code, response.text)
    except Exception as e:
        print('Error sending data:', e)

def main():
    connect_wifi()
    print("PIR sensor active... monitoring motion.")
    while True:
        motion_detected = pir.value()
        if motion_detected:
            print("Motion detected!")
            send_data_to_api(True)
        else:
            print("No motion detected.")
            send_data_to_api(False)
        time.sleep(5)  # adjust as needed

main()
