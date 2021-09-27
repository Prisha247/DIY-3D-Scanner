import serial
import matplotlib.pyplot as plt
import numpy as np
plt.ion()
fig=plt.figure()


i=0
x=list()
y=list()
i=0
ser = serial.Serial('COM4',9600) #check on com value before testing
ser.close()
ser.open()

while True:
    data = ser.readline().decode()
    data_list = [int(x) for x in data.split()]
    # print(data_list)
    x.append(i)
    y.append(data_list[2])

    plt.scatter(i, data_list[2])
    i += 1
    plt.show()
    plt.pause(0.001)  # Note this correction