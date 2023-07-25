## Control Multiple PWM fans using Raspberry Pi

If you want to control the speed of all fans at the same time (synchronized control), you can use a PWM splitter or PWM hub (eg. https://www.amazon.com/PWM-Fan-Splitter-Way/dp/B095HDK93L). These devices take a single PWM signal and distribute it to multiple fans, allowing you to control all of them together.

Here's how you can achieve that:

## Components Needed:

- Raspberry Pi (any model with GPIO pins, like Raspberry Pi 3 or 4)
- PWM splitter or PWM hub (number of fan connections as required)
- 10 ARCTIC F8 PWM fans with three wires (VCC, GND, and PWM)
- Power supply (12V) to power all the fans

## Wiring Instructions:

- Connect the VCC wire of each fan to the 12V power supply's positive terminal.
- Connect all the GND wires of the fans to the 12V power supply's negative terminal and also to the Raspberry Pi's ground (GND) pin.
- Connect the PWM wire of each fan to the corresponding fan connection on the PWM splitter or hub.
- Connect the PWM input of the PWM splitter or hub to a GPIO pin on the Raspberry Pi (e.g., GPIO18).

## Python Code: 

The Python code for controlling the fans is:

```python
import RPi.GPIO as GPIO
from time import sleep

# Set the GPIO pin number you are using for PWM control
# attach the PWM pin of the PWM splitter/hub to this pin
pwm_pin = 18

# Initialize the RPi.GPIO library
GPIO.setmode(GPIO.BCM)
GPIO.setup(pwm_pin, GPIO.OUT)

# Create a PWM instance
pwm = GPIO.PWM(pwm_pin, 100)  # Frequency of 100 Hz

# Start the PWM with 0% duty cycle (fan off)
pwm.start(0)

try:
    while True:
        # Change the fan speed from 0% to 100% in increments of 10%
        for speed in range(0, 101, 10):
            pwm.ChangeDutyCycle(speed)
            print(f"All Fans Speed: {speed}%")
            sleep(5)  # Wait for 5 seconds

except KeyboardInterrupt:
    # Ctrl+C was pressed, so cleanup and exit
    pwm.stop()
    GPIO.cleanup()
    print("Exiting...")

``` 

You can use the same code to control the PWM output on the GPIO pin connected to the PWM splitter or hub.

Run the Code: Save the Python script (e.g., fan_control.py) and run it as before using the following command:

`python3 fan_control.py`

Now, the script will run, and the speed of all 10 fans connected to the PWM splitter or hub will increase or decrease together.

Using a PWM splitter or hub simplifies the wiring and allows you to control multiple fans simultaneously with a single PWM signal. This solution is ideal when you want synchronized speed control for multiple fans in your setup.
