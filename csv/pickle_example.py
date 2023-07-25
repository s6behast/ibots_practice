import pickle
import numpy as np

data = np.genfromtxt('iris.csv', delimiter=',', names=True, dtype=None)

pickle_file = 'iris.pk'

#dump to file
with open(pickle_file, 'wb') as f:
    pickle.dump(data,f)


#load in data
with open(pickle_file, 'rb') as f:
    data = pickle.load(f)

print(data)