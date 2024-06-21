#include <stdio.h>
#include <stdlib.h>
#include <omp.h>
#include <util_random.h>
/* 
 * This example uses more complex methods to approximate pi
 */

#define SIZE 1048576

double approx_pi(size_t n_samples){
	size_t n_accepted_samples = 0;
	size_t i;

	//This allows us to combine values of 1 variable across threads
	//reduction clause will compute some form of reduction on the provided variable, in this case n_accepted_samples
	//private() clause creates private forms of i for each thread (they can iterate at different rates)
	//shared() this variable is the same across threads
	#pragma omp parallel reduction(+:n_accepted_samples) private(i) shared(n_samples)
	{
		#pragma omp for
		for(i = 0; i < n_samples; ++i){
			float x = random_uniform();
			float y = random_uniform();
			if((x*x+y*y) <= 1.0){
				n_accepted_samples += 1;
			}
		}
	}
	return 4.0 * ((double) n_accepted_samples) / ((double) n_samples);
}

int main(int argc, char **argv){
	const size_t N_SAMPLES = SIZE; // = 2^20
	double out;
	int ompsize;
	#pragma omp parallel shared(ompsize)
	{
		ompsize = omp_get_num_threads();
	}

	srand(1000);
	out = approx_pi(N_SAMPLES);
	printf("Approximated value: %f\n", out);
	return 0;
}

