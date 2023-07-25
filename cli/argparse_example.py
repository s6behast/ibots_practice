import argparse

# basic example
parser = argparse.ArgumentParser(description="says what the program does")
parser.add_argument("argument", help="description of argument",type=str, default = "a" )
parser.add_argument("-o", "--optional_argument",  help="description of argument",type=float, default = 0.0)

args = parser.parse_args()
print(args)
print (args.argument) # access individual args

