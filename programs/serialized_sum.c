#include <stdio.h>
#include <stdlib.h>
#include <stdlib.h>

// reduces the value of second variable such that it is very small than the first variable.
float epsilon(float a, float b) {
  float eps = b;
  while (a + eps != a) {
    eps /= 2.0f;
  }
  return eps;
}

// prints if the sum of two input variables is less than the first variable.
// returns separate values depending on the value of the sum.
int get_sum(float input1, float input2) {
  float a = input1;
  float b = epsilon(input1, input2);
  float c = -b;
  float sum = a + b + c;
  if (sum < a) {
      printf("The sum is lesser than the first input");
      return 0;
  }
  else {
      printf("The sum is greater than or equal to the first input");
      return 1;
  }
}

// takes input for two float numbers as arguments.
// prints if the sum of two input numbers is less than the first number.
int main(int argc, char** argv)
{
  float i1 = strtod(argv[1], NULL);
  float i2 = strtod(argv[2], NULL);
  return get_sum(i1, i2);
}

// 1.0 1.0
