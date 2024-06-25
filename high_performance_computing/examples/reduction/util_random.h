#include <stddef.h>

void seeds_create(void);
void seeds_destroy(void);

float random_uniform(void);
float random_normal(void);

void generate_random_uniform_data(float *data, size_t length, float lo, float hi);
void generate_random_normal_data(float *data, size_t length, float mean, float std);

void transform_normal_to_lognormal(float *data, size_t length);

