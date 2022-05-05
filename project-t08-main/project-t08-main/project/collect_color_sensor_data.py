#!/usr/bin/env python3

"""
This test is used to collect data from the color sensor.
It must be run on the robot.
"""

# Add your imports here, if any
from time import sleep
#from project.collect_us_sensor_data import TOUCH_SENSOR
from utils.brick import EV3ColorSensor, TouchSensor, configure_ports

DELAY_SEC = 0.01

# complete this based on your hardware setup
TOUCH_SENSOR, COLOR_SENSOR = configure_ports(PORT_1=TouchSensor, PORT_2=EV3ColorSensor)

def collect_color_sensor_data(color_sensor_data_file):
    """
    Collect continuous data from the ultrasonic sensor between two button presses.
    color_sensor_data_file: file to store the data
    """
    try:
        output_file = open(color_sensor_data_file, "w")
        while not TOUCH_SENSOR.is_pressed():
            pass  # do nothing while waiting for first button press
        print("Touch sensor pressed")
        sleep(1)
        print("Starting to collect Color samples")
        while not TOUCH_SENSOR.is_pressed():
            color_data = COLOR_SENSOR.get_value()  # Get RGB and unknown value
            print(color_data)
            #get the RGB vlaues
            output_file.write("{:d},{:d},{:d}\n".format(color_data[0], color_data[1], color_data[2])) 
            sleep(DELAY_SEC)
    except BaseException: # capture all exceptions including KeyboardInterrupt (Ctrl-C)
        pass
    finally:
        print("Done collecting color samples")
        output_file.close()
        exit()


if __name__ == "__main__":
    collect_color_sensor_data()
