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
