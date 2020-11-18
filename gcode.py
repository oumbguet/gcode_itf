#!/usr/bin/env python3

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

    # Move absolute
    def move_to(self, x, y, z):
        gcode=(
            """G90\nG01 X""" + str(x) +
            """ Y""" + str(y) +
            """ Z""" + str(z) +
            """\nG90\n"""
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


def move_to(gcode, args):
    if (len(args) == 5):
        gcode.move_to(int(args[2]), int(args[3]), int(args[4]))

def move_relative(gcode, args):
    if (len(args) == 5):
        gcode.move_X(int(args[2]));
        gcode.move_Y(int(args[3]));
        gcode.move_Z(int(args[4]));

def display_usage():
    print("\nUSAGE\n\n\t./gcode.py (move_to|move|move_X|move_Y|move_Z) [arg1] [arg2]...\n\n");
    print("\tmove_to\t\tX_axis Y_axis Z_axis");
    print("\t\tMove to absolute coordinates.")
    print("\n\tmove\t\tX_axis Y_axis Z_axis");
    print("\t\tMove to relative coordinates.")
    print("\n\tmove_(X|Y|Z)\trelative_offset_value");
    print("\t\tMove only one axis by relative offset.\n")

if __name__=="__main__":
    gcode = Gcode()
    args = sys.argv;
    functions = {
        'move_to':move_to,
        'move':move_relative
    };

    if (len(args) > 1):
        functions[args[1]](gcode, args);
    else:
        display_usage();