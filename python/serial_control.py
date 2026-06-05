import serial
import time

ser = serial.Serial("COM3", 115200)

time.sleep(2)

while True:
    command = input("Send command: ")

    ser.write(command.encode())