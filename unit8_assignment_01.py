__author__ = 'Krish'

profiling_timing = '''
This involves adding sufficient time.perf_counter calls at appropriate places and then calculating difference to calculate
elapsed time.

https://docs.python.org/3/library/time.html#time.perf_counter

This is similar to print debugging, but once you have narrowed down code to a small code section by other means,
this can be very useful and precise.

Generally you will study performance as you vary the input across a range e.g. count = 10, 100, 1000, 10000

profile the 4 methods in unit7_conversion_methods.py using time.clock() in this assignment.

for each value of count, execute the method 5 times and print out the min value and the actual 5 values.
output should look like (a total of 16 lines):
numbers_string1, count = 10, min = 0.0001, actuals = [0.0001, 0.0002, 0.0001, ...]
numbers_string1, count = 100, min = 0.002, actuals = [0.002, 0.002, 0.003, ...]
....
numbers_string4, count = 10000, min = 0.1 actuals = [....]

 Why 5 times and not just once? To get more data and to avoid the effects of noise (the outliers) due to so many things happening 
 on the system (like module imports, garbage collector running etc).
 
 Note: This is a python script which can be run from command line (python.exe <script>.py) or from pycharm (Right click -> Run <script>
 and not the usual pytest tests we have been using so far.
'''

import time
import unit8_conversion_methods as methods

# write clean code to run all the profiles in one go using loops, lists etc. Note that functions are first class objects
# in python so you can hold them in a list.
def profile_perf_counter():
    funcs = [methods.numbers_string1, methods.numbers_string2, methods.numbers_string3, methods.num_strings4]
    for func in funcs:
        for i in range(1,5):
            count = 10 ** i
            actuals = []
            for j in range(0,5):
                t1 = time.clock()
                func(count)
                t2 = time.clock()
                actuals.append(t2-t1)
            minmum = "%.6f" % min(actuals)
            actuals_output = ["%.6f" % k for k in actuals]
            print(func.__name__ + ", count = " + str(count) + ", min = " + minmum + ", actuals = " + str(actuals_output))
    pass



# write your findings on what is the most optimal method and what you learnt in the process.
summary = '''


'''

if __name__ == "__main__":
    profile_perf_counter()
