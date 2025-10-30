import network
import time
import urequests
from machine import Pin
import onewire, ds18x20

# WiFi credentials
ssid = ' '
password = ' '

# Initialize DS18B20 on pin 2
dat = Pin(2)
ds_sensor = ds18x20.DS18X20(onewire.OneWire(dat))

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
def send_data_to_api(temperature):
    url = 'http://192.168.100.11:5000/api/ds18b20'  # Flask endpoint for DS18B20
    headers = {'Content-Type': 'application/json'}
    payload = {'temperature': temperature}
    
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
    roms = ds_sensor.scan()  # Scan for connected DS18B20 sensors
    print('Found DS18B20 devices:', roms)
    
    while True:
        try:
            ds_sensor.convert_temp()
            time.sleep_ms(750)  # Wait for temperature conversion
            
            for rom in roms:
                temperature = round(ds_sensor.read_temp(rom), 2)
                print(f'Temperature: {temperature} °C')
                send_data_to_api(temperature)
            
            time.sleep(5)
        except OSError as os_err:
            print(f"Sensor error: {os_err}")
        except Exception as err:
            print(f"General error: {err}")

main()
