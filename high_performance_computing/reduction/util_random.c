#include <util_random.h>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <omp.h>

/**
 * Source: https://people.sc.fsu.edu/~jburkardt/c_src/random_openmp/random_openmp.c
 */
static float _p_random_value(int *seed) {
  *seed = ( (*seed) % 65536 );
  *seed = ( (3125 * (*seed)) % 65536 );
  return (float) (*seed) / 65536.0;
}

int *ompseed = NULL;
int n_ompseed = 0;

void seeds_create(void) {
  if (!ompseed) {
    if (omp_in_parallel()) {
      n_ompseed = omp_get_num_threads();
    }
    else {
      #pragma omp parallel
      n_ompseed = omp_get_num_threads();
    }

    #pragma omp master
    {
      int p;

      //printf("%s: Create %d OpenMP seed(s).\n", __func__, n_ompseed);
      ompseed = (int*) calloc(n_ompseed, sizeof(int));
      for (p=0; p<n_ompseed; p++) {
        ompseed[p] = 3634 + p;
      }
    }
    #pragma omp barrier
  }
}

void seeds_destroy(void) {
  #pragma omp master
  {
    free(ompseed);
    ompseed = NULL;
    n_ompseed = 0;
  }
  #pragma omp barrier
}

float random_uniform(void) {
  int ompthread = omp_get_thread_num();

  if (ompseed && ompthread < n_ompseed) {
    return _p_random_value(&ompseed[ompthread]);
  }
  else {
    return NAN;
  }
}

float random_normal(void) {
  float u, v, s;

  do {
    u = 2.0*(random_uniform () - 0.5); // uniform on [-1,1)
    v = 2.0*(random_uniform () - 0.5); // uniform on [-1,1)
    s = u*u + v*v;
  } while (s > 1.0 || s <= 0.0);

  s = sqrt(-2.0*log(s)/s);

  return u*s;
}

void generate_random_uniform_data(float *data, size_t length, float lo, float hi) {
  size_t i;

  for (i=0; i<length; i=i+1) {
    data[i] = (hi - lo)*random_uniform() + lo;
  }
}

void generate_random_normal_data(float *data, size_t length, float mean, float std) {
  size_t i;

  for (i=0; i<length; i=i+1) {
    data[i] = std*random_normal() + mean;
  }
}

void transform_normal_to_lognormal(float *data, size_t length) {
  size_t i;

  for (i=0; i<length; i=i+1) {
    data[i] = exp(data[i]);
  }
}
