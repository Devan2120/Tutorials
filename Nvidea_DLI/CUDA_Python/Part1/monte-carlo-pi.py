from numba import jit # `jit` is the Numba just-in-time-compiler function
import random
# This is a CPU compiled code

@jit # Use the decorator syntax to mark `monte_carlo_pi` for Numba compilation
def monte_carlo_pi(nsamples): # Estimates value of pi ysing monte carlo method
    acc = 0
    for i in range(nsamples):
        x = random.random()
        y = random.random()
        if (x**2 + y**2) < 1.0:
            acc += 1
    return 4.0 * acc / nsamples