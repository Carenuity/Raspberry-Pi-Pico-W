from ld2410 import *
from machine import UART, Pin
from time import sleep

# 38400
uart = UART(1, baudrate=256000, tx=Pin(4), rx=Pin(5))

radar = LD2410(uart)
# (self.target_state, self.moving_distance, self.moving_energy, self.stationary_distance,
# self.stationary_energy, self.detection_distance)
while True:
    radar.update()
 
    # print(radar.get_reports())
    print(uart.read())
    t_state, m_distance, m_energy, s_distance, s_energy, d_distance = radar.get_target_data()
    
    print(f"TState: {t_state} MDistance: {m_distance} MEnergy: {m_energy} SDistance: {s_distance} SEnergy: {s_energy} DDistance: {d_distance}")
    
    sleep(1)

