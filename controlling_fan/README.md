## Control fan and pump using RPI and relays

Here's a general guide on how to control two devices running on 12V using relays and a Raspberry Pi:
Materials needed:

-	Raspberry Pi (any model should work)
-	2-channel relay module (12V)
-	12V power supply (the voltage and amperage depend on the specific devices you want to control)
-	Jumper wires
-	Two devices to control (must be rated for 12V and should not draw more current than the relay module can handle)

### Step 1: Connect the power supply to the relay module
-	Connect the positive terminal of the power supply to the "COM" pin on the relay module
-	Connect the negative terminal of the power supply to the negative terminal of each device

### Step 2: Connect the relay module to the Raspberry Pi
-	Connect one of the relay module's control pins ("IN1" or "IN2") to a GPIO pin on the Raspberry Pi (e.g. GPIO17)
-	Connect the relay module's other control pin to another GPIO pin on the Raspberry Pi (e.g. GPIO18)
-	Connect the "GND" pin on the relay module to any available ground pin on the Raspberry Pi
-	Connect the "VCC" pin on the relay module to 5V pin on Raspberry Pi

### Step 3: Connect the devices to the relay module
-	Connect the positive terminal of one of the devices to the relay module's "NO" (normally open) terminal for channel 1
-	Connect the other device to the relay module's "NO" (normally open) terminal for channel 2

### Step 4: Install the necessary software on the Raspberry Pi
-	Create a new Python script using your preferred text editor (e.g. "nano relay_control.py")

### Step 5: Write the Python script to control the relays Here's an example script that you can modify to suit your needs:


```
import RPi.GPIO as GPIO
import time

# Set the GPIO pins for the relay control
relay1_pin = 17
relay2_pin = 18

# Set the GPIO mode
GPIO.setmode(GPIO.BCM)

# Set the GPIO pins as output
GPIO.setup(relay1_pin, GPIO.OUT)
GPIO.setup(relay2_pin, GPIO.OUT)

# Turn off both relays initially
GPIO.output(relay1_pin, GPIO.LOW)
GPIO.output(relay2_pin, GPIO.LOW)

# Function to turn on/off relay 1
def toggle_relay1():
    if GPIO.input(relay1_pin):
        GPIO.output(relay1_pin, GPIO.LOW)
    else:
        GPIO.output(relay1_pin, GPIO.HIGH)

# Function to turn on/off relay 2
def toggle_relay2():
    if GPIO.input(relay2_pin):
        GPIO.output(relay2_pin, GPIO.LOW)
    else:
        GPIO.output(relay2_pin, GPIO.HIGH)

# Main loop
while True:
    # Prompt the user to toggle a relay
    print("Enter '1' to toggle relay 1, '2' to toggle relay 2, or 'q' to quit.")
    choice = input("> ")

    # Toggle the selected relay or quit the program
    if choice == '1':
        toggle_relay1()
    elif choice == '2':
        toggle_relay2()
    elif choice == 'q':
        GPIO.cleanup()
        break

```

This script uses two functions to toggle each of the relays, and a simple loop to prompt the user for input to toggle a relay or quit the program.

For more details on how the relays work, you can go through this article written by RandomNerdTutorials:

https://randomnerdtutorials.com/guide-for-relay-module-with-arduino/