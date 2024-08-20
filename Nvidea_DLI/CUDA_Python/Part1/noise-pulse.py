import math
import numpy as np
from matplotlib import pyplot as plt
from numba import cuda

@vectorize(['float32(float32, float32, float32)'], target='cuda')
def make_pulses(i, period, amplitude):
    return max(math.sin(i / period) - 0.3, 0.0) * amplitude

@vectorize(['float32(float32, float32)'], target='cuda')
def add_ufunc(x, y):
    return x + y

n = 100000
noise = (np.random.normal(size=n) * 3).astype(np.float32)
t = np.arange(n, dtype=np.float32)
period = n / 23

# Transfer data to device
d_noise = cuda.to_device(noise)
d_t = cuda.to_device(t)
d_pulses = cuda.device_array(shape=(n,), dtype=np.float32)  # Define an array in the device

make_pulses(d_t, period, 100.0, out=d_pulses)  # The device array is passed as the output array, so data is not transferred to host 
waveform = add_ufunc(d_pulses, d_noise) # Here wveform is also a device array
print(waveform)
print(waveform.copy_to_host()) # This transfers the data from device to host

plt.plot(waveform)