#G90 Positionnement absolu
#G91 Positionnement relatif
#G00 FAST
#G01 AT F SPEEDRATE
#Fx SPEEDRATE IN MM/MIN

import os
import sys
import serial
import time

class Gcode():
    gcode = "";
    speed = 6000.0;

    def __init__(self):
        self.serialPort=None

    # X-Axis
    def move_X(self, val):                      # Move X-axis by val
        gcode=(
            """G91\nG01 X""" +
            str(val) +
            """\nG90\n"""
        )
        print(gcode)

    def reset_X(self):                          # Reset X-axis to 0
        gcode=(
            """G28 X0\n"""
        )
        print(gcode)

    # Y-Axis
    def move_Y(self, val):                      # Move Y-axis by val
        gcode=(
            """G91\nG01 Y""" +
            str(val) +
            """\nG90\n"""
        )
        print(gcode)

    def reset_Y(self):                          # Reset Y-axis to 0
        gcode=(
            """G28 Y0\n"""
        )
        print(gcode)

    # Z-Axis
    def move_Z(self, val):                      # Move Z-axis by val
        gcode=(
            """G91\nG01 Z""" +
            str(val) +
            """\nG90\n"""
        )
        print(gcode)

    def reset_Z(self):                          # Reset Z-axis to 0
        gcode=(
            """G28 Z0\n"""
        )
        print(gcode)

    # Speed
    def set_speed(self, val):                   # Set moving speedrate F
        gcode=(
            """G01 F""" + str(val) + """\n"""
        )
        print(gcode)

    # Serial port
    def init_port(self):
        self.serialPort = serial.Serial("/dev/ttyACM0")

    def send_gcode(self, command):              # Send gcode on serial port
        if (self.serialPort):                   # If serial port already exists
            self.serialPort.close();            # Close it
        self.init_port();                       # Init and open serial port
        for line in command.splitlines():       # For each line of the gcode command
            self.serialPort.write(line);        # Send line to the serial port

if __name__=="__main__":
    gcode = Gcode()
