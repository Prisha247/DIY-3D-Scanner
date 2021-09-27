
import serial
import matplotlib.pyplot as plt
import numpy as np
import time

ser = serial.Serial('COM4',9600) #check on com value before testing
ser.close()
ser.open()

# initialize data matrix
size = [180,180]
m = np.empty(size)
m[:,:] = np.nan

# create the figure
fig = plt.figure()
ax = fig.add_subplot(111)
im = ax.imshow(min)
plt.show(block=False)

def read_ser_data():
    ''' Reads data from serial and parses each line into the following format:
            [x, y, sharp_ir_val]
    '''
    ser_data = ser.readline().decode()
    parsed_ser_data = [int(x) for x in ser_data.split()]
    return parsed_ser_data

# draw some data in loop
for i in range(10):
    # wait for a bit
    plt.pause(0.001)

    # fetch new serial data
    ser_data = read_ser_data()

    # replace the image contents
    m[ser_data[0], ser_data[1]] = ser_data[2]
    im.set_array(m) # TODO: need to fix this

    # redraw the figure
    fig.canvas.draw()
    fig.canvas.flush_events()
