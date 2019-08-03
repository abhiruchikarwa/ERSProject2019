### Setup
- Python version [2.7](https://www.python.org/downloads/)
- C compiler (Not needed for running, but for input values)
- Z3 SAT solver (Not needed for running, but for input values)


### Prerequisites
1. The code for which control-flow instability has to be found, every different branch decision should return different integer values eventually.
2. The automated test case generator right now assumes that the code takes the values needed for the conditional check,
computes the boolean value depending on the input values, makes a decision, executes the code on that branch returns a numeric value and terminates.
3. The automated test case generator terminates when the updated float values are considerably bigger than the 
originally given values. This is a stopping condition as the values are not eligible for the approximate inequality
or equality assert statements and would not flip the critical condition.

### Compile and Run
- Run the program as `python automate.py`
- The program takes the following inputs:
	1. Two absolute paths for the two different compiled versions of code.
	2. The number of variables involved in the critical subexpression used for condition check.
	3. The float values obtained after solving this critical subexpression by symbolic execution.
- The program when given correct input values, finds the critical test cases by modifying the sample inputs.

### Output
- The program prints a list of test cases for which the given compiled versions exhibits control-flow instability, if there exists a list.
- Otherwise terminates and lets the user know that there aren't any test cases.

### Design choices
- When updating the values to check for control-flow instability, it is very difficult to decide which value to update so 
as to flip the critical condition as we don't know any thing about the floating-point arithmetic performed on these values.
- I decided to update the smallest of the given values, as the smallest change in the values can trigger the instability.

### Examples
1. Using `quadratic.c` for displaying CFI due to change in precision:
 - Compile the file `quadratic.c` twice - once with macro `TYPE` defined as `float` and once as `double`.
 - This compilation will require a minor change specified above to the code as the change in precision can only be made by changing the data type of numbers.
 - The inputs obtained from Z3 are  - `0.5, 0.125, 0.0078125`
 - Input these values after running `automate.py`

2. Using `serialized_sum.c` for displaying CFI due to change in optimization level:
 - Compile the file `serialized_sum.c` twice - once with optimization level -O0(`gcc -O0 -o ss0.exe serialized_sum.c`) 
   and once as -O3(`gcc -O3 -o ss3.exe serialized_sum.c`)
 - The inputs obtained from Z3 are  - `1.0 1.0`
 - Input these values after running `automate.py`

 3. Using `hello.c` for displaying CFI due to change in precision:
 - Compile the file `hello.c` twice - once with macro `TYPE` defined as `float` and once as `double`.
 - This compilation will require a minor change specified above to the code as the change in precision can only be made by changing the data type of numbers.
 - The inputs obtained from Z3 are  - `0.5, 1.0`
 - Input these values after running `automate.py`
