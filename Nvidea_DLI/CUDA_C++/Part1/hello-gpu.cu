#include <stdio.h>

void helloCPU()
{
  printf("Hello from the CPU.\n");
}


 // `helloGPU` is a kernel that can be launched on the GPU. It must be with a '__global__' keyword and a void return type
 
 __global__ void helloGPU()
{
  printf("Hello also from the GPU.\n");
}

int main()
{

  helloCPU();

  // 'helloGPU' is launched as a kernal on the GPU with 1 block of threads with 1 thread each.

  helloGPU<<<1,1>>>();

  // This synchronizes the completion of the kernal before continuing the CPU thread
  cudaDeviceSynchronize();
   
}
