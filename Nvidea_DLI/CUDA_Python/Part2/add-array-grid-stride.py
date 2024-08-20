from numba import cuda
import numpy as np

@cuda.jit
def add_kernel(x, y, out):
    

    start = cuda.grid(1)
    
    # This calculation gives the total number of threads in the entire grid
    stride = cuda.gridsize(1)   # 1 = one dimensional thread grid, returns a single value.
                                # This Numba-provided convenience function is equivalent to
                                # `cuda.blockDim.x * cuda.gridDim.x`

    # This thread will start work at the data element index equal to that of its own
    # unique index in the grid, and then, will stride the number of threads in the grid each
    # iteration so long as it has not stepped out of the data's bounds. In this way, each
    # thread may work on more than one data element, and together, all threads will work on
    # every data element.
    for i in range(start, x.shape[0], stride):
        # Assuming x and y inputs are same length
        out[i] = x[i] + y[i]
    
n = 100000 # This is far more elements than threads in our grid
x = np.arange(n).astype(np.int32)
y = np.ones_like(x)

d_x = cuda.to_device(x)
d_y = cuda.to_device(y)
d_out = cuda.device_array_like(d_x)

threads_per_block = 128
blocks_per_grid = 30

add_kernel[blocks_per_grid, threads_per_block](d_x, d_y, d_out)
print(d_out.copy_to_host()) # Remember, memory copy carries implicit synchronization