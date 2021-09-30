'''
This file contains functions to collect and save 3D scan data as well as visualize it on a heatmap. 
'''

import serial
import matplotlib.pyplot as plt
import numpy as np
import time
import pandas as pd 
import seaborn as sns

# data collection params
pan_i = 40
pan_f = 130
pan_interval = 5
tilt_i = 50
tilt_f = 130
tilt_interval = 10
pan_len = int((pan_f-pan_i)/pan_interval) + 1
tilt_len = int((tilt_f-tilt_i)/tilt_interval) + 1

# set up serial communication, comment this out if not connected to arduino
ser = serial.Serial('COM4',9600)
ser.close()
ser.open() 

def read_ser_data():
    ''' Reads data from serial and parses each line into the following format:
            [x, y, sharp_ir_val_inches]
    '''
    ser_data = ser.readline().decode()
    parsed_ser_data = [int(x) for x in ser_data.split()]
    
    return parsed_ser_data


def collect_data():
    ''' Performs a 3D scan and save outputs in a csv file.
    '''
    with open("heatmap_data_with_labels.csv", 'w') as fd:
        fd.write("Pan,Tilt,Inches\n")

    # find total number of points
    num_pts = pan_len*tilt_len

    # collect data
    for i in range(num_pts):
        # wait for a bit
        time.sleep(0.001)

        # fetch new serial data
        ser_data = read_ser_data()
        print(ser_data)

        # append to csv
        with open("heatmap_data_with_labels.csv", 'a') as fd:
            fd.write(f"{ser_data[0]},{ser_data[1]},{ser_data[2]}\n")
        

def plot_existing_data():
    ''' Create heatmap from existing data.
    '''
    df = pd.read_csv('heatmap_data_with_labels.csv',header=0)

    # turn columns into matrix and perform transformations for plotting
    df = pd.pivot_table(df, index='Tilt', columns='Pan', values='Inches')
    df = df.sort_index(axis=0, level=1, ascending=False)
    df = df.sort_index(axis=1, level=1, ascending=False)

    # plot heatmap
    ax = sns.heatmap(df)

    plt.show()


if __name__ == "__main__":
    # collect_data()
    plot_existing_data()