import numpy as np
from numba import cuda

n = 2048*2048 # 4M

# 2D blocks
threads_per_block = (32, 32)
# 2D grid
blocks = (64, 64)
# 32*64 = 2048, The grids form a matrix with each thread assigned to an element in the matrix

# 2048x2048 input matrices
a = np.arange(n).reshape(2048,2048).astype(np.float32)
b = a.copy().astype(np.float32)

# 2048x2048 0-initialized output matrix
out = np.zeros_like(a).astype(np.float32)

d_a = cuda.to_device(a)
d_b = cuda.to_device(b)
d_out = cuda.to_device(out)

@cuda.jit
def matrix_add(a, b, out, coalesced):
    x, y = cuda.grid(2)
    
    if coalesced == True:
        out[y][x] = a[y][x] + b[y][x]        # Column wise addition will be use coalesced data
    else:
        out[x][y] = a[x][y] + b[x][y]

matrix_add[blocks, threads_per_block](d_a, d_b, d_out, True)
result = d_out.copy_to_host()
matrix_add[blocks, threads_per_block](d_a, d_b, d_out, False) # Will take more time to run
result = d_out.copy_to_host()