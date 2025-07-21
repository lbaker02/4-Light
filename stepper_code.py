import time
import board
from adafruit_motorkit import MotorKit
from adafruit_motor import stepper
import random
from datetime import datetime
# Initialize the MotorKit object
kit = MotorKit()
# Define the stepper motor
stepper_motor = kit.stepper1
# Function to run the stepper motor
def run_stepper_motor(steps, direction=stepper.FORWARD, speed=0.01):
    for _ in range(steps):
        stepper_motor.onestep(direction=direction, style=stepper.INTERLEAVE)
        time.sleep(speed)
# Main loop with alternating direction and random intervals
try:
    flip_direction = stepper.FORWARD
    step_increment = 1/16 #  1 #1/16  # step size of 1/16
    while True:
        now = datetime.now()
        current_hour = now.hour
        if current_hour < 10 or current_hour >=16:
            print(f"Outside 10am to 4pm exiting at{now}.")
            break
        # Number of steps for each movement (rounded to integer)
        steps = int(step_increment * 10000)  # Scale up for the desired step size
        run_stepper_motor(steps, direction=flip_direction, speed=0.015)
        stepper_motor.release()
        # Flip direction for the next iteration
        flip_direction = stepper.BACKWARD if flip_direction == stepper.FORWARD else stepper.FORWARD
        # Random sleep interval between 20 and 30 seconds
        #sleep_time = random.uniform(20, 30)
        sleep_time = random.uniform(20, 30)
        print(f"Sleeping for {sleep_time:.2f} seconds...")
        time.sleep(sleep_time)
finally:
    # Turn off the stepper motor
    stepper_motor.release()







