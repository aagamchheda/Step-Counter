'''After watching the labelled data we can see a lot of noise
    Thus filtering the data to remove noise to get accurate data
'''

import pandas as pd
import csv 
import matplotlib.pyplot as plt
import scipy.signal
import time
import numpy as np
import math

#file = '/Users/Nizam/Desktop/data4Theigh@5.csv'

#, names= column_names, sep = '\t', skiprows= 1,
Accdata = pd.read_csv('foot70.csv')
#print(type(Accdata))
newData = Accdata.values.tolist()
#print(newData)
t = []
x = []
y = []
z = []
Accl_Mod = []
for i in range(len(newData)):
    t.append(newData[i][0])
    y.append(newData[i][2])
    x.append(newData[i][1])
    z.append(newData[i][3])
    Accl_Mod.append(math.sqrt(((newData[i][1])**2)+((newData[i][2])**2)+((newData[i][3])**2)))

#print(x)
#x.plot()
#plt.plot(x[400:2000], label = 'x')

#plt.plot(Accdata.z)

Wn = 0.2
b,a = scipy.signal.butter(4,Wn,'low')
filteredx = scipy.signal.filtfilt(b,a,x)
filteredy = scipy.signal.filtfilt(b,a,y)
filteredz = scipy.signal.filtfilt(b,a,z)
#plt.plot(t,x, label = 'XEuler V. Time')
#plt.plot(t,y, label = 'YEuler V. Time')
#plt.plot(t,z, label = 'ZEuler V. Time')
#plt.plot(t,Accl_Mod, label = 'Accl_Mod V. Time')
plt.plot(t,filteredx, label = 'x v. t')
plt.plot(t,filteredy, label = 'y V. Time')
plt.plot(t,filteredz, label = 'z V. Time')
plt.grid()
plt.legend()
plt.show()
'''
arr = np.array(filteredx)
filterXList = arr.tolist()

arr = np.array(filteredy)
filterYList = arr.tolist()

arr = np.array(filteredz)
filterZList = arr.tolist()


#accumilating filtered values in csv file.
filename_Euler = "03_02_23_Filtered_Thigh_Walk_3_Euler.csv"
def append_to_csv_Euler(d):
    with open(filename_Euler, mode = 'a', newline='') as file:
        writer = csv.writer(file)
        #if file.tell() == 0:
        #    writer.writerow(["Time","x-axis","y-axis","z-axis"])
        writer.writerow(d)
Filtered_data = t,filterXList,filterYList,filterZList
append_to_csv_Euler(Filtered_data)
'''

'''
figx, (ax1, ax2) = plt.subplots(1, 2)
figx.suptitle('X-Axis_V._filteredX')
ax1.plot(t[200:650], x[200:650], 'tab:green')
ax2.plot(t[200:650],filteredx[200:650], 'tab:red')
figx.savefig('(X-Axis)03_02_23_Thigh_Walk_3_Euler.png')
#figx.show()

figy, (ay1, ay2) = plt.subplots(1, 2)
figy.suptitle('Y-Axis_V._filteredY')
ay1.plot(t[200:650],y[200:650], 'tab:green')
ay2.plot(t[200:650],filteredy[200:650], 'tab:red')
figy.savefig('(Y-Axis)03_02_23_Thigh_Walk_3_Euler.png')
#figy.show()

figz, (az1, az2) = plt.subplots(1, 2)
figz.suptitle('Z-Axis_V._filteredZ')
az1.plot(t,z, 'tab:green')
az2.plot(t,filteredz, 'tab:red')
figz.savefig('(Z-Axis)03_02_23_Thigh_Walk_3_Euler.png')
#figz.show()
'''