#include <stdio.h>
#include <math.h>
#include<stdlib.h>

// change the value of TYPE to change precision
// single precision - float
// double precision - double
#define TYPE double

// prints the type of roots for these coefficients for a quadratic equation
// then returns a value depending on the value of the discriminant.
int get_discriminant(TYPE a, TYPE b, TYPE c) {
    TYPE discriminant;
    discriminant = b * b - 4 * a * c;

    if (discriminant > 0) {
        printf("Real and distinct roots\n");
        return 1;
    }
    else if (discriminant == 0) {
        printf("Equal roots\n");
        return 0;
    }
    else {
        printf("Real and imaginary roots\n");
        return -1;
    }
}

// takes inputs for coefficients as arguments
int main(int argc, char** argv)
{
    TYPE a, b, c, discriminant;
    a = atof(argv[1]);
    b = atof(argv[2]);
    c = atof(argv[3]);
    return get_discriminant(a, b, c);
}

//  0.50000000 0.1250000000 0.0078125001
