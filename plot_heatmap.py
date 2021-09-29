
import serial
import matplotlib.pyplot as plt
import numpy as np
import time
import pandas as pd 
import seaborn as sns

ser = serial.Serial('COM4',9600) #check on com value before testing
ser.close()
ser.open() 

# data collection params
pan_i = 40
pan_f = 130
pan_interval = 5
tilt_i = 50
tilt_f = 130
tilt_interval = 10


def read_ser_data():
    ''' Reads data from serial and parses each line into the following format:
            [x, y, sharp_ir_val]
    '''
    ser_data = ser.readline().decode()
    parsed_ser_data = [int(x) for x in ser_data.split()]
    
    return parsed_ser_data

def run_live_visualization():

    # initialize data matrix
    pan_len = int((pan_f-pan_i)/pan_interval) + 1
    tilt_len = int((tilt_f-tilt_i)/tilt_interval) + 1
    size = (pan_len, tilt_len)
    m = np.zeros(size)
    m[:,:] = np.nan

    # create the figure
    fig = plt.figure()
    ax = fig.add_subplot(111)
    # im = ax.imshow(m)
    im = ax.imshow(np.random.random(size))

    plt.show(block=False)

    # length of file
    num_pts = pan_len*tilt_len

    # draw some data in loop
    for i in range(20):
        # wait for a bit
        time.sleep(0.001)

        # fetch new serial data
        ser_data = read_ser_data()
        print(ser_data)

        # turn pan tilt angles into coordinates
        pan = (ser_data[0]-pan_i)/pan_interval
        tilt = (ser_data[1]-tilt_i)/tilt_interval
        print(pan, tilt)
        # replace the image contents
        m[int(pan), int(tilt)] = ser_data[2]
        # im.set_array(np.array(m))

        # plt.imshow(m, cmap='hot', interpolation='nearest')
        # ax = sns.heatmap(m, linewidth=0.5)
        # plt.show()

        # redraw the figure
        # fig.canvas.draw()
        # fig.canvas.flush_events()

    # ax = sns.heatmap(m, linewidth=0.5)
    # plt.show()
    # save data to csv
    np.savetxt("heatmap_matrix.csv", m, delimiter=",")

    # pd.DataFrame(m).to_csv("heatmap_matrix.csv")
    print("saved graph")

def plot_existing_data():
    file = open("heatmap_matrix.csv")
    m = np.loadtxt(file, delimiter=",")
    ax = sns.heatmap(m, linewidth=0.5)
    plt.show()

if __name__ == "__main__":
    # run_live_visualization()
    plot_existing_data()

