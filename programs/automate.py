import os
from os.path import isfile


# class for automated test-case generation
class Automate:
    def __init__(self, n, file_path1, file_path2, sat_inputs):
        self.SMALL = 0.0000000001
        self.n = n
        self.file_path1 = file_path1
        self.file_path2 = file_path2
        self.sat_inputs = sat_inputs
        self.min = 0

    # method that returns critical test cases to display control-flow instability.
    # stops finding critical test cases if the given input values have been updated by a very large difference.
    def generate_test_cases(self):
        command1 = self.file_path1
        command2 = self.file_path2
        for i in range(self.n):
            command1 = command1 + ' ' + str(self.sat_inputs[i])
            command2 = command2 + ' ' + str(self.sat_inputs[i])
        r1 = os.system(command1)
        r2 = os.system(command2)
        self.min = min(self.sat_inputs)
        while r1 == r2:
            small_ip = min(self.sat_inputs)
            idx = self.sat_inputs.index(small_ip)
            new_value = self.update_value(small_ip)
            if new_value - self.min > (self.SMALL * 1000):
                print '\n------------------------------------\n------------------------------------\n' \
                      'No critical test cases found'
                self.sat_inputs = []
                break
            self.sat_inputs[idx] = new_value
            command1 = self.file_path1
            command2 = self.file_path2

            for i in range(self.n):
                command1 = command1 + ' ' + str(self.sat_inputs[i])
                command2 = command2 + ' ' + str(self.sat_inputs[i])
            r1 = os.system(command1)
            r2 = os.system(command2)
        return self.sat_inputs

    # updates a given value by a very small value of 0.0000000001
    def update_value(self, number):
        return number + self.SMALL


# uses the Automate class to find critical test cases for the given input programs and their values.
def main():
    file_path1 = raw_input('Absolute path of the first compiled file: ')
    file_path2 = raw_input('Absolute path of the second compiled file: ')
    if not isfile(file_path1) or not isfile(file_path2):
        print 'Enter valid file paths to the compiled files.'
        return
    if file_path1 == file_path2:
        print 'Two different compiled version of files required.'
        return
    n = raw_input('The number of variables in the condition check: ')
    n = int(n)
    sat_inputs = []
    for i in range(n):
        ip = raw_input('Enter the ' + str(i) + 'th input obtained from symbolic execution: ')
        sat_inputs.append(float(ip))

    a = Automate(n, file_path1, file_path2, sat_inputs)
    critical_inputs = a.generate_test_cases()
    if len(critical_inputs) > 0:
        print '\n------------------------------------\n------------------------------------'
        print 'The critical test cases are:'
        for num in critical_inputs:
            print num


# call to main() function
main()

# n = 3
# file_path1 = 'C:\\Users\\abhir\\Documents\\ERS\\project\\programs\\qf.exe'
# file_path2 = 'C:\\Users\\abhir\\Documents\\ERS\\project\\programs\\qd.exe'
# sat_inputs = [0.5, 0.125, 0.0078125]
# n = 2
# file_path1 = 'C:\\Users\\abhir\\Documents\\ERS\\project\\programs\\hello_single.exe'
# file_path2 = 'C:\\Users\\abhir\\Documents\\ERS\\project\\programs\\hello_double.exe'
# sat_inputs = [0.5, 1.0]
