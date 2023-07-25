import h5py
import pandas as pd
import numpy as np

h5_file = 'iris.h5' # name of hdf5 file

####################
#with pandas
####################

#data to write to hdf5
data = pd.read_csv('iris.csv')

#write to file
with  h5py.File(h5_file, 'w') as f:
    for col in data: # wirte each column as dataset
        f.create_dataset(col,data=data[col].values)


#######################
#with numpy
######################
data = np.genfromtxt('iris.csv', delimiter=',', names=True, dtype=None)
#write to file
with h5py.File(h5_file, 'w') as f:
    for col in data.dtype.names:  # wirte each column as dataset
        f.create_dataset(col, data=data[col])


#check file structure
with  h5py.File(h5_file, 'r') as f:
    print(f.keys())
    #print(f.info())
    print(f['species']) # get info about datset
    print(f['species'][()]) # get actual data values)


# attributes

with h5py.File(h5_file, 'a') as f:
    
    f['petal_width'].attrs.create('some info', 'xxxxx')
    f['petal_width'].attrs.create('version', 1)

    print(dict(f['petal_width'].attrs))