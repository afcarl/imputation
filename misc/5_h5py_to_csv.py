import h5py
import argparse
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument("--name", type=str)
args = parser.parse_args()

args.name = args.name.split('/')[-1]
if '.p' not in args.name:
    print(args.name)
    f = h5py.File('./data/mar/' + args.name, 'r')
    X = f['dataset'][:]
    np.savetxt('./data/marcsv/' + args.name + '.csv',
               X, delimiter=',', newline='\n')
