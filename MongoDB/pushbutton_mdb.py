import network
import time
import urequests
from machine import Pin

# Wi-Fi credentials
ssid = '  '
password = '  '

# Pushbutton pin
button = Pin(12, Pin.IN, Pin.PULL_UP)  # use internal pull-up resistor

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
def send_data_to_api(button_state):
    url = 'http://192.168.100.11:5000/api/button'  # Flask endpoint
    headers = {'Content-Type': 'application/json'}
    payload = {'button_state': button_state}
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
    last_state = None
    print("Monitoring button state...")
    while True:
        current_state = button.value()  # 1 = not pressed, 0 = pressed
        if current_state != last_state:  # send only when state changes
            if current_state == 0:
                print("Button pressed!")
                send_data_to_api("Pressed")
            else:
                print("Button released!")
                send_data_to_api("Released")
            last_state = current_state
        time.sleep(0.1)  # debounce delay

main()
