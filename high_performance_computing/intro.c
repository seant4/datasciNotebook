#include <omp.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char* argv[]){
	int nthreads;
	int thread_id;

	//Initializes parallel region
	#pragma omp parallel private(nthreads, thread_id) //this gives the program the number of threads, and the individual thread id
	{
		thread_id = omp_get_thread_num(); //Get current thread id
		printf("current thread: %d\n", thread_id);
	}
}

