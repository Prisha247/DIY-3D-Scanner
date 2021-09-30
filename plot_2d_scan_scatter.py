import serial
import matplotlib.pyplot as plt
import numpy as np
plt.ion()
fig=plt.figure()

ser = serial.Serial('COM4',9600) #check on com value before testing
ser.close()
ser.open()

numpts = 19

while (numpts):
    data = ser.readline().decode()
    data_list = [int(x) for x in data.split()]

    plt.scatter(data_list[0], data_list[2])
    plt.xlabel("Pan Angle (degrees)")
    plt.ylabel("Distance (in)")
    plt.title("2D Scan")
    plt.show()
    plt.pause(0.001)  # Note this correction