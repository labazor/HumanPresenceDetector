import serial
import os

ser = serial.Serial(port="/dev/ttyACM0", baudrate=9600)
ser.flushInput()

while True:
    f = open("data.txt", "a")
    ser_bytes = ser.readline()
    data = str(ser_bytes)
    f.write(data)
    f.write("\n")
    f.close()

    os.system("sed -i '1d' data.txt")

    print(ser_bytes)