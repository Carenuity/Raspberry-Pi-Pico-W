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

<img width="741" height="365" alt="image" src="https://github.com/user-attachments/assets/b3ef932a-5418-45e6-b28b-04b06f4778f1" />

Eg...

<img width="504" height="307" alt="image" src="https://github.com/user-attachments/assets/cecbcfe9-7a15-48c5-9381-94aa4b679ba2" />


B). External Libraries (Need to Be Downloaded and Uploaded)

Some libraries are not built-in and must be added manually.
These include drivers for sensors, displays, and additional modules such as:

<img width="707" height="281" alt="image" src="https://github.com/user-attachments/assets/0db2bcc8-6912-4ddc-b9d3-d71f82e804b2" />

**How to Upload External Libraries to the Pico W**

1.	Download the required .py library files from trusted sources such as:

-	MicroPython Library Repository: https://github.com/micropython/micropython-lib

-	Sensor manufacturer’s GitHub (e.g., Adafruit, etc.)

2.	Open Thonny IDE and connect your Pico W via USB.

*Go to View → Files to open the file browser pane.*

3.	In Thonny:

-	The left top panel shows your computer files.
-	The left bottom panel shows the files stored on your Pico W

<img width="673" height="547" alt="image" src="https://github.com/user-attachments/assets/2d1bbef2-06d5-41c9-97e2-2bd2a4864f7d" />

4.	Drag and drop or right-click → “Upload to /” to copy the library file to the Pico W.

5.	Confirm the file appears in the right panel under /.

6.	Once uploaded, you should see the library listed in the right-hand (Pico W) pane under 

<img width="853" height="204" alt="image" src="https://github.com/user-attachments/assets/7bdaa2fd-ad8c-4bf7-9d0e-b26786cb5641" />

## 4. Programming the Raspberry Pi Pico W

Example: Blink the Onboard LED

<img width="878" height="506" alt="image" src="https://github.com/user-attachments/assets/b4b356f0-8b4e-458c-8fa7-72e9c6b6aab8" />

Running Code

-	Save your code as blink.py. [To make it auto-run on boot, save as main.py]
-	You can also click Run (▶) to execute manually from Thonny.

https://github.com/user-attachments/assets/dfef3ef2-d570-4542-bace-dd1a96eb6d98

With Carenuity's triple adapter:

https://github.com/user-attachments/assets/dcfe16dd-37d6-450a-a259-b81665125249

## 5. Interfacing with a 0.96’’ OLED Display (SSD1306) Wiring (I2C)

<img width="292" height="267" alt="image" src="https://github.com/user-attachments/assets/ca828ea1-4c40-49dc-abda-73699bef768d" />

Upload the ssd1306 library from: https://gist.github.com/cwyark/d7f2becd84b0b69b05a83315bf84c467 

Example code: 

<img width="859" height="543" alt="image" src="https://github.com/user-attachments/assets/32233f0c-d8f6-4e30-a2ac-a794d36866c2" />


Display:


![WhatsApp Image 2025-10-27 at 12 48 31 AM](https://github.com/user-attachments/assets/7b1a02d8-6bd8-4f50-b262-d5bdfcd18aea) 

## Connecting and programming a sensor(DHT11) to the Pico W:

**To display the sensor readsings on the console:**
- Install the necessary libraries:  dht.py
- Connect the data pin (D4 in case of DHT Shield) to GPIO 0 on the pico W
- Get the code from the repository: https://github.com/Carenuity/Raspberry-Pi-Pico-W/blob/main/dht11.py 

![WhatsApp Image 2025-10-27 at 1 34 16 AM (1)](https://github.com/user-attachments/assets/fe077513-15c6-449f-924d-dc56cdc6a65d)



**To display the sensor readsings on an OLED display (0.96 inch OLED display):**
- Install the necessary libraries: ssd1306.py and dht.py
- Connect the data pin (D4 in case of DHT Shield) to GPIO 0 on the pico W
- Connect the SCL pin to GPIO9 and SCL Pin to GPIO8
- Get the Code from the repository: https://github.com/Carenuity/Raspberry-Pi-Pico-W/blob/main/dht11_0.96OLED.py

![WhatsApp Image 2025-10-27 at 1 34 12 AM](https://github.com/user-attachments/assets/003f16be-d02e-4633-a012-bc3bba3f6bbf)




![WhatsApp Image 2025-10-27 at 1 34 12 AM (1)](https://github.com/user-attachments/assets/759748bd-26bc-4f03-8c82-17178f451d3f)


![WhatsApp Image 2025-10-27 at 1 34 12 AM (2)](https://github.com/user-attachments/assets/3394badb-3344-49f9-939a-5e4d7d8b9b9a)

## 6. Connecting to Wi-Fi

<img width="519" height="397" alt="image" src="https://github.com/user-attachments/assets/7533a960-217c-4294-adc0-03ab96003804" />

The display on the console:

<img width="914" height="239" alt="image" src="https://github.com/user-attachments/assets/cee7cac6-7c7e-45b6-8e9d-db788de54866" />

## 7. Sending Data to IoT Platforms

### 8. Adafruit IO

Adafruit IO provides MQTT-based dashboards and feeds.

Setup:

1.	Create an account at https://io.adafruit.com
2.Create a new Feed. This is what will link your database to the code

<img width="1713" height="266" alt="image" src="https://github.com/user-attachments/assets/c28a5922-65ab-4186-a54a-85b92bb3c553" />

<img width="727" height="483" alt="image" src="https://github.com/user-attachments/assets/8eed1cf6-e77a-4b83-95ed-9eda0b26ca79" />

<img width="709" height="478" alt="image" src="https://github.com/user-attachments/assets/c2e33255-b97e-4bbe-a978-8cf107058af6" />

3. Create a new Dashboard. This is where your data will be ddisplayed in a graph

<img width="1471" height="257" alt="image" src="https://github.com/user-attachments/assets/b23af6da-2643-4d37-aa61-e26160a643a8" />

<img width="722" height="439" alt="image" src="https://github.com/user-attachments/assets/b887f61c-32dd-49ad-a8ea-5167819e737a" />

3.Create new block

<img width="1793" height="386" alt="image" src="https://github.com/user-attachments/assets/30c946cd-8351-4cd0-a19c-fb423bec8721" />

<img width="692" height="607" alt="image" src="https://github.com/user-attachments/assets/1371d48f-1448-4141-9018-29647611a196" />

4.	select necessary feed ie. Temperature feed and Humidity Feed > Name block > create new block

<img width="975" height="708" alt="image" src="https://github.com/user-attachments/assets/f0760cf2-f7f9-4b71-a52b-725603da5747" />

5. You should have the following:

<img width="1359" height="559" alt="image" src="https://github.com/user-attachments/assets/11b36c3e-4f7f-417e-868c-0841b0eaf327" />

6.Take note of your Username and API Key

<img width="1159" height="231" alt="image" src="https://github.com/user-attachments/assets/975c3c13-7793-4474-82ab-6e9a1eb3aba2" />


<img width="677" height="508" alt="image" src="https://github.com/user-attachments/assets/b41aebc4-c821-4360-b3fd-db8080b73f88" />

7. Copy and Paste the code from the repository: https://github.com/Carenuity/Raspberry-Pi-Pico-W/blob/main/dht11_0.96OLED_Adafruit.py

- On the Console you will see:


<img width="305" height="217" alt="image" src="https://github.com/user-attachments/assets/e8299a4a-fe09-430e-b052-2c1f135964fc" />

-On the Adafruit IO Dashboards you will see:

<img width="1493" height="492" alt="image" src="https://github.com/user-attachments/assets/c4943dd2-cd78-44a2-a684-35fde9e5f8aa" />

### THINGSPEAK
1.Create a ThingSpeak account from: https://thingspeak.mathworks.com/login?skipSSOCheck=true
2.Create a new channel

<img width="1273" height="165" alt="image" src="https://github.com/user-attachments/assets/cbe45d09-7438-4cc8-9c99-4500de02af02" />


<img width="842" height="512" alt="image" src="https://github.com/user-attachments/assets/5db2e346-7eba-4b2a-93a9-8eeb3b20177c" />


<img width="1086" height="229" alt="image" src="https://github.com/user-attachments/assets/dc771fd0-b00d-4413-85db-d44201029802" />


3.Create 2 suitable fields: Temperature and Humidity

<img width="842" height="512" alt="image" src="https://github.com/user-attachments/assets/65518d08-38db-414d-8d6b-3a6abd12aa0a" />


4.Take note of the API Key

<img width="842" height="516" alt="image" src="https://github.com/user-attachments/assets/b2304be5-f826-4711-9cd9-d2978de9d9dc" />


5.Copy and paste the code from the repository: https://github.com/Carenuity/Raspberry-Pi-Pico-W/blob/main/dht11_0.96OLED_Thingspeak.py
6.You will see:

<img width="1281" height="425" alt="image" src="https://github.com/user-attachments/assets/bd87a27c-c966-4a76-b374-0c09a71a8645" />


### FIREBASE

1. Create Firebase Account
-	Go to Firebase Console: https://console.firebase.google.com/u/0/
-	Click "Get Started" or "Go to Console"
-	Sign in with your Google account (or create one if you don't have it)

2. Create a New Project
-	Click "Add project" or "Create a project"
-	Enter a project name (e.g., DHT11-Sensor-Project)
=	Click "Continue"
=	Disable Google Analytics or leave it enabled
-	Click "Create project"

3. Set Up Realtime Database
-	In the left sidebar, click "Build" → "Realtime Database"
-	Click "Create Database"
-	Select a location closest to you (e.g., us-central1)
-	Choose "Start in test mode" (for development)

> Note: Test mode allows public access. For production, you'll need to configure security rules.

*Configure Database Rules*
After creating the database:
1.	Click the "Rules" tab
2.	You'll see default rules. For testing, use: 

<img width="252" height="146" alt="image" src="https://github.com/user-attachments/assets/c6cc41dc-a93f-4374-afad-0770f9deabae" />

> Note: These rules allow anyone to read/write to your database. 


4. Get Your Firebase URL
-	In the Realtime Database page, look at the top
-	You'll see your database URL: https://YOUR-PROJECT-ID-default-rtdb.firebaseio.com/
-	Copy this URL - you'll need it for the code

Example: https://dht11-firestore-717dd-default-rtdb.firebaseio.com/

5. Enable Authentication
-	In the left sidebar, click "Build" → "Authentication"
-	Click "Get started"
-	Go to the "Sign-in method" tab
-	Click on "Email/Password"
-	Toggle "Enable" to ON
-	Click "Save"

*Create a User Account*

-	Go to the "Users" tab
-	Click "Add user"
-	Enter an email address (can be any email, doesn't need to be real) 

>	Example: myproject@example.com

-		Enter a password (minimum 6 characters)
  
>	Example: MySecurePass123

	- Click "Add user"
 - Save these credentials - you'll need them in your code

6. Get Your API Key
-	Click the gear icon ⚙️ next to "Project Overview" in the left sidebar
-	Select "Project settings"
-	Scroll down to the "Your apps" section
-	Look for "Web API Key"
-	Copy this key - you'll need it for authentication
Example:
AIzaSyAhZXCCUpwC8UlRKW1aJPDkw0nmfr4_mTo

7. Configure the Code
- Get the code from the repository: 
- Edit the firebase URL, API, Wifi credentials on the code

8. View Your Sensor Data

In Firebase Console
-	Go to Firebase Console
-	Select your project
-	Click "Realtime Database" in the left sidebar
-	You'll see your data in a tree structure







