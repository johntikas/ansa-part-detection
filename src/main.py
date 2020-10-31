import os
import time
import timeit

import numpy as np

import ansa
from ansa import guitk, base, utils, dm

class Settings(object):
    def __init__(self, parts, tolerance):
    	self.tolerance

def main():
    start_time = time.time()
    idx = 6
    nx, ny = (idx+1, idx+1)
    x = np.linspace(start=0, stop=idx, num=nx)
    y = np.linspace(start=0, stop=idx, num=ny)
    xv, yv = np.meshgrid(x, y)
    print(xv)
    print(yv)
    stop_time = time.time()
    time_diff = stop_time - start_time
    time_diff_str = '{:.3f} seconds'.format(time_diff)
    print(time_diff_str)

if __name__ == '__main__':
	main()
