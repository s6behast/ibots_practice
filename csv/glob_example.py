import glob
import os
import sys
import time
from tqdm import tqdm
# glob files

data_dir = 'data'
files = glob.glob(os.path.join(data_dir,'**/*.csv'),recursive=True)

print(files)


# simple progress tracker
i=1
for f in files:
    time.sleep(1)
    sys.stdout.write ("\r%s / %s files loaded" %(i, len(files)))
    i+=1

for x in os.walk('data'):
    print(x)
