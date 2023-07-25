import yaml
import os
input_file = 'settings.yaml'

#basic 
with open(input_file, 'r') as f:
    dat = yaml.safe_load(f)

    
#with fancy exceptions
if os.path.isfile(input_file):
    with open(input_file, 'r') as f:
        try:
            dat = yaml.safe_load(f)
        except Exception as e:
            print('problem loading file')
            print(str(e))
            exit()
else:
    raise FileNotFoundError('%s not found!'%input_file)

print(dat)