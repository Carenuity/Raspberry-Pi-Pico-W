# Raspberry Pi Pico W 

A guide to getting started with the Raspberry Pi Pico W using MicroPython.

**Learn how to:** set up your environment, upload libraries, program using Thonny, interface with sensors and OLED displays, and connect to IoT databases:  ThingSpeak, Firebase, and Adafruit IO.

## 1. Introduction

The Raspberry Pi Pico W is a low-cost microcontroller board based on the RP2040 chip, with built-in Wi-Fi capability.

It’s ideal for IoT projects where you want to connect sensors and upload data to the cloud.

***Key features:***

- Dual-core ARM Cortex-M0+ processor
-	264 KB SRAM, 2 MB Flash
-	Built-in 2.4GHz Wi-Fi (CYW43439)
-	USB programming interface
-	Supports MicroPython and C/C++

<img width="975" height="526" alt="image" src="https://github.com/user-attachments/assets/81ff44d2-d7fb-4cf0-9830-b60ca57f8df7" />


 ## 2. Software Setup
 
### Step 1: Install Thonny IDE

Thonny is the easiest IDE for programming the Pico W in MicroPython.

-	Download and install Thonny from: https://thonny.org
-	Open Thonny and go to: Tools → Options → Interpreter
-	Select:

**Interpreter:** MicroPython (Raspberry Pi Pico)

**Port:** Auto-detect or select the correct USB port.

### Step 2: Install MicroPython on the Pico W

If this is your first time:

1.	Connect the Pico W to your computer while holding the BOOTSEL button.

2.	It appears as a USB drive named RPI-RP2.

3.	Download the latest MicroPython UF2 file for the Pico W from: https://www.raspberrypi.com/documentation/microcontrollers/micropython.html 

4.	Go to the Drag and Drop Micropython section, navigate to the Pico W, Download the .uf2 file.

5.	Drag and drop the .uf2 file onto the RPI-RP2 drive.

6.	The Pico W will reboot and be ready for use… ie disappear as a USB drive (RPI-RP2)

## 3. Libraries

There are two main types of libraries you will use with the Raspberry Pi Pico W:

 A). Built-in Libraries (Pre-installed with MicroPython)
 
These libraries come already included in the MicroPython firmware. You can use them directly without downloading or uploading anything.

Common examples include:




