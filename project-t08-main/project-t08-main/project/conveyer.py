from utils.brick import Motor
from utils.brick import Color, configure_ports
from threading import Thread, Event
from time import sleep, time
from collections import deque

def start_loading_motor(LOAD_MOTOR, POWER_LIMIT, SPEED_LIMIT):
    """
    The loading motor will move slower than the other two.
    """
    LOAD_MOTOR.set_limits(POWER_LIMIT, SPEED_LIMIT)  # This should start the motor
    LOAD_MOTOR.set_dps(90)                           # Or maybe this will

def start_sorting_motor(SORTING_MOTOR, POWER_LIMIT, SPEED_LIMIT):
    """
    The sorting motor will be turning continuously while the system is running.
    """
    SORTING_MOTOR.set_limits(POWER_LIMIT, SPEED_LIMIT)  # This should start the motor
    SORTING_MOTOR.set_dps(90)                           # Or maybe this will

def turn_pivot_motor(PIVOT_MOTOR, POWER_LIMIT, SPEED_LIMIT, current: int, target: int):
    """
    Turn the pivot from current angle to target angle.
    """
    PIVOT_MOTOR.set_limits(POWER_LIMIT, SPEED_LIMIT)  # This should start the motor
    PIVOT_MOTOR.set_dps(90)                           # Or maybe this will
    angle_to_turn = current - target                    # Could change to target - current, depending on the rotation direction
    PIVOT_MOTOR.set_position_relative(angle_to_turn)