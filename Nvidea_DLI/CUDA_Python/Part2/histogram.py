import numpy as np
from numba import cuda
# Code to create a histogram

@cuda.jit
def cuda_histogram(x, xmin, xmax, histogram_out):
    '''Increment bin counts in histogram_out, given histogram range [xmin, xmax).'''
    
    nbins = histogram_out.shape[0]
    bin_width = (xmax - xmin) / nbins
    
    start = cuda.grid(1)
    stride=cuda.gridsize(1)
    
    for i in range(start, x.shape[0], stride):
        bin_number = np.int32((x[i] - xmin)/bin_width)
        if bin_number >= 0 and bin_number < histogram_out.shape[0]:
            # only increment if in range
            cuda.atomic.add(histogram_out, bin_number, 1) # To prevent errors due to multiple threads accessing the same memory
            # Adds the value '1' to the element of the array 'histogram_out' at index 'bin_number'

x = np.random.normal(size=10000, loc=0, scale=1).astype(np.float32)
xmin = np.float32(-4.0)
xmax = np.float32(4.0)
d_x = cuda.to_device(x)
d_histogram_out = cuda.to_device(np.zeros(shape=10, dtype=np.int32))

blocks = 128
threads_per_block = 64

cuda_histogram[blocks, threads_per_block](d_x, xmin, xmax, d_histogram_out)