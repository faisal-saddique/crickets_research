import RPi.GPIO as GPIO

# Set the GPIO pins for the relay control
relay1_pin, relay2_pin = 17, 18

# Set the GPIO mode and pins as output
GPIO.setmode(GPIO.BCM)
GPIO.setup((relay1_pin, relay2_pin), GPIO.OUT, initial=GPIO.LOW)

# Functions to toggle relays
def toggle_relay(pin):
    GPIO.output(pin, not GPIO.input(pin))

# Main loop
while True:
    # Prompt the user to toggle a relay
    choice = input("Enter '1' to toggle relay 1, '2' to toggle relay 2, or 'q' to quit.\n> ")

    # Toggle the selected relay or quit the program
    if choice == '1':
        toggle_relay(relay1_pin)
    elif choice == '2':
        toggle_relay(relay2_pin)
    elif choice == 'q':
        GPIO.cleanup()
        break