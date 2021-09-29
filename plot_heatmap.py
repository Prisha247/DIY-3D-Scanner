
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

ser = serial.Serial('COM4',9600) #check on com value before testing
ser.close()
ser.open() 

def read_ser_data():
    ''' Reads data from serial and parses each line into the following format:
            [x, y, sharp_ir_val]
    '''
    ser_data = ser.readline().decode()
    parsed_ser_data = [int(x) for x in ser_data.split()]
    
    return parsed_ser_data

def collect_data():

    with open("heatmap_labels_with_data.csv", 'w') as fd:
        fd.write("Pan,Tilt,Inches\n")

    # initialize data matrix
    size = (pan_len, tilt_len)
    m = np.zeros(size)
    m[:,:] = np.nan

    # length of file
    num_pts = pan_len*tilt_len

    # draw some data in loop
    for i in range(num_pts):
        # wait for a bit
        time.sleep(0.001)

        # fetch new serial data
        ser_data = read_ser_data()
        print(ser_data)

        # load into csv with labels
        with open("heatmap_labels_with_data.csv", 'a') as fd:
            fd.write(f"{ser_data[0]},{ser_data[1]},{ser_data[2]}\n")
        
        # turn pan tilt angles into coordinates
        pan = (ser_data[0]-pan_i)/pan_interval
        tilt = (ser_data[1]-tilt_i)/tilt_interval
        print(pan, tilt)

        # update matrix
        m[int(pan), int(tilt)] = ser_data[2]


    # save data to csv
    np.savetxt("heatmap_matrix.csv", np.array(m), delimiter=",")
    print("saved matrix")

def plot_existing_data():
    # file = open("heatmap_matrix.csv")
    # m = np.loadtxt(file, delimiter=",")
    # m = np.rot90(m, 1)
    # m = np.flip(m,1)
    # # m = np.transpose(m)
    # ax = sns.heatmap(m, linewidth=0.5)
    # plt.show()

    # plotting with labels
    # file = open("heatmap_labels_with_data.csv")

    df = pd.read_csv('heatmap_labels_with_data.csv',header=0)  
    # m = np.loadtxt(file, delimiter=",")
    # m = np.rot90(m, 1)

    # df = df.pivot("Pan", "Tilt", "Inches")
    df = pd.pivot_table(df, index='Pan', columns='Tilt', values='Inches')

    # perform translations to make it look right
    np_df = df.to_numpy()
    np_df = np.rot90(np_df, 1)
    np_df = np.flip(np_df,1)
    ax = sns.heatmap(np_df)
    plt.show()


if __name__ == "__main__":
    # collect_data()
    plot_existing_data()

