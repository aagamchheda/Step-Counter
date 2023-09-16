#Plotting After getting the data
import pandas as pd
import matplotlib.pyplot as plt

column_names =[
    'x',
    'y',
    'z',
    't',
]

#df= pd.read_csv('ThighACCdata.txt', sep='\t', header=None, names=column_names)
#df= pd.read_csv('classificationdata.txt', sep='\t', header=None, names=column_names)  #one with tutorial
#df= pd.read_csv('FootACCdata.txt', sep='\t', header=None, names=column_names)
#df= pd.read_csv('CalfACCdata.txt', sep='\t', header=None, names=column_names)
#df= pd.read_csv('finalhandaccel.txt', sep='\t', header=None, names=column_names)
#df= pd.read_csv('revisedHandACCdata.txt', sep='\t', header=None, names=column_names)
df= pd.read_csv('FootACCdata.txt', sep='\t', header=None, names=column_names)
plt.figure()
plt.plot(df.x)
plt.plot(df.y)
plt.plot(df.z)

plt.show()