#include <stdio.h>
#include <conio.h>
#include <stdlib.h>

#define product(X, Y) (X * Y)
#define LIMIT 0.5

// change the value of TYPE to change precision
// single precision - float
// double precision - double
#define TYPE float

// takes inputs for two numbers as arguments
// prints of their product is greater than, equal to or less than LIMIT
int main(int argc, char** argv) {
  TYPE a, b, p;
  a = atof(argv[1]);
  b = atof(argv[2]);
  printf("%0.20g %0.20g\n", a, b);
  p = product(a, b);
  printf("%0.20g\n", p);
  if (p > LIMIT) {
    printf("Off limit\n");
    return 1;
  } else {
    printf("In limit\n");
    return 0;
  }
}

// 1.000000000 0.5000000001
// 1.6558990 0.30195079