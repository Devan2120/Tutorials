#include <stdio.h>

  /*
   * We are trying to replace the for loop
   * so it can be accelerated.
   * The code prints numbers from 0 to 9 using multiple blocks.
   */

__global__ void loop()
{
  /*
   * This idiomatic expression gives each thread
   * a unique index within the entire grid.
   */

  int i = blockIdx.x * blockDim.x + threadIdx.x;
  printf("%d\n", i);
}

int main()
{
  /*
   * Additional execution configurations that would
   * work and meet the exercises contraints are:
   *
   * <<<5, 2>>>
   * <<<10, 1>>>
   */
  
  loop<<<2, 5>>>();
  cudaDeviceSynchronize();
}
