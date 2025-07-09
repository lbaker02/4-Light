import RPi.GPIO as GPIO
import time
import random

# Use Broadcom pin numbering
GPIO.setmode(GPIO.BCM)

# Define GPIO pins
DIR_PIN = 3     # Direction pin
STEP_PIN = 20   # Step pin

# Set up pins
GPIO.setup(DIR_PIN, GPIO.OUT)
GPIO.setup(STEP_PIN, GPIO.OUT)

def run_stepper_motor(steps, direction=True, speed=0.01):
    # Set direction
    GPIO.output(DIR_PIN, GPIO.HIGH if direction else GPIO.LOW)
    
    # Pulse the step pin for each step
    for _ in range(steps):
        GPIO.output(STEP_PIN, GPIO.HIGH)
        time.sleep(speed / 2)  # Half-period for high
        GPIO.output(STEP_PIN, GPIO.LOW)
        time.sleep(speed / 2)  # Half-period for low

# Main loop
try:
    flip_direction = True  # True = forward, False = backward
    step_increment = 1 / 16  # Microstepping scaling

    while True:
        # Number of steps for each movement (scale as needed)
        steps = int(step_increment * 10000)
        run_stepper_motor(steps, direction=flip_direction, speed=0.015)

        # Flip direction
        flip_direction = not flip_direction

        # Random delay
        sleep_time = random.uniform(20, 30)
        print(f"Sleeping for {sleep_time:.2f} seconds...")
        time.sleep(sleep_time)

finally:
    GPIO.cleanup()  # Reset all GPIO pins
