#include <stdio.h>
#include <omp.h>


double basic_quad(double x){
	return (-1 * (x*x)) + (2 * x) + 0;
}


double midpoint(double a, double b, int n){
	double res = 0;
	double h = (b-a) / n;
	int i;
	#pragma omp parallel for reduction(+:res) private(i)
	for(i = 0; i < n; i++){
		double x = a + (i + 0.5) * h;
		res = res + basic_quad(x);
	}
	return h * res;
}

int main(){
	double a = 0;
	double b = 2;
	int n = 1000000000;
	printf("Approximation: %f\n", midpoint(a,b,n));
	return 0;
}

